from django.shortcuts import render, redirect, HttpResponse, get_list_or_404
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse
from .forms import CreateFullPostForm, CreateCommentForm
from .models import Post, ImagesForPost, Comment
from users.models import CustomUser, UserProfile
from users.views import login_required
from django.views import View
# Create your views here.


class show(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        user_id = request.session.get('user_id', None)
        comments = reversed(post.comment_set.all())
        form = CreateCommentForm()
        if user_id:
            user = CustomUser.objects.get(pk = user_id)
            profile = UserProfile.objects.get(user=user)
            return render(request, 'posts/post.html', {'post': post, 'profile': profile, 'form': form,
                                                       'comments': comments, 'user_id': user_id})

        return render(request, 'posts/post.html', {'post': post, 'form': form, 'comments': comments})


@login_required
def create(request):
    user_id = request.session['user_id']
    user = CustomUser.objects.get(pk=user_id)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = CreateFullPostForm(request.POST, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            user.posts_written += 1
            saved_form = form.save(commit=False)
            saved_form.author = profile
            user.save()
            saved_form.save()
            for f in files:
                ImagesForPost(post=saved_form, image=f).save()
            return redirect(reverse('post', kwargs={'pk': saved_form.id}))

    else:
        form = CreateFullPostForm()
        return render(request, 'posts/create_post.html', {'form': form, 'profile': profile, 'user_id': user_id})


@login_required
def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    data = {'author': post.author, 'title': post.title,
            'body': post.body, 'images': post.imagesforpost_set.all}
    if request.method == 'POST':
        form = CreateFullPostForm(request.POST, request.FILES or None, initial=data, instance=post)
        files = request.FILES.getlist('images')
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.author = post.author
            saved_form.save()
            for f in files:
                ImagesForPost(post=saved_form, image=f).save()
            return render(request, 'posts/update_post.html', {'form': form, 'pk': post.pk, 'success': 1})
    else:
        form = CreateFullPostForm(initial=data)
        return render(request, 'posts/update_post.html', {'form': form, 'pk': post.pk})

@login_required
def delete_post(request, pk):
    if request.method == 'GET':
        author = Post.objects.get(id=pk).author
        Post.objects.get(id=pk).delete()
        return redirect(reverse('profile_posts', kwargs={'pk': author.pk}))


def create_comment(request, pk):
    if request.is_ajax and request.method == 'POST':
        form = CreateCommentForm(request.POST)
        user = request.session['user_id']
        profile = UserProfile.objects.get(user=user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = profile
            instance.post = Post.objects.get(pk=pk)
            instance.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({'instance': ser_instance}, status=200)

        return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": ""}, status=400)