from django.shortcuts import render, redirect
from home.forms import RegisterForm
from django.contrib import messages
from home.backEnd import FaceRecognition
from home.models import UserProfile
from datetime import datetime

facerecognition = FaceRecognition()

def home(request):
    return render(request, 'home/home.html')

def register(request):
    t1 = datetime.now()
    if request.POST:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully Registerd!')
            addFace(request.POST['face_id'])
            t2 = datetime.now()
            delta = t2 - t1
            # time difference in seconds
            print(f"Register: Time difference is {delta.total_seconds()} seconds")
            # time difference in milliseconds
            ms = delta.total_seconds() * 1000
            print(f"Register: Time difference is {ms} milliseconds")
            return redirect('/')
        else:
            messages.error(request, "Account Register Failed!")

    form = RegisterForm()
    context = {
        'title' : 'Register Form',
        'form' : form
    }
    t2 = datetime.now()
    delta = t2 - t1
    # time difference in seconds
    print(f"Register2: Time difference is {delta.total_seconds()} seconds")
    # time difference in milliseconds
    ms = delta.total_seconds() * 1000
    print(f"Register2: Time difference is {ms} milliseconds")
    return render(request, 'home/register.html', context)

def addFace(face_id):
    face_id = face_id
    facerecognition.faceDetect(face_id)
    facerecognition.trainFace()
    return redirect('/')


def login(request):
    t1 = datetime.now()

    face_id = facerecognition.recognizeFace()
    t2 = datetime.now()
    delta = t2 - t1
    # time difference in seconds
    print(f"Login: Time difference is {delta.total_seconds()} seconds")
    # time difference in milliseconds
    ms = delta.total_seconds() * 1000
    print(f"Login: Time difference is {ms} milliseconds")

    print("face id predicted :: " , face_id)
    if(face_id == -1):
        return render(request, 'home/home.html')
    return redirect('/home/welcome/'+ str(face_id))

def welcome(request, face_id):
    face_id = int(face_id)
    print(face_id)
    if(face_id == -1):
        return render(request, 'home/home.html')
    # data = {
    #     'user': UserProfile.objects.get(face_id= face_id)
    # }
    

    return render(request, 'home/profile.html')
    # return render(request, 'home/profile.html', data)
    