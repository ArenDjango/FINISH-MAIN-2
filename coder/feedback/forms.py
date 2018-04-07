from django import forms
from .models import *

from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

import os
import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        os.environ['RECAPTCHA_DISABLE'] = 'True'

    def test_myform(self):
        form = MyForm({
            'field1': 'field1_value'
        })
        self.assertTrue(form.is_valid())

    def tearDown(self):
        del os.environ['RECAPTCHA_DISABLE']

class SubscriberForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = Feedback
        exclude = [""]