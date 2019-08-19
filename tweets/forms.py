from .models import Tweet

from django import forms



class TweetModelForm(forms.ModelForm):
	class Meta:
		model=Tweet
		fields=[
		#"user",
		"content"
		]


	# def clean(self,*args,**Kargs):
	# 	content=self.cleaned_data.get("content")
	# 	if content =="abc":
	# 		raise forms.ValidationError("nhi chale ga")
	# 	else :
	# 		pass
	# 	return content

