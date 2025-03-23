from django.shortcuts import render
def homeview(request):
    return render(request,'testapp/home.html')
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Student
class allstudentslistview(ListView):
    model = Student
def pythonview(request):
    python_students = Student.objects.filter(subject='python')
    return render(request,'testapp/python.html',{'students':python_students})

def djangoview(request):
    django_students = Student.objects.filter(subject='django')
    return render(request,'testapp/python.html',{'students':django_students})
from django.contrib.auth.mixins import LoginRequiredMixin
class adminlistview(LoginRequiredMixin,ListView):
    model = Student
    template_name = 'testapp/students.html'
    context_object_name = 'students'
from django.urls import reverse_lazy
class admincreateview(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('adminstudents')
class adminupdateview(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('adminstudents')
class admindeleteview(DeleteView):
    model = Student
    success_url = reverse_lazy('adminstudents')
from django.contrib.auth import logout
from django.shortcuts import redirect
def logoutview(request):
    logout(request)
    return redirect('/')

from testapp.forms import signupform
from django.http import HttpResponseRedirect
def signupview(request):
    form = signupform()
    if request.method == 'POST':
        form = signupform(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})