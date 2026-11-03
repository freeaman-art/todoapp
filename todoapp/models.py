from django.db import models

# Create your models here.


class Todo_List(models.Model):
    TASK_CHOICES = [
        ('Personal', 'Personal'),
        ('Business', 'Business'),
        ('Job', 'Job'),
        ('Exercise', 'Exercise'),       
    ]
    category = models.CharField(max_length=50, choices=TASK_CHOICES, default='Other')    
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.category} - {self.name}"



