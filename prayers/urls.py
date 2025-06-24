from django.urls import path
from . import views  
from .views import prayers_page, prayer_detail, send_response, user_profile, export_prayers_csv



app_name = 'prayers'

urlpatterns = [
    path('', views.prayers_page, name='prayers_page'),
    path('<int:prayer_id>/respond/', views.send_response, name='send_response'),
    #path('inbox/', views.inbox, name='prayers_inbox'),
    path('inbox/', views.inbox, name='inbox'),
    path('create/', views.create_prayer_request, name='create_prayer_request'),
    path('prayer/<int:pk>/', prayer_detail, name='prayer_detail'), 
    path('user/profile/', views.user_profile, name='user_profile'),
    path('prayers/export/', export_prayers_csv, name='export_prayers_csv'),
    path('prayers/mark_prayed/', views.mark_prayed, name='mark_prayed'),
    path('prayers/reply/', views.reply_prayer, name='reply_prayer'),



]



