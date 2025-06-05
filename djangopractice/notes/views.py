from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, RegisterForm, NoteForm
from .models import Note
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(AuthLoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class NoteView(LoginRequiredMixin, FormView):
    template_name = 'notes.html'
    login_url = 'login'
    redirect_field_name = 'next'
    form_class = NoteForm

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(user=self.request.user)
        return context
    
    def form_valid(self, form):
        note = form.save(commit = False)
        note.user = self.request.user
        form.save()
        return super().form_valid(form)
    

class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note')

    def get_queryset(self):
        return Note.objects.filter(user = self.request.user)
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return super().delete(request, *args, **kwargs)

