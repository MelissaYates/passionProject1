from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from urllib3.util import request

from .forms import UserForm, ExistingUserForm, RelatedCourseForm, CourseForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Subject, Course, RelatedCourse, Module, Content, ItemBase, Chat

# Create your views here.
#  the index view is the main page that the user sees with all of the entries
def index(request):
    context = {
        'item': Course.objects.all()
    }
    return render(request, "eLearningApp/index.html", context)

def landing(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # print(request.POST)
            form = CourseForm(request.POST)
            if form.is_valid():
                tempFile = request.FILES
                # print('if 1')
            if not tempFile:
                tempFile = ''
                # print('if 2')
            else:
                print('else made it')
                tempFile = tempFile['thumbnail']
            entry = Course(title=request.POST['title'], info=request.POST['info'], docFile=tempFile,
                           foreignKey=request.user)
            entry.save()
            return redirect('landing')
        image_list = Course.objects.all()
        myEntries = Course.objects.filter(owner=request.user)
        context = {
            'form': CourseForm,
            'myEntries': myEntries,
        }
        return render(request, 'eLearningApp/landing.html', context)

def edit(request, pkToEdit):
    item = get_object_or_404(Course, pk=pkToEdit)
    form = CourseForm(request.POST or None, instance=item)
    currentUser = request.user
    userForeignKey = Course.objects.get(pk=pkToEdit)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'item': item,
        'form': form,
        'userForeignKey': userForeignKey.foreignKey.username,
        'currentUser': currentUser,
        'usersPost': Course.objects.all(),
    }
    return render(request, 'eLearningApp/edit.html', context)


def delete(request, pkToDelete):
    item = get_object_or_404(Course, pk=pkToDelete)
    item.delete()
    return redirect('landing')


def logIn(request):
    if request.method == 'POST':
        returnUser = authenticate(username=request.POST['username'], password=request.POST['password'])
        if returnUser is not None:
            login(request, returnUser)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password Incorrect, Please try again.')
            return redirect('logIn')
    context = {
        'form': ExistingUserForm
    }
    return render(request, "eLearningApp/logIn.html", context)


def logOut(request):
    logout(request)
    return redirect('index')


def signUp(request):
    if request.method == 'POST':
        newUser = UserForm(request.POST or None)
        if newUser.is_valid():
            loggedInUser = User.objects.create_user(username=request.POST['username'], email='',
                                                    password=request.POST['password'])
            login(request, loggedInUser)
            return redirect('index')
        else:
            messages.error(request, "This user exists, new user name needed!")
            return redirect('signUp')
    else:
        context = {
            'form': UserForm(),

        }
        return render(request, 'eLearningApp/signUp.html', context)

def related_course(request, pkToRelated):
    item = Course.objects.get(pk=pkToRelated)
    if request.method == "POST":
        form = RelatedCourseForm(request.POST)
        if form.is_valid():
            tempFiles = request.FILES
            if not tempFiles:
                tempFiles = ''
            else:
                tempFiles = tempFiles["image"]
            related = RelatedCourse(entryName=request.POST['entryName'], entryInfo=request.POST['entryInfo'], image=tempFiles, relatedKey=item)
            related.save()
        return redirect("landing")
    else:
        context = {
            'form': RelatedCourseForm()
        }
    return render(request, 'eLearningApp/related_course.html', context)

def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
    context = {
        'list': Course.objects.filter(entryName__contains=query)}
    return render(request, 'eLearningApp/search.html', context)


def display(request, pkToShow):
    item = Course.objects.get(pk=pkToShow)
    displayInfo = {
        'item': item,
    }
    return render(request, 'eLearningApp/display.html', displayInfo)


