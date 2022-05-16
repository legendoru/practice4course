from operator import index
from typing import List
from django.contrib import admin
from django.urls import path
from empty.views import index, create, List
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name = 'index'),
    path('create', create, name = "create"),
    path('list', login_required(List.as_view()), name = "list"),
]

