from django.db import models


# Create your models here.
class histoy(models.Model):
    history = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.calculation
