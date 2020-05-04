from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ParticipantInfo
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def registration(request):
    return render(request, 'registration.html')


# Image save as a file, needs a file manager.
def registration_success(request):
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        PhNo_r = request.POST.get('phone')
        USN_r = request.POST.get('usn')
        DOB_r = request.POST.get('dob')
        Sem_r = request.POST.get('sem')
        Image_r = request.FILES.get('image')

        Event1_r = request.POST.get('event1')
        if Event1_r:
            Event1_r = True
        else:
            Event1_r = False
        Event2_r = request.POST.get('event2')
        if Event2_r:
            Event2_r = True
        else:
            Event2_r = False
        Event3_r = request.POST.get('event3')
        if Event3_r:
            Event3_r = True
        else:
            Event3_r = False
        Event4_r = request.POST.get('event4')
        if Event4_r:
            Event4_r = True
        else:
            Event4_r = False
        Event5_r = request.POST.get('event5')
        if Event5_r:
            Event5_r = True
        else:
            Event5_r = False
        Event6_r = request.POST.get('event6')
        if Event6_r:
            Event6_r = True
        else:
            Event6_r = False
        Event7_r = request.POST.get('event7')
        if Event7_r:
            Event7_r = True
        else:
            Event7_r = False
        Event8_r = request.POST.get('event8')
        if Event8_r:
            Event8_r = True
        else:
            Event8_r = False
        Event9_r = request.POST.get('event9')
        if Event9_r:
            Event9_r = True
        else:
            Event9_r = False
        Event10_r = request.POST.get('event10')
        if Event10_r:
            Event10_r = True
        else:
            Event10_r = False
        Event11_r = request.POST.get('event11')
        if Event11_r:
            Event11_r = True
        else:
            Event11_r = False
        Event12_r = request.POST.get('event12')
        if Event12_r:
            Event12_r = True
        else:
            Event12_r = False
        Event13_r = request.POST.get('event13')
        if Event13_r:
            Event13_r = True
        else:
            Event13_r = False
        Event14_r = request.POST.get('event14')
        if Event14_r:
            Event14_r = True
        else:
            Event14_r = False
        Event15_r = request.POST.get('event15')
        if Event15_r:
            Event15_r = True
        else:
            Event15_r = False

        to_save = ParticipantInfo(ParticipantName=name_r, ParticipantEmail=email_r, ParticipantPhNo=PhNo_r,
                                  ParticipantUSN=USN_r, ParticipantDOB=DOB_r, ParticipantSem=Sem_r,
                                  ParticipantImage=Image_r, Event1=Event1_r, Event2=Event2_r, Event3=Event3_r,
                                  Event4=Event4_r, Event5=Event5_r, Event6=Event6_r, Event7=Event7_r, Event8=Event8_r,
                                  Event9=Event9_r, Event10=Event10_r, Event11=Event11_r, Event12=Event12_r,
                                  Event13=Event13_r,
                                  Event14=Event14_r, Event15=Event15_r
                                  )

        to_save.save()

        return HttpResponse('<h1>Registration Success.</h1>')

    else:
        return HttpResponse('<h1>Registration Failure.</h1>')


# Use objects.filter() to list accordingly.
# Count method counts all objects in database, use filter(attributes).count() to count objects accordingly.

@login_required(login_url='admin_login')
def view_participants(request):
    objects = ParticipantInfo.objects.all()
    count = objects.count()
    context = {
        'objects': objects,
        'count': count,
    }
    return render(request, 'branch_admin.html', context)


# Using pk as reference to delete Info

@login_required(login_url='admin_login')
def delete(request, pk):
    info = ParticipantInfo.objects.get(id=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('branch_admin')

    context = {'name': info}
    return render(request, 'delete.html', context)


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('branch_admin')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('branch_admin')
            else:
                messages.info(request, 'Username or Password is Incorrect.')

        context = {}
        return render(request, 'admin_login.html', context)


def admin_logout(request):
    logout(request)
    return redirect('admin_login')