from django.db import models


class Post(models.Model):
	text = models.TextField()

	def __str__(self):
		"""a string representation of model"""
		return self.text[:50]


