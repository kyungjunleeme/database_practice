from django.shortcuts import render
from .models import Book
from django.views import View
from django.http import HttpResponse, JsonResponse


class IndexView(View):
    def get(self, request):
        b = Book.objects.get(id=2)
        b.name = 'update_fields-2'
        b.save(update_fields=['name'])
        dummy_data = {
            'name': '죠르디',
            'type': '공룡',
            'job': '편의점알바생',
            'age': 5
        }
        return JsonResponse(dummy_data)

