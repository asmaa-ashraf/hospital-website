
from django.urls import path

from . import views
#from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/',views.detail,name='detail'),
    path('doctor/<int:pk>/',views.doctor_detail,name='doctor_detail'),
    
]