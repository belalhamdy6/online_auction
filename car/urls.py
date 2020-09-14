from django.urls import path
from . import views
from . import api

app_name = 'car'
urlpatterns = [
    path('job/', views.job_list, name='job_list'),
    path('', views.index, name='index'),
    path('add/', views.add_job, name='add'),
    path('<str:slug>', views.job_details, name='job_details'),
    path('bid/<str:slug>', views.bid, name='bid'),


    ## api
    path('api/cars', api.CarListApi.as_view(), name='car_list_api'),
    path('api/cars/<int:id>', api.CarDetail.as_view(), name='car_detail_api'),
    path('api/bid', api.Bid_Detail.as_view(), name='car_bid_api')
]