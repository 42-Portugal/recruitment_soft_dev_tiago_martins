from django.db import models

class Task(models.Model):
	STATUS_CHOICES = [
		('not_started', 'Not Started'),
		('in_progress', 'In Progress'),
		('done', 'Done'),
	]

	title = models.CharField(max_lenght=255)
	description = models.TextField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
	due_date = models.DateTimeField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks') #TODO: create Project class
	categories = models.ManyToManyField(Category, related_name='tasks') #TODO: create Category class
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title