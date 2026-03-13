from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('works/', views.works, name='works'),
    path('legacy/', views.legacy, name='legacy'),
    path('documents/', views.documents_list, name='documents'),
    path('documents/<int:pk>/download/', views.download_document, name='download_document'),
    path('books/', views.books_list, name='books'),
    path('books/<int:pk>/download/', views.download_book, name='download_book'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
