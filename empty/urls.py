from operator import index
from typing import List
from django.contrib import admin
from django.urls import path
from empty.views import index, create, List, reviews, createreviews
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name = 'index'),
    path('index', index, name = 'index'),
    path('create', create, name = "create"),
    path('list', login_required(List.as_view()), name = "list"),
    path('reviews', reviews, name="reviews"),
    path('createreviews', createreviews, name="createreviews"),
]

