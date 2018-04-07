from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)

from django.db.models import Q

from .forms import *
from .models import UserProfile

from django.conf import settings
from django.contrib import messages

import json
import urllib


def login_view(request):
	next = request.GET.get('next')
	title = "Авторизация"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())

		if result['success']:
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			login(request, user)
			if next:
				return redirect(next)
			return redirect("/")
		else:
			messages.error(request, 'Invalid reCAPTCHA. Please try again.')
	return render(request, "accounts/form.html", {"form":form, "title": title})

def register_view(request):
	next = request.GET.get('next')
	title = "Регистрация"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		if result['success']:
			user = form.save(commit=False)
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			new_user = authenticate(username=user.username, password=password)
			login(request, new_user)
			if next:
				return redirect(next)
			return redirect("/")
		else:
			messages.error(request, 'Invalid reCAPTCHA. Please try again.')

	context = {
		"form":form,
		"title": title
	}
	return render(request, "accounts/form.html", context)

def logout_view(request):
	logout(request)
	return redirect("/")

def userdetail(request, id=None):
	userobj = get_object_or_404(UserProfile, id=id)

	user = request.user

	runfollow = request.POST.get("username")
	if runfollow:
		if user in userobj.followers.all():
			userobj.followers.remove(user)
		else:
			userobj.followers.add(user)

	initial_data = {
		"object_id": userobj.id,
	}

	context = {
		"userobj": userobj,
	}
	return render(request, 'accounts/kabdetail.html', context)

def kablist(request):
	users_list = UserProfile.objects.filter(~Q(user=request.user))

	druzya = request.GET.get("d")
	if druzya:
		users_list = users_list.filter(
			Q(user__first_name__icontains=druzya)|
			Q(user__last_name__icontains=druzya)|
			Q(placework__icontains=druzya)|
			Q(city__icontains=druzya)
			).distinct()

	context = {
			"title": "ListUser",
			"users_list": users_list,
		}
	return render(request, 'accounts/kablist.html', context)


# createprofileimage
def kabinet(request):
	formimg = Createimg(request.POST or None, request.FILES or None)
	if formimg.is_valid():
		ins = formimg.save(commit=False)
		ins.user = request.user
		ins.save()
		return redirect("/kabinet/")
	context = {
		"forming": formimg,
	}
	
	return render(request, 'accounts/kabinet.html', context)
	
# editprofile
def kabinetedit(request):
	instance = get_object_or_404(UserProfile, user=request.user)
	try:
		profile = request.user.userprofile
	except UserProfile.DoesNotExist:
		profile = UserProfile(user=request.user)

	formimg = Editprofile(request.POST or None,request.FILES or None, instance=instance)
	if request.method == 'POST':
		if formimg.is_valid():
			instance = formimg.save(commit=False)
			instance.save()
			return redirect("/kabinet/")
	return render(request, 'accounts/kabedit.html', {'formimg': formimg})




def kabimgdel(request):
	instance = get_object_or_404(UserProfile, user=request.user)
	try:
		profile = request.user.userprofile
	except UserProfile.DoesNotExist:
		profile = UserProfile(user=request.user)

	instance.delete()
	return redirect("/kabinet/")