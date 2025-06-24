from django.shortcuts import render
from prayers.models import PrayerRequest, PrayerResponse

def user_profile(request, username):
    user = get_object_or_404(settings.AUTH_USER_MODEL, username=username)
    user_requests = user.prayer_requests.all()
    user_responses = user.sent_prayers.all()
    return render(request, 'users/profile.html', {
        'profile_user': user,
        'user_requests': user_requests,
        'user_responses': user_responses
    })

