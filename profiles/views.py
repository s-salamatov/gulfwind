from django.http import Http404
from django.shortcuts import redirect, render

from authentication.models import User
from profiles.decorators import profile_required
from profiles.forms import CreateProfileForm


@profile_required
def profile_detail(request, username):
    try:
        user = User.active_users('get', username=username)
    except User.DoesNotExist:
        raise Http404('Такого аккаунта не существует. Возможно он был заблокирован или удален')
    return render(request, 'profiles/profile_detail.html', {'user': user})


def profile_create(request):
    print(request.method)
    if request.method == 'GET':
        form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(obj.get_absolute_url())
    return render(request, 'profiles/profile_create.html', {'form': form})


def profile_update(request):
    return None