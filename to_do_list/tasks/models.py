from django.db import models
from django.utils import timezone

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title

class Task(models.Model):
	STATUS_CHOICES = [
		('not_started', 'Not Started'),
		('in_progress', 'In Progress'),
		('done', 'Done'),
	]

	title = models.CharField(max_length=255)
	description = models.TextField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
	due_date = models.DateTimeField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
	categories = models.ManyToManyField(Category, related_name='tasks')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	completed_at = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.title
	
	def save(self, *args, **kwargs):
		if self.status == 'done' and not self.completed_at:
			self.completed_at = timezone.now()
		super().save(*args, **kwargs)