from django.db import models
from django.utils import timezone

from accounts.models import Users
    

class BookTutors(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    tutor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='tutor')
    date = models.DateTimeField(default=timezone.now)
    is_done = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    price = models.IntegerField()
    hour = models.IntegerField()
    

class ReviewOfTutors(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='writer')
    tutor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='reviewed_tutor')
    review = models.TextField(max_length=500)
    