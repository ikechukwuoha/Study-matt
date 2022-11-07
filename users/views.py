from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from django.core.mail import send_mail
from jet.models import Topic



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('jet1:index')
    page = 'register'
    user = get_user_model()
    
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            messages.success(request, f'Dear {user.email} You have been Registered!')
            return redirect('jet:index')
        
        else:
            messages.error(request, f'Something went wrong, Please try again')
            
    else:
        form = CustomUserCreationForm()
    
    
    context = {'form': form, 'page': page}
    return render(request, 'users/register.html', context)





def logoutPage(request):
    page = 'logout'
    logout(request)
    
    context = {'page': page}
    return render(request, 'users/loggedout.html', context)



def loginPage(request):
    User = get_user_model()
    if request.user.is_authenticated:
        return redirect('jet1:index')
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            
        except:
            messages.error(request, f'User does not exist...')
            
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Hello {user.username} Logged in successfully')
            return redirect('jet:index')
        
        else:
            messages.error(request, f'invalid Credentials...')
            

    context = {'page': page}
    return render(request, 'users/login.html', context)





def userProfile(request, pk):
    User = get_user_model()
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'users/profile.html', context)