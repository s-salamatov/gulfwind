from django.http import Http404, HttpResponseForbidden
from django.shortcuts import redirect, render

from authentication.models import User
from profiles.decorators import profile_required
from profiles.forms import CreateProfileForm
from profiles.models import Profile


@profile_required
def profile_detail(request, username):
    try:
        user = User.active_users('get', username=username)
        if user != request.user:
            return HttpResponseForbidden('Вы не можете редактировать профиль другого пользователя')
    except User.DoesNotExist:
        raise Http404('Такого аккаунта не существует. Возможно он был заблокирован или удален')
    return render(request, 'profiles/profile_common.html', {'user': user})


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid:
            obj = form.save(commit=False)
            print(request.FILES)
            if 'image' in request.FILES:
                obj.image = request.FILES['image']
            obj.user = request.user
            obj.save()
            print(obj, obj.image)
            return redirect(obj.get_absolute_url())
    return render(request, 'profiles/profile_create.html', {'form': form})


def profile_update(request, username):
    try:
        profile = Profile.objects.get(user__is_active=True, user__username=username)
        print(profile.user, request.user)
        if profile.user != request.user:
            return HttpResponseForbidden('Вы не можете редактировать профиль другого пользователя')
    except Profile.DoesNotExist:
        return Http404('Такого профиля не существует')
    if request.method == 'GET':
        form = CreateProfileForm(instance=profile)
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            obj = form.save(commit=False)
            print(request.FILES)
            if 'image' in request.FILES:
                obj.image = request.FILES['image']
            obj.save()
            print(obj, obj.image)
            return redirect(obj.get_absolute_url())
    return render(request, 'profiles/profile_update.html', {'form': form})


@profile_required
def profile_settings(request):
    try:
        user = User.active_users('get', username=request.user.username)
    except User.DoesNotExist:
        raise Http404('Такого аккаунта не существует. Возможно он был заблокирован или удален')
    return render(request, 'profiles/profile_detail.html', {'user': user})