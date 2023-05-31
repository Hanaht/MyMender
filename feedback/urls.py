from django.urls import path
from .views import CreateFeedback,User_filter

urlpatterns = [
    path('', CreateFeedback.as_view()),
    # path('<str:pk>', Bid.as_view())
        path('search', User_filter.as_view()),

    
]