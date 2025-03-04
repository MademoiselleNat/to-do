from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        null = True,
        )
    title = models.CharField(
        max_length = 150,
        blank = True,
        null = True,
        )
    description = models.TextField(
        blank = True,
        null = True,
    )
    completed = models.BooleanField(
        default = False,
    )
    created = models.DateTimeField(
        auto_now_add = True,
    )

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed']
