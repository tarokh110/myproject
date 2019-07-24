from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect , get_object_or_404
from accounts.forms import Newuser
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import Newuser, CommentForm
from django.contrib.auth.decorators import  login_required
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
            return redirect('account:profile')
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
    # shayd lazem bashe baraye posts tooye line pain ye var e dge tarif beshe
    paginator =  Paginator(posts, 1) #3 post in every page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts,
                                                   'page':page})


def post_detail(request, id ):
    post = get_object_or_404(Post, id= id )
    comments = post.comment_set.filter(active=True)
    Added = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            Added = new_comment

    else:
        comment_form = CommentForm()
    return render(request,
                'blog/post/detail.html', {'post':post,
                                          'comment_form': comment_form,
                                          'comments':comments ,
                                          'Added':Added})

"""
def post_share(request, post_id):
    # retrieve post by id
    post = get_object_or_404(Post, id = post_id, status= 'published' )

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post':post,
                                                    'form':form })
"""




#"""return render(request, 'accounts/login.html')"""





