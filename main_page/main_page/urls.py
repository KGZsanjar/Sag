from django.urls import path, include
from  . import views

urlpatterns = [
        path('about/', views.about, name='about'),
        path('about_my_pet/', views.about_my_pet, name='about_my_pet'),
        path('current_time/', views.current_tima),
        path('book/', views.BooklistView.as_view(), name='booklist'),
        path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    ]


