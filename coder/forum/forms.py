from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import Forum

class PostForm(forms.ModelForm):
	content = forms.CharField(widget=AdminPagedownWidget)
	class Meta:
		model = Forum
		fields = [
			"title",
			"categ",
			"content",
		]