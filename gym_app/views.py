"""from django.shortcuts import render

def dashboard(request):
    return render(request, 'gym_app/dashboard.html')

def members(request):
    return render(request, 'gym_app/member_list.html')

def plans(request):
    return render(request, 'gym_app/plans.html')

def trainers(request):
    return render(request, 'gym_app/trainers.html')

def payments(request):
    return render(request, 'gym_app/payments.html')
"""

from django.shortcuts import render, redirect
from .models import Member

def dashboard(request):
    return render(request, 'gym_app/dashboard.html')

def members(request):
    members = Member.objects.all()
    return render(request, 'gym_app/member_list.html', {'members': members})

# ---- TEMP CRUD VIEWS (placeholder) ----

def member_add(request):
    return render(request, 'gym_app/member_add.html')

def member_edit(request, id):
    return render(request, 'gym_app/member_edit.html')

def member_delete(request, id):
    return redirect('members')

def plans(request):
    return render(request, 'gym_app/plan_list.html')

def trainers(request):
    return render(request, 'gym_app/trainer_list.html')

def payments(request):
    return render(request, 'gym_app/payment_list.html')


