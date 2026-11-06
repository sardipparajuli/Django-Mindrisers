from django.db import models


class Todolist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title