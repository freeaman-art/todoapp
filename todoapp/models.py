from django.db import models

# Create your models here.


class todo_list(models.Model):
    TASK_CHOICES = [
        ('Personal', 'Personal'),
        ('Business', 'Business'),
        ('Job', 'Job'),
        ('Exercise', 'Exercise'),       
    ]
    category = models.CharField(max_length=50, choices=TASK_CHOICES, default='AEO-SEO-GEO')    
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.category} - {self.name}"



