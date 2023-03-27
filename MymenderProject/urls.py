from django.urls import path, include
from django.contrib import admin

urlpatterns =[
    path('admin/', admin.site.urls),
    path('api/bid/', include('Bid.urls')),
    path('api/feedback/', include('feedback.urls')),
    path('announce/', include('announcement.urls')),
    path('auth/', include('Auth.urls')),

]