from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, AuthorizationForm, EditProfile
from django.contrib.auth.hashers import make_password, check_password
from .models import CustomUser, UserProfile, Group
from posts.models import Post
from django.utils.timezone import now
# Create your views here.

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('user_id', None):
            return func(request, *args, **kwargs)
        return redirect('/login/')
    return wrapper



def main(request):
    if request.method == 'GET':
        posts_list = reversed(Post.objects.all())
        user_id = request.session.get('user_id', None)
        if user_id:
            user = CustomUser.objects.get(pk=user_id)
            profile = UserProfile.objects.get(user=user)
            return render(request, 'users/main.html', {'user_id': user_id, 'posts': posts_list, 'profile': profile})
        return render(request, 'users/main.html', {'user_id': user_id, 'posts': posts_list})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = make_password(form.cleaned_data['password'])
            if not CustomUser.objects.filter(login=login).exists():
                group = Group.objects.get(id=1)
                new_user = CustomUser(login=login, password=password, group=group)
                new_user.save()
                UserProfile(user=new_user, name=new_user.login).save()
                return redirect('/login')
            else:
                return render(request, 'users/register.html', {'form': form, 'failure': 1})
        return render(request, 'users/register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            if not remember_me:
                request.session.set_expiry(0)

            if CustomUser.objects.filter(login=login).exists():
                user = CustomUser.objects.get(login=login)
                user.last_login = now()
                user.save()
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    return redirect('/')

            return render(request, 'users/login.html', {'form': form, 'failure': 1})

    else:
        form = AuthorizationForm()
        return render(request, 'users/login.html', {'form': form})


def profile(request, pk):
    if request.method == 'GET':
        user_id = request.session.get('user_id', None)
        if user_id:
            user = CustomUser.objects.get(pk=request.session['user_id'])
            profile = UserProfile.objects.get(user=user)
            if profile.pk == pk:
                return render(request, 'users/profile.html', {'profile': profile})
        user = CustomUser.objects.get(pk=pk)
        profile = UserProfile.objects.get(user=user)
        return render(request, 'users/profile.html', {'profile': profile, 'to_show': 1})

@login_required
def profile_settings(request):
    user = CustomUser.objects.get(pk=request.session['user_id'])
    profile = UserProfile.objects.get(user=user)
    data = {'name': profile.name, 'email': profile.email, 'photo': profile.photo}
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, initial=data)
        if form.is_valid():
            if not form.cleaned_data['password'] == '':
                password = make_password(form.cleaned_data['password'])
                user.password = password
            filter_profile = UserProfile.objects.filter(email=form.cleaned_data['email'])
            if filter_profile.exists() and filter_profile[0].user != CustomUser.objects.get(pk=request.session['user_id']):
                return render(request, 'users/profile_settings.html', {'form': form, 'failure': 1})
            saved_form = form.save(commit=False)
            user.save()
            saved_form.user = user
            saved_form.save()
            return render(request, 'users/profile_settings.html', {'form': form, 'pk': profile.pk, 'success': 1})

        return HttpResponse('wtf')
    else:
        form = EditProfile(initial=data)
        return render(request, 'users/profile_settings.html', {'form': form, 'pk': profile.pk})


def profile_posts(request, pk):
    if request.method == 'GET':
        user_id = request.session.get('user_id', None)
        if user_id:
            user = CustomUser.objects.get(pk=request.session['user_id'])
            profile = UserProfile.objects.get(user=user)
            if profile.pk == pk:
                posts = Post.objects.filter(author=profile)
                return render(request, 'users/users_posts.html', {'posts': posts, 'profile': profile,
                                                                  'pk': pk, 'user_id': user_id})

        user = CustomUser.objects.get(pk=pk)
        profile = UserProfile.objects.get(user=user)
        posts = Post.objects.filter(author=profile)
        if len(posts) == 0:
            return render(request, 'users/users_posts.html', {'posts': posts, 'profile': profile, 'pk': user_id})
        return render(request, 'users/users_posts.html', {'posts': posts, 'profile': profile, 'pk': pk})



@login_required
def logout(request):
    del request.session['user_id']
    return redirect('/')
