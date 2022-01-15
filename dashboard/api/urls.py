from django.urls import path
from . import views

urlpatterns=[    
    path('init/',views.initial),
    path('update/<int:code>/',views.update),
    path('list/',views.list)
]