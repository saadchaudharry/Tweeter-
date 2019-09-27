from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.conf import settings

# Create your models here.
def validation(value):
	content=value
	if content=="":
		raise ValidationError("Tweet can be blank")
	return value


class Tweet(models.Model):
	user  		=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	content 	=models.CharField(max_length=142,validators=[validation])
	updated		=models.DateTimeField(auto_now=True)
	timestamp	=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("tweet:detail",kwargs={"pk":self.pk})

	class Meta:
		ordering =['-timestamp']



	# def clean(self,*args,**Kargs):
	# 	content=self.content
	# 	if content =="abc":
	# 		raise ValidationError("nhi chale ga"\
	# 	return super(Tweet,self).clean(*args,**Kargs)