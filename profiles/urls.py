from django.urls import include, path

from . import views


app_name = 'profiles'

urlpatterns = [
    path('<str:username>/', views.profile_detail, name='detail'),
    path('create/', views.profile_create(), name='create'),
    path('<str:username>/edit/', views.profile_update, name='update'),

]
