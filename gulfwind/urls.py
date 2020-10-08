from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # path('', include('authentication.urls', namespace='auth')),
    # path('account/profile/', include('profiles.urls', namespace='profile')),

    path('admin/', admin.site.urls),
]
