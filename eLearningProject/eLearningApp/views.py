from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

from .forms import LogInForm, UserForm, RelatedCourseForm, CourseForm
from .models import Role, Course, RelatedCourse, CourseUser
from django.contrib import messages
from taggit.models import Tag


# Create your views here.

def index(request):
    return render(request, "eLearningApp/index.html")


def dashboard(request):
    context = {
        "message": "Please Log in",
        "error": False
    }
    if request.method == "POST":
        try:
            getUser = CourseUser.objects.get(username=request.POST['username'])
            context['msg'] = getUser
        except Exception as e:
            context['message'] = "Wrong username" + str(e)
            context['error'] = True
            return render(request, 'logIn.html', context)
        if getUser.user_password == request.POST['password']:
            request.session['authenticated'] = True
            request.session['user_id'] = getUser.user_id
            request.session['user_level_id'] = getUser.user_level_id
            request.session['first_name'] = getUser.user_first_name
            return redirect('dashboard')
        else:
            context['message'] = "Wrong Password"
            context['error'] = True
            return render(request, 'logIn', context)
    else:
        return render(request, 'dashboard', context)


def course_listing(request, userId):
    item = Course.objects.get(pk=userId)
    displayInfo = {
        'item': item,
    }
    return render(request, 'eLearningApp/course_list.html', displayInfo)


def edit(request, pkToEdit):
    item = get_object_or_404(Course, pk=pkToEdit)
    form = CourseForm(request.POST or None, instance=item)
    currentUser = request.user
    userForeignKey = Course.objects.get(pk=pkToEdit)
    common_tags = Course.tags.most_common()[:4]
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'course': Course,
        'common_tags':common_tags,
        'form': form,
        'userForeignKey': userForeignKey.foreignKey.username,
        'currentUser': currentUser,
        'usersPost': Course.objects.all(),
    }
    return render(request, 'eLearningApp/edit.html', context)


def logIn(request):
    if request.method == "POST":
        logged_in_user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if logged_in_user is not None:
            login(request, logged_in_user)
            return render(request, 'eLearningApp/dashboard.html')
        else:
            messages.error(request, "Incorrect Username or Password")
            return redirect('logIn')
    context = {
        "form": LogInForm
    }
    return render(request, "eLearningApp/logIn.html", context)


def signUp(request):
    print("Work")
    if request.method == 'POST':
        newUser = UserForm(request.POST or None)
        print("Hello")
        if newUser.is_valid():
            print("Debug")
            tempUser = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password'])
            CourseUser.objects.create(django_user=tempUser)
            tempUser.save()
            print("next line")
            login(request, tempUser)
            return redirect('dashboard')
        else:
            print("sign up issue")
            messages.error(request, "This user exists, new user name needed!")
            return redirect('signUp')
    else:
        context = {
            'form': UserForm(),

        }
        return render(request, 'eLearningApp/signUp.html', context)


def logOut(request):
    logout(request)
    return redirect('/')


def delete(request, userId):
    try:
        deleteUser = CourseUser.objects.get(user_id = userId)
        deleteUser.delete()
    except Exception as e:
        return HttpResponse('Something went wrong. Error Message : '+ str(e))
    messages.add_message(request, messages.INFO, "CourseUser Deleted Successfully !!!")
    return redirect('dashboard', user_id = userId)


def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        context = {
            'list': Course.objects.filter(title__contains=query)}
        return render(request, 'eLearningApp/search.html', context)


def practitioner_details(request, pkToPerson):
    person = CourseUser.objects.get(pk=pkToPerson)
    person_details = {
        'person': person,
    }
    return render(request, 'eLearningApp/user.html', person_details)


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


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name
    courses = Course.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'courses':courses,
    }
    return render(request, 'course_list.html', context)

#allows instructor to add a new entry
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            tempImageFile = request.FILES
            if not tempImageFile:
                tempImageFile = ''
            else:
                tempImageFile = tempImageFile['image']
            new_course = Course(title=request.POST['title'], slug=request.POST['slug'], image=tempImageFile, overview=request.POST['overview'],
                                info=request.POST['info'], author=request.user, tags=request.POST['tags'])
            new_course.save()
        return redirect('dashboard')

    context = {
        'form': CourseForm(),

    }
    return render(request, 'eLearningApp/add_course.html', context)