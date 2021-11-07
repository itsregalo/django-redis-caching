from django.shortcuts import render
from django.http import JsonResponse
from api.models import Question
from .utils import Red
import time
# Create your views here.

def IndexView(request, *args, **kwargs):
    cache_data = Red.get("api")
    if cache_data:
        return JsonResponse(cache_data, safe=False)
    data = list(Question.objects.values())
    cache_data = Red.set("api", data)

    return JsonResponse(data, safe=False)