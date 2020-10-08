from django.urls import include, path


urlpatterns = [
    path('', include('allauth.urls')),
    path('account/', include('profiles.urls', namespace='profiles')),
]
