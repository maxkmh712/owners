from django.shortcuts import render

# Create your views here.
import json

from django.http    import JsonResponse
from django.views   import View

from owners.models    import Owner

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        Owner.objects.create(
            name = data['name'],
            age = data['age'],
            email = data['email']
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)