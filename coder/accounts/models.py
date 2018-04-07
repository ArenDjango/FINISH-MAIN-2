from django.db import models
from django.urls import reverse

from django.conf import settings

from markdown_deux import markdown
from comments.models import Comment

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='imageusers', verbose_name='Изображение')
	infouser = models.CharField(max_length=40, default=5)
	placework = models.TextField(default='Отсутствует')
	city = models.TextField(default='Отсутствует')
	followers = models.ManyToManyField(User, 
				related_name='is_following',
				blank=True)

	def __unicode__(self):
		return self.user

	def user_get_absolute_url(self):
		return reverse("accounts:userdetail", kwargs={"id": self.id})

class Meta:
	verbose_name = 'Профиль'
	verbose_name_plural = 'Профили'