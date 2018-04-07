from django.shortcuts import render, redirect
from .forms import SubscriberForm
import json
import urllib
from django.conf import settings
from django.contrib import messages


def feedbackdef(request):
    name = "Aren"
    current_day = "16.03.2018" # Realy
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        recaptcha_response = request.POST.get('d-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if result['success']:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

        else:
            data  = form.cleaned_data
            new_form = form.save()



    return render(request, 'feedback/feedback.html', locals())

