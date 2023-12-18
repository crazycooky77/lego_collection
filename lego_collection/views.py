from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello, World!')


class CreateUser(CreateView):
    model = CustomUser
    fields = ['username', 'email', 'privacy', 'password']
    template_name = 'create_user.html'
    success_url = reverse_lazy('user_list')


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})
