from django.http import JsonResponse
from .models import ClusterDetails
from django.http import HttpResponse


def cluster_view(request):
    clusters = ClusterDetails.objects.all().values()
    clusters_list = list(clusters)  # Convert queryset to list
    return JsonResponse(clusters_list, safe=False)


def home_view(request):
    return HttpResponse("Welcome to the Cluster Data API. Visit /cluster to see the cluster data.")
