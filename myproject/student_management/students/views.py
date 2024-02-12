from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Student
from django.urls import reverse_lazy

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'roll_number', 'grade']
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'roll_number', 'grade']
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
