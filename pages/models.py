from django.db import models
from django.urls import reverse

class Page(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	last_update = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('page-detail', args = [self.id])
