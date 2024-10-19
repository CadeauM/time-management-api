from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    # priority levels
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    # task fields
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()  # date by which the tasks should be completed
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)  # task priority
    is_completed = models.BooleanField(default=False)  # False = Pending, True = Completed, status: completed or not
    created_at = models.DateTimeField(auto_now_add=True)  # automatically set when created
    completed_at = models.DateTimeField(null=True, blank=True)  #set when task is marked complete
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  # associated user

    def __str__(self):  # string representation of the model, useful in admin interface
        return self.title

    def save(self, *args, **kwargs):
        # automitically set completed_at when task is marked complete
        if self.is_completed and not self.completed_at:
            self.completed_at = timezone.now()
        # Reset completed_at if task is marked incomplete again
        elif not self.is_completed and self.completed_at:
            self.completed_at = None
        super().save(*args, **kwargs)

        