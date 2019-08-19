from django import forms
from django.forms.utils import ErrorList
#create your mixin
class FormUserNeed(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(FormUserNeed, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList(["This user must be log in"])
            return self.form_invalid(forms)


class NotSameUser(FormUserNeed,object):
    def form_valid(self,form):
        if form.instance.user == self.request.user:
            return super(NotSameUser , self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList(["this user have not right to update this tweeet"])
            return self.form_invalid(form)
