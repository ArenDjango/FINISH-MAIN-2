from django.db import models
from django.urls import reverse

from django.conf import settings

from markdown_deux import markdown
from comments.models import Comment



from django.contrib.contenttypes.models import ContentType

# def upload_location(instance, filename):
# 	return "%s/%s" %(instance.id, filename)


class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
					default=1, 
					on_delete=models.CASCADE)
	title = models.CharField(max_length=70)
	content = models.TextField()
	image = models.ImageField(upload_to='imageposts/',
			null=True,
			blank=True,)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	categ = models.CharField(max_length=40)
	prosmotr = models.IntegerField(default=1)
	like = models.IntegerField(default=0)
	dizlike = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})



	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(self)
		return qs
		
	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(
					   instance.__class__)
		return content_type


	class Meta:
		ordering = ["-timestamp", "-updated"]