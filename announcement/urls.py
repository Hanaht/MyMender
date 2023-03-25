from django.urls import path
from .views import announce_list, dep
urlpatterns = [
     path('list/',announce_list.as_view()),
     path('dep/',dep.as_view()),
]
