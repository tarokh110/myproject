from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect , get_object_or_404
from accounts.forms import Newuser
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import Newuser
from django.contrib.auth.decorators import  login_required
from .models import Post

# Create your views here.

def log_in(request):
    if request.method == 'POST':
        form = Newuser(request.POST)
        if form.is_valid():
          #  cd = form.cleaned_data
          #  user = authenticate(last_name=cd['last_name'],
          #                      password=cd['password'])
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            user = authenticate(last_name=last_name, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('successful')
                else:
                    return HttpResponse('login disabled')
            else:
                return HttpResponse('invalid login')
        else:
            return HttpResponse('invalid form')
    else:
        form = Newuser()
    return render(request, 'registration/../templates/accounts/login.html', {'form': form})





def signUp(request):
    form = Newuser()

    if request.method == 'POST':
        form = Newuser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('dashboard')
        else:
            print('error')
    return render(request, 'acounts/signUp.html', {'form': form})


def register3(request):
    form = Newuser()

    if request.method == 'POST':
        form = Newuser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('dashboard')
        else:
            print('error')
    return render(request, 'acounts/signUp.html', {'form': form})

@login_required(login_url='django.contrib.auth.login')
def profile(request):
    return render(request, "accounts/profile.html",{'section':'profile'})


def post_list(request):
    posts =  Post.published.all()

    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id ):
    post = get_object_or_404(Post, id= id )

    return render(request,
                'blog/post/detail.html', {'post':post})





#"""return render(request, 'accounts/login.html')"""





