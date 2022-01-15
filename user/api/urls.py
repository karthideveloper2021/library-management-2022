from django.urls import path
from . import views

urlpatterns=[    
    path('list/',views.userList,name="user-list"),
    path('<int:reg>/',views.userDetail),
    path('<int:reg>/<int:ser>/',views.userDetailSpecific),
    path('<int:reg>/records/',views.userDetailRecords),
    path('add/',views.userAdd),
    path('<int:userId>/delete/',views.userDelete),
    path('<int:userId>/update/',views.userUpdate),
    path('<int:userId>/update/return=<int:status>',views.userReturn),
    
]
