import datetime
import uuid
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Movie(models.Model):
    id = models.UUIDField(primary_key=True,
       default=uuid.uuid4, editable=False)
    current_year=int(datetime.datetime.now().strftime ("%Y"))
    title = models.CharField(max_length=150)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1930),MaxValueValidator(current_year)])
    Dhero = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])
