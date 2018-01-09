from django.shortcuts import render, HttpResponse
from .forms import FormForLogin, CustomUserCreationForm
from django.http import HttpResponseRedirect 



def home(request):
    return render(request, 'devforlessapp/home.html')

def careers(request):
    return render(request, 'devforlessapp/careers.html')

def signup(request):
    return render(request, 'devforlessapp/signup.html')

def login(request):

	if request.method == 'POST':
		form = FormForLogin(request.POST)
		if form.is_valid():
			useremail = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")

			return HttpResponseRedirect('home')
	else:
		form = FormForLogin()
	return render(request, 'devforlessapp/login.html', {'form': form})

def register(request):
	if request.method == 'POST':
		f = CustomUserCreationForm(request.POST)
		if f.is_valid():
			f.save()
			#messages.success(request, 'Account created successfully')
			return HttpResponseRedirect('register')

	else:
		f = CustomUserCreationForm()
	return render(request, 'devforlessapp/register.html', {'form': f})

