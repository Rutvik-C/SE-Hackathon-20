from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from Authority.models import problem

# Create your models here.
class rate(models.Model):
    user = models.ForeignKey(User,related_name="foods11",related_query_name="foods11",blank=True,on_delete=models.CASCADE)
    ratings = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.TextField(max_length=200)

class problem_selected(models.Model):
    p_id=models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name="order_foods", related_query_name="order_foods", null=True, blank=True,
                             on_delete=models.CASCADE)
    s = models.IntegerField(default=1)
    problem_title = models.ForeignKey(problem, on_delete=models.CASCADE, null=True)
    pdf = models.FileField(upload_to="documents", max_length=254, default='settings.MEDIA_ROOT/documents/SE Hackathon PS.pdf')
