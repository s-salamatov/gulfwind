from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Profile


def profile_required(view):
    @login_required
    def wrapper(request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            return redirect('profiles:create')
        return view(request, *args, **kwargs)
    return wrapper