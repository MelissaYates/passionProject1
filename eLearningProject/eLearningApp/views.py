from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ExistingUserForm, RelatedCourseForm, CourseForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Subject, Course, RelatedCourse, Module, Content, ItemBase

# Create your views here.
#  the index view is the main page that the user sees with all of the entries
def index(request):
    context = {
        'item': Course.objects.all()
    }
    return render(request, "eLearningApp/index.html", context)

def dashboard(request):
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
            return redirect('dashboard')
        image_list = Course.objects.all()
        myEntries = Course.objects.filter(owner=request.user, created_date_lte=timezone.now()).order_by('-created_date')
        context = {
            'form': CourseForm,
            'myEntries': myEntries,
            'image_list': image_list,
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
    course_pk = item.post.pk
    item.delete()
    return redirect('dashboard', pk=course_pk)


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
    if request.method == "POST":
        form = RelatedCourseForm(request.POST)
        if form.is_valid():
            tempFiles = request.FILES
            if not tempFiles:
                tempFiles = ''
            else:
                tempFiles = tempFiles["image"]
                related = RelatedCourse.objects.select_related('entryName').prefetch_related('time').only(
                'entryInfo', 'created_on', 'image')
                related.save()
        return redirect("dashboard")
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


def course_detail(request, pkToShow):
    item = Course.objects.get(pk=pkToShow)
    displayInfo = {
        'item': item,
    }
    return render(request, 'eLearningApp/course_detail.html', displayInfo)


def practitioner_details(request, pkToPerson):
    person: User.objects.get(pk=pkToPerson)
    person_details = {
        'person': person,
    }
    return render(request, 'eLearningApp/person_detail.html', person_details)