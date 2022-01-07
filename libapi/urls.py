from django.urls import path
from . import views

urlpatterns=[
    path('',views.apiIndex,name="apiIndex"),
    path('book-list/',views.bookList,name="book-list"),
    path('book-detail/<int:ser>',views.bookDetail,name="book-detail"),
    path('book-new/',views.bookCreate,name="book-new"),
    path('book-delete/<int:ser>',views.bookDelete,name="book-delete"),
    path('user-list/',views.userList,name="user-list"),
    path('user-detail/<int:reg>',views.userDetail,name="user-detail"),
    path('user-new/',views.userCreate,name="user-new"),
    path('user-delete/<int:reg>&<int:ser>',views.userDelete,name="user-delete"),
]

