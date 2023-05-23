from django.db import models
from django.utils import timezone

from accounts.models import Users


EVALUATION_TYPES = (
    ('Very Good', 'Very Good'),
    ('Good', 'Good'),
    ('Not Bad', 'Not Bad'),
    ('Bad', 'Bad'),
    ('Very Bad', 'Very Bad'),
)
    

class BookTutors(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    tutor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='tutor')
    start_date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    is_done = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    price = models.IntegerField()
    

class ReviewOfTutors(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='writer')
    tutor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='reviewed_tutor')
    lecture = models.ForeignKey(BookTutors, on_delete=models.CASCADE, related_name='lecture', null=True)
    review = models.TextField(max_length=500)
    evaluation = models.CharField(max_length=100, default='Not Bad' ,choices=EVALUATION_TYPES)
    