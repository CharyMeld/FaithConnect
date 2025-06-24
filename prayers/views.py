from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import PrayerRequest, PrayerResponse
from .forms import PrayerRequestForm, PrayerResponseForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Q
import csv
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


User = get_user_model()



@login_required
def prayers_page(request):
    prayers_list = PrayerRequest.objects.all().order_by('-created_at')
    paginator = Paginator(prayers_list, 10)  # 10 prayers per page

    page_number = request.GET.get('page')
    prayers = paginator.get_page(page_number)

    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            prayer = form.save(commit=False)
            prayer.user = request.user
            prayer.save()
            return redirect('prayers_page')
    else:
        form = PrayerRequestForm()
    return render(request, 'prayers/prayers.html', {'prayers': prayers, 'form': form})



@login_required
def send_response(request, prayer_id):
    prayer_request = get_object_or_404(PrayerRequest, id=prayer_id)
    if request.method == 'POST':
        form = PrayerResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.prayer_request = prayer_request
            response.sender = request.user
            response.save()

            # Send email notification
            subject = f"New response to your prayer request: {prayer_request.title}"
            message = (
                f"Hi {prayer_request.user.username},\n\n"
                f"You have received a new response to your prayer request:\n\n"
                f"\"{response.message}\"\n\n"
                f"Log in to FaithConnect to view it.\n\n"
                f"Blessings,\n"
                f"The FaithConnect Team"
            )

            return redirect('prayers:prayers_page')
    else:
        form = PrayerResponseForm()
    return render(request, 'prayers/send_response.html', {'prayer_request': prayer_request, 'form': form})


@login_required
def prayer_detail(request, pk):
    prayer = get_object_or_404(PrayerRequest, pk=pk)
    responses = PrayerResponse.objects.filter(prayer_request=prayer).order_by('-created_at')
    return render(request, 'prayers/prayer_detail.html', {'prayer': prayer, 'responses': responses})

@login_required
def inbox(request):
    prayers = PrayerRequest.objects.filter(user=request.user).order_by('-created_at')
    query = request.GET.get('q', '')
    prayers = PrayerRequest.objects.all()

    if query:
        prayers = prayers.filter(Q(name__icontains=query) | Q(email__icontains=query))

    prayers = prayers.order_by('-created_at')

    paginator = Paginator(prayers, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'prayers/inbox.html', {
        'prayers': page_obj,
        'query': query
    })


@login_required
def create_prayer_request(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            prayer = form.save(commit=False)
            prayer.user = request.user
            prayer.save()
            return redirect('prayers_page')
    else:
        form = PrayerRequestForm()
    return render(request, 'prayers/create_prayer_request.html', {'form': form})

@login_required
def user_profile(request):
    user = request.user
    prayers = PrayerRequest.objects.filter(user=user).order_by('-created_at')
    responses = PrayerResponse.objects.filter(sender=user).order_by('-created_at')
    return render(request, 'prayers/user_profile.html', {
        'profile_user': user,
        'user_requests': prayers,
        'user_responses': responses
    })

def export_prayers_csv(request):
    prayers = PrayerRequest.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prayer_requests.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Message', 'Date'])

    for p in prayers:
        writer.writerow([p.name, p.email, p.message, p.created_at])

    return response

@require_POST
def mark_prayed(request):
    prayer_id = request.POST.get('prayer_id')
    prayer = get_object_or_404(PrayerRequest, id=prayer_id)
    prayer.is_prayed = not prayer.is_prayed
    prayer.save()
    return JsonResponse({'status': 'success', 'is_prayed': prayer.is_prayed})

@login_required
@require_POST
def reply_prayer(request):
    to_email = request.POST.get('to_email')
    reply_message = request.POST.get('reply_message')

    subject = "Reply to your prayer request"
    send_mail(subject, reply_message, settings.DEFAULT_FROM_EMAIL, [to_email])

    messages.success(request, f"Reply sent to {to_email}")
    return redirect('inbox')

@csrf_exempt  # Optional if CSRF token is used in form
def reply_prayer(request):
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        message = request.POST.get('reply_message')

        if to_email and message:
            send_mail(
                'Reply to Your Prayer Request',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [to_email],
                fail_silently=False,
            )
            messages.success(request, f"Reply sent to {to_email}.")
        else:
            messages.error(request, "Failed to send reply. Please provide all fields.")

    return redirect('inbox')  # Assumes 'inbox' is a named URL for the inbox view
