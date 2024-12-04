from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import signupForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect( "home")
    else:
        records = signupForm()
        return render(request, "home.html", {'records': records})

def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            
            logout_user(request)
            return redirect("home")  # Redirect to login after signup
            messages.success(request, "Account created successfully! Please log in.")
        else:
            messages.error(request, "An error occurred during signup. Please try again")
            return redirect('signup')  
    else:
        form = signupForm()
    return render(request, "signup.html", {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')



