from django.contrib import admin
from .models import *
from .forms import *

class SubscriberAdmin (admin.ModelAdmin):
	list_display = [field.name for field in Feedback._meta.fields]
	list_filter = ['name',]
	search_fields = ['name', 'email', 'subject']

	fields = ["email", "name", "subject", "message"]

	class Meta:
		model = Feedback

admin.site.register(Feedback, SubscriberAdmin)