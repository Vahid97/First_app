from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Message, Profile, Skill
from django.contrib.auth import authenticate, login, logout
from projects.models import Project
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm

def loginUser(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    

    if request.method == 'POST':

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user-profile', pk=user.id)
        else:
            messages.error(request, 'Invalid Form')
    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('projects')


def user_profile(request, pk):

    user = User.objects.get(id=pk)
    profile = user.profile
    skills = profile.skill_set.all()

    context = {'user':user, 'skills':skills}

    return render(request, 'users/user-profile.html', context)

def registerUser(request):

    userObj = request.POST

    if request.method == 'POST':
        emptyField = ''
        if userObj['username'] and userObj['password'] and userObj['email'] != emptyField:
            user = User.objects.create_user(userObj['username'], userObj['email'], userObj['password'])
            user.save
        else:
            messages.error(request, 'Invalid Form')
    
    return render(request, 'users/register.html')

def addProject(request):
    details = request.POST
    if request.method == 'POST':
        emptyField = ''
        if details['title'] and details['description'] != emptyField:
            projectCreate = Project.objects.distinct().create(title=details['title'], description=details['description'])
            projectCreate.tags.create(name=details['tag'])
        else:
            messages.error(request, 'Invalid Form')



    return render(request, 'users/add-project.html')


def addSkill(request):

    details = request.POST
    if request.method == 'POST':
        emptyField = ''
        if details['name'] and details['description'] != emptyField:
            skillCreate = Skill.objects.create(name=details['name'])
            skillCreate.save()
        else:
            messages.error(request, 'Invalid Form')

    return render(request, 'users/add-skill.html')


def getDevelopers(request):
    developers = User.objects.all()

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        developers = User.objects.filter(username=search_query)

    context = {'developers':developers}

    return render(request, 'users/developers.html', context)

@receiver(post_save, sender=User)
def profileSignal(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name = user.username,
            email = user.email,
        )

@receiver(post_delete, sender=Profile)
def deleeteProfileSignal(sender, instance, **kwargs):
    
    try:
        user = instance.user
        user.delete()
    except:
        pass


def inbox(request, pk):

    user = User.objects.get(id=pk)
    profile = user.profile
    messages = profile.receiver.all()

    context = {'messages':messages}

    return render(request, 'users/inbox.html', context)


def messageInbox(request, pk):

    message = Message.objects.get(id=pk)

    context = {'message':message}

    return render(request, 'users/message.html', context)


def sendMessage(request, pk):

    subject = request.POST.get('subject')
    print(subject)
    body = request.POST.get('body')
    receiver = str(request.POST.get('receiver'))
    

    if request.method == 'POST':
        user = User.objects.get(id=pk)
        user_filter = User.objects.get(username=receiver)
        profile_filter = user_filter.profile
        profile = user.profile
        createMessage = Message.objects.create(sender=profile, receiver=profile_filter, subject=subject, body=body)

    return render(request, 'users/send-message.html')











