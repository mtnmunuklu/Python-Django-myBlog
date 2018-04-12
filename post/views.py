from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponsePermanentRedirect,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
def post_index(request):
    posts = Post.objects.all()
    return render(request,'post/index.html',{'posts': posts})

def post_detail(request,id):
    post=get_object_or_404(Post, id=id)
    context = {
        'post':post,
    }
    return render(request,'post/detail.html', context)

def post_create(request):

    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        messages.success(request, "You have successfully created")
        return HttpResponsePermanentRedirect(post.get_absolute_url())

    context = {
            'form': form
        }

    return render(request, 'post/form.html', context)

def post_update(request,id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "You have successfully created",  extra_tags="mesaj-basarili")
        return HttpResponsePermanentRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'post/form.html', context)

def post_delete(request,id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("post:index")