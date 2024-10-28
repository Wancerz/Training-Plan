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
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect

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
        option = request.GET.get('ButSelect')
        if option == '0':
            queryset = Calendar_exercises.objects.filter(created_at=date).filter(id_User_id=request.user.id).select_related('id_Exercises').values('note','repeats','id_Exercises__title', 'id_Exercises' )
        else:
            queryset = Calendar_exercises.objects.filter(created_at=date).filter(id_User_id=request.user.id).select_related('id_Exercises').values('note','repeats','id_Exercises__title_polish', 'id_Exercises' )        
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
        option = request.GET.get('ButSelect')
        if option == '0':
            queryset = Exercises.objects.values('title')
        else:
            queryset = Exercises.objects.values('title_polish')
        queryset = json.dumps(list(queryset)) 
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
        option = request.GET.get('ButSelect')
        if option == '0':
            exercise = Exercises.objects.get(title=exercise)
        else:
            exercise = Exercises.objects.get(title_polish=exercise)



        queryset = Calendar_exercises(note=note, repeats=rep, id_Exercises=exercise, id_User_id = request.user.id, created_at=date)
        queryset.save()



    return render(request,'calendar.html')


@login_required(login_url='LoginSite')
def log_calendar(request):

    queryset = Calendar_exercises.objects.filter(id_User_id=request.user.id).select_related('id_Exercises').values('note','repeats','id_Exercises__title','created_at' ).order_by('-created_at')


    return render(request,'logs.html',{"queryset":queryset})



def info_site(request):

    return render(request,'info.html')


# def add_exercise_site(request):

#     return render(request,'add_exercise.html')






def add_exercise_site(request):

    show_my_exercises = Exercises.objects.filter(User_id=request.user.id).values('id','title','title_polish')
    to_delete = request.GET.get("to_delete")
    
    print(to_delete)

    # if 'my_file' in request.FILES:
    #     myfile = request.FILES['my_file']
    #     # do something with the file
    # else:
    #     return render(request, 'add_exercise.html',{"show_my_exercises":show_my_exercises})

    try:
        if request.method == 'POST' and request.FILES['myfile'] :
            myfile = request.FILES['myfile']
            english_title = request.POST.get('english_title')
            polish_title = request.POST.get('polish_title')
            print(english_title)
            fs = FileSystemStorage(location='magcalendar/static/pictures/')
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print(myfile.name)


            queryset = Exercises(title=english_title, title_polish=polish_title, User_id = request.user.id, photo_url=myfile.name)
            queryset.save()



            return render(request, 'add_exercise.html', {
                'uploaded_file_url': uploaded_file_url,
                "show_my_exercises":show_my_exercises
            })
    except:
        return render(request, 'add_exercise.html',{"show_my_exercises":show_my_exercises})


    if to_delete is not None:
        
        query = Exercises.objects.get(id=to_delete, User_id = request.user.id)

        query.delete()
        return redirect("AddExerciseSite")



        
    return render(request, 'add_exercise.html',{"show_my_exercises":show_my_exercises})


# def add_exercise_site_delete(request):

#     show_my_exercises = Exercises.objects.filter(User_id=request.user.id).values('id','title','title_polish')


#     to_delete = request.GET.get("to_delete")
#     print(to_delete+"AA")
#     if to_delete is not None:
#         query = Exercises.object.filter(id=to_delete).filter(User_id=request.user.id)
#         query.delete



#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         english_title = request.POST.get('english_title')
#         polish_title = request.POST.get('polish_title')
#         print(english_title)
#         fs = FileSystemStorage(location='magcalendar/static/pictures/')
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         print(myfile.name)


#         queryset = Exercises(title=english_title, title_polish=polish_title, User_id = request.user.id, photo_url=myfile.name)
#         queryset.save()



#         return render(request, 'add_exercise.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'add_exercise.html',{"show_my_exercises":show_my_exercises})





def url_of_photo(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        url = request.GET.get('selectedValue')
        option = request.GET.get('ButSelect')
        print(option)

        if option == '0':
            queryset = Exercises.objects.filter(title=url).values('photo_url').first()
        else:
            queryset = Exercises.objects.filter(title_polish=url).values('photo_url').first()

        print(queryset)


        queryset = json.dumps(queryset) 
        return JsonResponse({'queryset':queryset})

    return render(request,'calendar.html')





def info_row(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        info = request.GET.get('ButtonValue')
        print(info)
        queryset = Exercises.objects.filter(id=info).values('video_url', 'note').first()


        string_value = """"""

        # for query in queryset:
        #     print(query.video_url)
        queryset = json.dumps(queryset)
        return JsonResponse({'queryset':queryset})


    return render(request,'calendar.html')







