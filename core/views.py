from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, PostForm
from .models import BibleVerse  
from post.models import Post, PostFile 
from django.contrib.auth.decorators import login_required
import random
from django.http import JsonResponse
from user_messages.models import Message, ChatRoom  
from django.urls import reverse

# Home page → display all posts (public)
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

# Dashboard → logged-in users only + features list + posts + messages
@login_required
def dashboard(request):
    # Try to get latest chat room user is in
    latest_room = ChatRoom.objects.filter(participants=request.user).order_by('-created_at').first()


    if latest_room:
        messages_url = reverse("user_messages:chat_room", args=[latest_room.id])
    else:
        # fallback to chat list if no room found
        messages_url = reverse("user_messages:chat_list")

    features = [
    {
        "title": "Connect",
        "icon": "fas fa-users",
        "description": "Find and connect with other believers.",
        "url": reverse("core:connect_page"),
    },
    {
        "title": "Share",
        "icon": "fas fa-pray",
        "description": "Share your faith journey.",
        "url": reverse("core:share_page"),
    },
    {
        "title": "Devotionals",
        "icon": "fas fa-book",
        "description": "Daily spiritual nourishment.",
        "url": reverse("core:devotionals_page"),
    },
    {
        "title": "Messages",
        "icon": "fas fa-envelope",
        "description": "Send and receive encouragement.",
        "url": reverse("user_messages:messages_home")
        
    },
    {
        "title": "Prayers",
        "icon": "fas fa-hands",
        "description": "Share and view prayer requests.",
        "url": reverse("prayers:prayers_page"),
    },
    {
        "title": "Events",
        "icon": "fas fa-calendar-alt",
        "description": "Discover Christian events.",
        "url": reverse("core:events_page"),
    },
    {
        "title": "Grow",
        "icon": "fas fa-bible",
        "description": "Grow in faith with discussions.",
        "url": reverse("core:grow_page"),
    },
    {
        "title": "Post",
        "icon": "fas fa-pen",
        "description": "Create a new post to share.",
        "url": reverse("post:post_list"),
    },
]


    posts = Post.objects.all().order_by('-created_at')
    user_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, "dashboard.html", {
        "features": features, 
        "posts": posts,
        "user_messages": user_messages,
        
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        files = request.FILES.getlist('media_files')

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            for f in files:
                PostFile.objects.create(post=post, file=f)

            return redirect('home')  # redirect to home page or dashboard
    else:
        form = PostForm()

    return render(request, "post/create_post.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('core:login')

def random_verse(request):
    verses = list(BibleVerse.objects.all())
    if not verses:
        return JsonResponse({'error': 'No verses in the database'})
    
    verse = random.choice(verses)
    return JsonResponse({
        'book': verse.book,
        'chapter': verse.chapter,
        'verse': verse.verse,
        'text': verse.text
    })

def about_view(request):
    return render(request, 'about.html')

def blog_view(request):
    return render(request, 'blog.html')

def contact_view(request):
    return render(request, 'contact.html')

# Additional feature pages (link targets)
@login_required
def connect_page(request):
    return render(request, 'features/connect.html')

@login_required
def share_page(request):
    return render(request, 'features/share.html')

@login_required
def devotionals_page(request):
    return render(request, 'features/devotionals.html')

@login_required
def messages_page(request):
    return render(request, 'user_messages/chat_room.html')

@login_required
def prayers_page(request):
    return render(request, 'prayers/prayers.html')

@login_required
def events_page(request):
    return render(request, 'features/events.html')

@login_required
def grow_page(request):
    return render(request, 'features/grow.html')

