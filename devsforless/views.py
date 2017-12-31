from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect 
from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'devsforless/home.html')

def careers(request):
    return render(request, 'devsforless/careers.html')



def signup(request):
	if request.method == 'POST':
		f = CustomUserCreationForm(request.POST)
		if f.is_valid():
			f.save()
			#messages.success(request, 'Account created successfully')
			return HttpResponseRedirect('signup')

	else:
		f = CustomUserCreationForm()
	return render(request, 'devsforless/signup.html', {'form': f})

