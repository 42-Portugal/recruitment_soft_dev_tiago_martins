from rest_framework import serializers
from models import Project, Category, Task

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = [
			'id',
			'name'
			]

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = [
			'id',
			'title',
			'description']

class TasksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = [
			'id',
			'title',
			'description',
			'status',
			'due_date',
			'project',
			'categories',
			'created_at',
			'updated_at'
		]