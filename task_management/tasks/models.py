from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    title = models.CharField(max_length=255)
    
    description = models.TextField()
   
    due_date = models.DateField()
    
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    
    status = models.BooleanField(default=False)  # False = Pending, True = Completed
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    completed_at = models.DateTimeField(null=True, blank=True)
    # creates a relationship between task and user.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title