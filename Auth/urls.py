from django.urls import path
from . import views
from knox import views as knox_views
from .views import  user_list, admin_list,dep,register_user,UserLoginView,UserLogoutView,register_admin,User_filter
urlpatterns = [
     path('user_list/',user_list.as_view(), name="user_list"),
     #path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
     path('register_user/',register_user.as_view()),
     path('register_admin/',register_admin.as_view()),
     path('adUser_filtermin_list/',admin_list.as_view()),
     path('dep/',dep.as_view(),name="dep"),
     
     path('login/', UserLoginView.as_view()),
     path('login/', UserLogoutView.as_view()),
     path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
     path('userSearch/', User_filter.as_view())

]