
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bid/', include('Bid.urls')),
    path('api/feedback/', include('feedback.urls'))

]
