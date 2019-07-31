from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('acctsvcs', views.acctsvcs, name='acctsvcs'),
    path('taxsvcs', views.taxsvcs, name='taxsvcs'),
    path('contactus', views.contactus, name='contactus')
]