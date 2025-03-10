"""
URL configuration for core project.

The `urlpatterns` list.py routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("api/v1/artist/",include("urls.artist.urls")),
    path("api/v1/music/",include("urls.music.urls")),
    path("api/v1/user/",include("urls.user.urls")),
    path("api/v1/auth/",include("urls.authentication.urls")),
    path("api/v1/dashboard/",include("urls.dashboard.urls")),
    path('admin/', admin.site.urls),
]
