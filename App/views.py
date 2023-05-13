from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView,CreateView,FormView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Todo
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
# Create your views here.
class Registers(FormView):
    form_class=UserCreationForm
    template_name='register.html'
    redirect_authenticated_user=True
    success_url=reverse_lazy('all')
    
    def form_valid(self, form):
        user=form.save()
        if user is not None :
           login(self.request,user)
        return super(Registers,self).form_valid(form)
    
    

class Logins(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    success_url=reverse_lazy('all')
    
    def get_success_url(self):
        return reverse_lazy('all')
    
    
class Create(CreateView):
    model=Todo
    template_name='create.html'
    fields=['title','description','completed']
    success_url=reverse_lazy('all')
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(Create,self).form_valid(form)
    
    


class List(ListView):
    model=Todo
    template_name='alllist.html'
    context_object_name='todo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo"] =context['todo'].filter(user=self.request.user) 
        search= self.request.GET.get('search')
        if search:
            context['todo']=context['todo'].filter(title__istartswith=search)
            context['search']=search
        return context
    
    
    

class Detail(DetailView):
    model=Todo
    template_name='singlelist.html'
    context_object_name='todo'
    success_url=reverse_lazy('all')

class Deletes(DeleteView):
    model=Todo
    template_name='delete.html'
    context_object_name='todo'
    success_url=reverse_lazy('all')

class Update(UpdateView):
    model=Todo
    template_name='update.html'
    fields='__all__'
    success_url=reverse_lazy('all')


