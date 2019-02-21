from django.shortcuts import render
from django.http import HttpResponse
from .models import Mother, Child


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#grabs all moms
def mothers(request):
    parents = Mother.objects.all()
    for x in parents:
    print(f'{x. mother_first_name}')
    for y in Child.objects.\
            filter(child_mom__ mother_first_name=x. mother_first_name):
    return HttpResponse(y.child_name)

def children(request):
    return HttpResponse("")