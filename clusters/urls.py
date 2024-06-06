from django.urls import path
from .views import cluster_view

urlpatterns = [
    path('cluster/', cluster_view, name='cluster-view'),
]
