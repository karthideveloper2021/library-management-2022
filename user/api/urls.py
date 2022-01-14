from django.urls import path
from . import views

urlpatterns=[    
    path('list/',views.userList,name="user-list"),
    path('<int:reg>/',views.userDetail),
    path('<int:reg>/records/',views.userDetailRecords),
    path('add/',views.userAdd,name="user-add"),
    path('<int:reg>/<int:ser>/delete/',views.userDelete),
    path('<int:reg>/<int:ser>/update/',views.userUpdate),
    path('<int:reg>/<int:ser>/update/return=<int:status>',views.userReturn),
    path('settings/<int:code>&<int:val>/',views.settingsParameters)
]
