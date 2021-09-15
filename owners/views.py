# Create your views here.
import json

from django.http    import JsonResponse
from django.views   import View

from owners.models    import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name = data['name'],
            age = data['age'],
            email = data['email']
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        result = []

        for owner in owners:
            dogs = owner.dogs_set.all()
            dog_list = []

            for dog in dogs:
                dog_info = (
                    {
                        'name' : dog.name,
                        'age' : dog.age,
                    }
                )
                dog_list.append(dog_info)

            result.append(
                {
                'name' : owner.name,
                'age' : owner.age,
                'email' : owner.email,
                'dog' : dog_list
                }
            )
        return JsonResponse({'result' : result}, status=200)
            


class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)

        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner_id = data['owner_id']
        )

        return JsonResponse({'MESSAGE' : 'CREATED'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        result = []

        for dog in dogs:
            result.append(
                {
                    'name':dog.name,
                    'age':dog.age,
                    'owner':dog.owner.name
                }
            )
        return JsonResponse({'result':result}, status=200)


        