from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request, "index.html")


def Vechileview(request):
    vehicles = [
        {'Vehicle_no': 'MH9619', 'Vehicle_type': 'four wheelers',
            'Vehicle_model': 'Sedan', 'Vehicle_des': 'A comfortable family car.'},
        {'Vehicle_no': 'GJ8779', 'Vehicle_type': 'two wheelers',
            'Vehicle_model': 'MotorCycle', 'Vehicle_des': ' An agile and efficient bike.'},
        {'Vehicle_no': 'UP9819', 'Vehicle_type': 'three wheelers',
            'Vehicle_model': 'Auto', 'Vehicle_des': 'Basic for easy travelling.'},
        {'Vehicle_no': 'HY8520', 'Vehicle_type': 'four wheelers',
            'Vehicle_model': 'manual', 'Vehicle_des': 'hyper car for racing .'},
        {'Vehicle_no': 'KA7021', 'Vehicle_type': 'two wheelers',
            'Vehicle_model': 'manual', 'Vehicle_des': 'hyabhosda.'}
    ]

    for vehicle in vehicles:
        print(vehicle)
    return render(request, "vehicle.html", context={'vehicles': vehicles})


def add_vehicle(request):
    if request.method == "POST":

        data = request.POST
        Vehicle_no = data.get('Vehicle_no')
        Vehicle_type = data.get('Vehicle_type')
        Vehicle_model = data.get('Vehicle_model')
        Vehicle_des = data.get('Vehicle_des')

        Vehicle.objects.create(
            Vehicle_no=Vehicle_no,
            Vehicle_type=Vehicle_type,
            Vehicle_model=Vehicle_model,
            Vehicle_des=Vehicle_des,
        )
        
        return redirect('/add-vehicle')

    queryset = Vehicle.objects.all()
    context = {'vehicles': queryset}

    return render(request, "insert.html", context)


def log_in(request):
    return render(request, "index.html")


def info(request):
    return render(request, "vehicle.html")
