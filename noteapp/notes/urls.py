from django.urls import path
from .views import IndexView, LoginView, RegisterView, NoteView, DeleteNoteView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('note/', NoteView.as_view(), name='note'),
    path('delete/note/<int:pk>/', DeleteNoteView.as_view(), name="delete_note"),
]