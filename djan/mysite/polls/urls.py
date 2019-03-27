from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('detail/<id1>', views.detail,name='detail')
]