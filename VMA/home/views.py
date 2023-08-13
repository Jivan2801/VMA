from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='/log_in')
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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/log_in/')
        
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/log_in/')
        else:
            login(request, user)
            return redirect('/add-vehicle/')

    return render(request, "index.html")

def log_out(request):
    logout(request)
    return redirect('/log_in/')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, 'Username already taken')
            return redirect('/register/')
            

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()

        messages.success(request , 'Account created sucessfully')

        return redirect('/register/')
    
    return render(request, "register.html")


def delete_vehicle(request, id):
    queryset = Vehicle.objects.get(id=id)
   
    queryset.delete()
    return redirect('/add-vehicle/')


def update_vehicle(request , id):
    queryset = Vehicle.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        Vehicle_no = data.get('Vehicle_no')
        Vehicle_type = data.get('Vehicle_type')
        Vehicle_model = data.get('Vehicle_model')
        Vehicle_des = data.get('Vehicle_des')

        queryset.Vehicle_no = Vehicle_no
        queryset.Vehicle_type = Vehicle_type
        queryset.Vehicle_model = Vehicle_model
        queryset.Vehicle_des = Vehicle_des

        queryset.save()
        return redirect('/add-vehicle/')

    context={'vehicle': queryset}
    return render(request, 'update_vehicle.html' , context)

