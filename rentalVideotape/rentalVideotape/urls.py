"""rentalVideotape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from rentalApp import views


urlpatterns = [
    path('', views.index),
    path('createRental/', views.createRental),
    path('editRental<int:id>/', views.editRental),
    path('displayGenre/', views.displayGenre),
    path('displayDirector/', views.displayDirector),
    path('displayStatus/', views.displayStatus),
    path('displayVideotape/', views.displayVideoTape),
    path('displayGenre/createGenre/', views.createGenre),
    path('displayDirector/createDirector/', views.createDirector),
    path('displayStatus/createStatus/', views.createStatus),
    path('displayVideotape/createVideotape/', views.createVideoTape),
    path('displayGenre/editGenre<int:id>/', views.editGenre),
    path('displayDirector/editDirector<int:id>/', views.editDirector),
    path('displayStatus/editStatus<int:id>/', views.editStatus),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
