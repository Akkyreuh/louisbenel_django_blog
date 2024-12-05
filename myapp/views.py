from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm

# Create your views here.

def list_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author'] 
        content = request.POST['content']
        BlogPost.objects.create(title=title, author=author, content=content)
        return redirect('list_posts')
    return render(request, 'create_post.html')



def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id)

    if request.method == 'POST':
        author = request.POST.get('author')
        if author != post.author: 
            return HttpResponseForbidden("Vous devez être auteur du post pour l'éditer")

        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', id=post.id)

    return render(request, 'edit_post.html', {'post': post})
def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('list_posts')
    return render(request, 'delete_post.html', {'post': post})

def add_comment(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        author = request.POST['author']
        text = request.POST['text']
        Comment.objects.create(post=post, author=author, text=text)
        return redirect('post_detail', id=post.id)
    return render(request, 'add_comment.html', {'post': post})

def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        author = request.POST.get('author')
        if author != comment.author:
            return HttpResponseForbidden("Vous devez être l'auteur du commentaire pour l'éditer.")

        comment.text = request.POST['text']
        comment.save()
        return redirect('post_detail', id=comment.post.id)
    return render(request, 'edit_comment.html', {'comment': comment})



def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', id=comment.post.id)
    return render(request, 'delete_comment.html', {'comment': comment})