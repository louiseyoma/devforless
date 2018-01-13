from django.db import models
from django.utils import timezone



class JobPost(models.Model):
	employer = models.ForeignKey('auth.User', 'on_delete')
	job_title = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	desired_skills = models.TextField()
	job_description = models.TextField()
	time_of_post_creation = models.DateTimeField(default = timezone.now)


	def publish(self):
		self.time_of_post_creation = timezone.now()
		self.save()

'''
class Employer():
	name = models.ForeignKey('auth.User', 'on_delete')
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=15)
	address = models.TextField()
'''
