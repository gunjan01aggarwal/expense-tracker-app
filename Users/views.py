# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import logout
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.views import LoginView
#from django.contrib.auth.forms import PasswordChangeForm
#from django.contrib.auth import update_session_auth_hash

# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        """if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password or Username")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('money_manager:index')"""
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")

        
            #  Ensure Profile exists
            profile, created = Profile.objects.get_or_create(user=user)

            #  Check if profile is complete
            if not profile.is_complete():   # yeh method tum Profile model me bana sakti ho
                return redirect('/complete-profile/')  # redirect to profile completion page

            #  Agar profile complete hai to money_manager home page pe bhejo
            return redirect('money_manager:index')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('login_page')
    
    return render(request, 'users/login.html')
    

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        
        # Set the user's password and save the user object
        if password1==password2:
            user.set_password(password1)
            user.save()
        else:
            # Display an error message if the passwords do not match
            messages.error(request, "Passwords do not match!")
            return redirect('/register/')    
        
        # Display an information message indicating successful account creation
        messages.success(request, "Account created Successfully!")
        return redirect('/register/')
    
    # Render the registration page template (GET request)
    return render(request, 'users/register.html')

@login_required
def about(request):
     return render(request,"users/about.html")

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login_page')


# update profile information
@login_required
def profile_page(request):
    user = request.user

    # Ensure profile exists
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method=="POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('about')
        
        """if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, request.user)  # Keep user logged in after password change
            messages.success(request, "Your password has been updated successfully!")
            return redirect('about')
"""

    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)


    return render(request, 'users/profile.html', {'user_form': user_form,
                                                   'profile_form': profile_form})


# new user complete their profile infomation
@login_required
def complete_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('money_manager:index')  # ab home/dashboard pe bhejo
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'users/complete_profile.html', {'form': form})


# if user completed their profile information before, 
# he doesn't fill again his information.he redirect on home page.

