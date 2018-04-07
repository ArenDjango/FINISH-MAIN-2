from django.db import models


class Feedback(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=50)
	subject = models.TextField()
	message = models.TextField()



	def __str__(self):
		return "Собшение %s %s %s %s" %(self.email, self.name, 
										self.subject, self.message)

	class Meta:
		verbose_name = 'Собшение'
		verbose_name_plural = 'Собшении'