from django.urls import path
from . import views

urlpatterns=[
    path('',views.apiIndex,name="apiIndex"),
    path('list/',views.bookList,name="book-list"),
    path('list/issued=<int:status>/',views.bookListReturn),
    path('<int:ser>/',views.bookDetail),
    path('add/',views.bookCreate),
    path('<int:ser>/delete/',views.bookDelete),
    path('<int:ser>/update/',views.bookUpdate),
]