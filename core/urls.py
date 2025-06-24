from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views




app_name = 'core'  # or your app name

urlpatterns = [
    path('', views.home, name='home'),  # root URL -> home view
    path('home/', views.home, name='home'),  # optional: if you want /home too
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/random-verse/', views.random_verse, name='random_verse'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('create/', views.post_create, name='create'),

    # Dashboard feature pages
    path('connect/', views.connect_page, name='connect_page'),
    path('share/', views.share_page, name='share_page'),
    path('devotionals/', views.devotionals_page, name='devotionals_page'),
    path('messages/', views.messages_page, name='messages_page'),
    path('prayers/', views.prayers_page, name='prayers_page'),
    path('events/', views.events_page, name='events_page'),
    path('grow/', views.grow_page, name='grow_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

