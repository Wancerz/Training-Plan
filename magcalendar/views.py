from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View
from time import time
from django.http import JsonResponse
from magcalendar.models import Exercises, Calendar_exercises
from django.core import serializers
from datetime import datetime
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

def Main(request):

    return render(request, 'main.html')

def HomePageSite(request):

    return render(request, 'HomePage.html')

@login_required(login_url='LoginSite')
def CalendarSite(request):

    return render(request, 'calendar.html')

def get_data(request):
    text = request.GET.get('button_text')

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        queryset = Calendar_exercises.objects.all()
        queryset = serializers.serialize('json',queryset)

        return JsonResponse({'queryset':queryset})

    return render(request,'calendar.html' )

def show_day_calendar(request):
    date = request.GET.get('date')
    date = date[4:]
    date = datetime.strptime(date,"%b %d %Y").date()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
  
        queryset = Calendar_exercises.objects.filter(created_at=date).filter(id_User_id=request.user.id).select_related('id_Exercises').values('note','repeats','id_Exercises__title' )
        queryset = json.dumps(list(queryset))

        return JsonResponse({'queryset':queryset})

    return render(request,'calendar.html' )


#coś pomieszałem tutaj i jako repeats wysyła się z fronute note i vice versa
def delete_row(request):
     
     exercise = request.GET.get('exercise')
     repeats = request.GET.get('repeats')
     note = request.GET.get('note')
     date = request.GET.get('date')
     date = date[4:]
     date = datetime.strptime(date,"%b %d %Y").date()

     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = Calendar_exercises.objects.filter(created_at=date, note=note, repeats=repeats, id_Exercises__title=exercise, id_User_id=request.user.id)[0]
        queryset.delete()

     return render(request,'calendar.html' )
    

def add_values_to_options(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        queryset = Exercises.objects.values('title')
        queryset = json.dumps(list(queryset)) 
        print(queryset)
        return JsonResponse({'queryset':queryset})

    return render(request,'calendar.html')


def add_exercise_to_db(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        exercise = request.GET.get('exerc')
        note = request.GET.get('not')
        rep = request.GET.get('rep')
        date = request.GET.get('currentDate')
        date = date[4:]
        date = datetime.strptime(date,"%b %d %Y").date()
        exercise = Exercises.objects.get(title=exercise)
        queryset = Calendar_exercises(note=note, repeats=rep, id_Exercises=exercise, id_User_id = request.user.id, created_at=date)
        queryset.save()
    return render(request,'calendar.html')


@login_required(login_url='LoginSite')
def log_calendar(request):

    queryset = Calendar_exercises.objects.filter(id_User_id=request.user.id).select_related('id_Exercises').values('note','repeats','id_Exercises__title','created_at' ).order_by('-created_at')
    return render(request,'logs.html',{"queryset":queryset})



def info_site(request):


    return render(request,'info.html')









