from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map', views.map, name='map'),
    path('pay', views.pay, name='pay'),
    path('widget', views.widget, name='widget'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('globe', views.globe, name='globe')
]
