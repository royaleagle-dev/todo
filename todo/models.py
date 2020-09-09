from django.db import models

class Task(models.Model):
	name = models.CharField(max_length = 255)
	options = (
		('d', 'done'),
		('nd', 'Not Done'),
		)
	status = models.CharField(max_length = 2, choices = options, default = 'nd')
	date_added = models.DateField(auto_now_add = True)

	def __str__(self):
		return self.name


