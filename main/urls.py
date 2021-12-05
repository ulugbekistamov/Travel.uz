from django.urls import path
from .views import *


urlpatterns = [
    path('',LadingPageView.as_view(),name='index'), 
    path('viloyat/',viloyatPageView.as_view(),name='viloyat'), 
    path('teatr/',TeatrPageView.as_view(),name='teatr'),
    path('restaran/',RestoranPageView.as_view(),name='restaran'),
    path('maskan/',MaskanPageView.as_view(),name='maskan'),
    path('hotel/',HotelPageView.as_view(),name='hotel'),
    path('hotel-main/',HotelmainPageView.as_view(),name='hotel-main'),
    
    
     
]
