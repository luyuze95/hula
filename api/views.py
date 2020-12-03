from django.http import JsonResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Category


class InfoView(View):
    """咨询相关接口"""

    def get(self, request, *args, **kwargs):
        data = [1, 2, 3]
        return JsonResponse(data, safe=False)


class DrfInfoView(APIView):

    def get(self, request, *args, **kwargs):
        data = [4, 5, 6]
        return Response(data)


class CategoryView(APIView):

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        category = Category()
        category.name = name
        category.save()
        return Response({
            'code': 0,
            'data': None,
            'message': 'success'
        })
