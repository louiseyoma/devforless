from django.shortcuts import render, HttpResponse
from .forms import FormForLogin, CustomUserCreationForm, JobPostForm
from django.http import HttpResponseRedirect
from django.utils import timezone



def home(request):
    return render(request, 'devforlessapp/home.html')

def careers(request):
    return render(request, 'devforlessapp/careers.html')

def signup(request):
    return render(request, 'devforlessapp/signup.html')


def suc(request):
	return render(request, 'devforlessapp/success_page.html')











def post_job(request):

	if request.method == "POST":
		form = JobPostForm(request.POST)
		if form.is_valid():
			jobpost = form.save(commit=False)
			jobpost.employer = request.user
			jobpost.time_of_post_creation = timezone.now()
			jobpost.save()
			return HttpResponseRedirect('suc')
	else:
		form = JobPostForm()
	return render(request, 'devforlessapp/post_job.html', {'form': form} )


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

