from django.urls import path
from . import views

urlpatterns=[
    path('',views.apiIndex,name="apiIndex"),
    path('book/list/',views.bookList,name="book-list"),
    path('book/list/return=<int:status>',views.bookListReturn),
    path('book/<int:ser>/',views.bookDetail),
    path('book/add/',views.bookCreate),
    path('book/<int:ser>/delete/',views.bookDelete),
    path('book/<int:ser>/update/',views.bookUpdate),
    path('user/list/',views.userList,name="user-list"),
    path('user/<int:reg>/',views.userDetail),
    path('user/add/',views.userAdd,name="user-add"),
    path('user/<int:reg>/delete/<int:ser>/',views.userDelete),
    path('user/<int:reg>/update/<int:ser>/',views.userUpdate),
    path('user/<int:reg>/update/<int:ser>/return=<int:status>',views.userReturn)
]

