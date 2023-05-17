from django.urls import path, include
from django.contrib import admin

urlpatterns =[
    # path('admin/', admin.site.urls),
    path('api/bid/', include('Bid.urls')),
    path('api/feedback/', include('feedback.urls')),
    path('announce/', include('announcement.urls')),
    path('auth/', include('Auth.urls')),
    path('api/Service/', include('service.urls')),
    path('api/Notification/', include('notification.urls')),
    path('api/form/', include('Form.urls')),


]


