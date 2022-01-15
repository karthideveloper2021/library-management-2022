from django.urls import path
from . import views

urlpatterns=[    
    path('settings/<int:code>&<int:val>/',views.settingsParameters)
]