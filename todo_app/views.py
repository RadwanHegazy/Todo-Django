from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import ListView, View, FormView
from django.contrib.auth.models import User
from django.views.generic.base import RedirectView, TemplateView
from .models import Todo
from .forms import SignupForm
from django.contrib.auth.views import auth_login
# Create your views here.



class home (View) :
    model = Todo
    template_name = 'home.html'

    def post (self, request) :
        todo = request.POST['todo']
        Todo.create_action(text=todo,user=request.user)
        return redirect('home')

    def get(self, request):
        if request.user.is_authenticated:
            return render(request,'home.html',{'object_list':Todo.objects.filter(user=request.user).all()})
        else:
            return redirect('login')


class is_done (View) :
    model = Todo
    def get (self,request,id) :
        Todo.make_done(id=id,user=request.user)
        return redirect('home')


class signup (FormView) :
    template_name = 'signup.html'
    form_class = SignupForm


    def form_valid (self, form) :
        if form.is_valid() :
            user = form.save()
            auth_login(self.request,user=user)
            return redirect('home')



class delete (RedirectView) :
    def get (self, request,id) :
        user = request.user
        Todo.delete_action(user,id)
        return redirect('home')

class edit (View) :
    def get (self,request,id) :
        self.user = request.user
        self.todo = Todo.objects.get(id=id,user=self.user)
        return render(request,'edit.html',{'action':self.todo})

    def post (self,request,id) :
        text = request.POST['text']
        todo = Todo.objects.get(id=id,user=request.user)
        todo.text = text
        todo.save()
        return redirect('home')