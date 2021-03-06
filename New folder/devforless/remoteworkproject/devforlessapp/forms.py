from django import forms
from django.forms import ModelForm
from .models import JobPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class FormForLogin(forms.Form):
	email = forms.EmailField(label='Email Address', max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)

	def check_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		#if r.count():


class CustomUserCreationForm(forms.Form):
	username = forms.CharField(label='Enter your name', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class' : 'form-control white-border', 'id' : 'formGroupExampleInput'}))
	email = forms.EmailField(label='Email address', required=True, widget=forms.TextInput(attrs={'class' : 'form-control white-border', 'id' : 'formGroupExampleInput'}))
	password1 = forms.CharField(label='Choose password', widget=forms.TextInput(attrs={'class' : 'form-control white-border', 'id' : 'formGroupExampleInput2'}))
	password2 = forms.CharField(label='Confirm password', widget=forms.TextInput(attrs={'class' : 'form-control white-border', 'id' : 'formGroupExampleInput2'}))


	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise ValidationError("Username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count():
			raise ValidationError("Email already exists")
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise ValidationError("Passwords dont match")
		return password2

	def save(self, commit=True):
		user = User.objects.create_user(
			self.cleaned_data['username'],
			self.cleaned_data['email'],
			self.cleaned_data['password1']
		)
		return user



class JobPostForm(forms.ModelForm):
	class Meta:
		model = JobPost
		fields = ['job_title', 'category', 'desired_skills', 'job_description']







