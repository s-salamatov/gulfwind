from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path('', include('allauth.urls')),
    path('account/', include('profiles.urls', namespace='profiles')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
