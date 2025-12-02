from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Project, Task
from .serializers import ProjectSerializer, CategorySerializer, TasksSerializer

class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TasksSerializer