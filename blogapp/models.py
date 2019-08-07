from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	area = models.CharField(max_length=100, default = "강남구 역삼1동")
	job_type = models.CharField(max_length=100, default = "서비스")
	gender = models.CharField(max_length=10, default=0)
	condition = models.CharField(max_length=200, null=True)
	age = models.CharField(max_length=3, null=True)
	edu = models.CharField(max_length=10, default=0)
	pay = models.CharField(max_length=100, null=True)
	userdate1 = models.CharField(max_length=10, default="")
	userdate2 = models.CharField(max_length=10, default="")
	time1 = models.CharField(max_length=10, default=0)
	time2 = models.CharField(max_length=10, default=0)
	plus = models.CharField(max_length=10, default=0)
	email =  models.CharField(max_length=30, null=True)
	call =  models.CharField(max_length=15, null=True)
	etc =  models.CharField(max_length=100, null=True)
	enddate = models.DateTimeField(null=True)
	pub_date = models.DateTimeField('date published')
	body = models.TextField()
	like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_user_set',through='Like')

	@property
	def like_count(self):
		return self.like_user_set.count()
	
	def __str__(self):
		return self.title

class Like(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
			
	class Meta:
		unique_together = (('user','blog'))	


