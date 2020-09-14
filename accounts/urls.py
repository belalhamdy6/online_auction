from django.urls import path
from . import views
from . import api

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),

    ### Profile api
    path('api/profile', api.Profile_Api.as_view(), name='profile_api'),
    path('api/user', api.User_Api.as_view(), name='user_api'),



]
