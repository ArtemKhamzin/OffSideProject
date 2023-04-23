from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout
from web.forms import RegistrationForm, AuthForm, BlogForm, BlogTagForm
from web.models import Blog, BlogTag

User = get_user_model()


def main_view(request):
    blogs = Blog.objects.all().order_by('-publication_date')
    return render(request, 'web/main.html', {
        'blogs': blogs
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request, 'web/registration.html', {
        'form': form,
        'is_success': is_success
    })


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены неверные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/auth.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main")


@login_required
def blog_edit_view(request, id=None):
    blog = get_object_or_404(Blog, user=request.user, id=id) if id is not None else None
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(data=request.POST, files=request.FILES, instance=blog, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, "web/blog_form.html", {"form": form})


@login_required
def blogs_delete_view(request, id):
    tag = get_object_or_404(Blog, user=request.user, id=id)
    tag.delete()
    return redirect('main')


@login_required
def tags_view(request):
    tags = BlogTag.objects.all()
    form = BlogTagForm()
    if request.method == 'POST':
        form = BlogTagForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags')
    return render(request, "web/tags.html", {"tags": tags, 'form': form})

@login_required
def tags_delete_view(request, id):
    tag = get_object_or_404(BlogTag, id=id)
    tag.delete()
    return redirect('tags')
