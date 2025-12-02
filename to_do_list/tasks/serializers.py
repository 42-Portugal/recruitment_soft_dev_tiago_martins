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
	project_id = serializers.PrimaryKeyRelatedField(source='project', queryset=Project.object.all())
	categories_id = serializers.PrimaryKeyRelatedField(source='categories', many=True, queryset=Category.object.all())

	class Meta:
		model = Task
		fields = [
			'id',
			'title',
			'description',
			'status',
			'due_date',
			'project_id',
			'categories_id',
			'created_at',
			'updated_at'
		]