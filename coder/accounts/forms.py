from django import forms

from django.contrib import messages

import json
import urllib

from pagedown.widgets import AdminPagedownWidget

from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)

from .models import UserProfile
from feedback.forms import *

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField(label='Логин')
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect passsword")
			if not user.is_active:
				raise forms.ValidationError("This user is not longer active.")
		return super(UserLoginForm, self).clean(*args, **kwargs)
		

class UserRegisterForm(forms.ModelForm):
	username = forms.CharField(label='Логин')
	email = forms.EmailField(label='Email')
	email2 = forms.EmailField(label='Повторите Email')
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
	first_name = forms.CharField(label='Имя')
	last_name = forms.CharField(label='Фамилия')
	class Meta:
		model = User
		fields = [

			'email',
			'email2',

			'first_name',
			'last_name',

			'username',
			'password',

		]

	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Emails must match")

		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered")
		return email


class Createimg(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [
			"avatar",
		]

class Editprofile(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = [
			"avatar",
			"placework",
			"city"
		]