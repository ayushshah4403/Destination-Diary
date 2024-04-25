from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def destinations(request):
    if request.method == "POST":        
        data = request.POST
        destination_name  = data.get('destination_name')
        destination_description  = data.get('destination_description')
        destination_image = request.FILES.get('destination_image')
        
        Destination.objects.create(
            destination_name = destination_name,
            destination_description = destination_description,
            destination_image = destination_image
        )
        
        return redirect('/')
    query_set = Destination.objects.all()
    context = {'destinations' : query_set}
    
    return render(request, 'home.html', context)


def update_destination(request, id):
    queryset = Destination.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        destination_name  = data.get('destination_name')
        destination_description  = data.get('destination_description')
        destination_image = request.FILES.get('destination_image')
        queryset.destination_name = destination_name
        queryset.destination_description =  destination_description
        
        if destination_image:
            queryset.destination_image = destination_image
        
        queryset.save()
        return redirect('/')
    context = {'destination' : queryset}
    return render(request, "update_destination.html", context)


def delete_destination(request, id):
    query_set = Destination.objects.get(id = id)
    query_set.delete()
    return redirect('/')