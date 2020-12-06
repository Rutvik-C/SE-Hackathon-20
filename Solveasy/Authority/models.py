from django.db import models
from django.contrib.auth.models import User

class Belongs(models.Model):
    user = models.OneToOneField(User, related_name="belong", related_query_name="belong", null=True, blank=True,
                                on_delete=models.CASCADE)
    is_authority = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Cities(models.Model):
    name = models.CharField(max_length=100, default="enter")

    def __str__(self):
        return self.name

CHOICES = (
    ('institute','INSTITUTE'),
    ('student', 'STUDENT')
)
class otherDetails(models.Model):
    user = models.OneToOneField(User, related_name="details", related_query_name="details", null=True, blank=True,on_delete=models.CASCADE)
    address = models.TextField(max_length=250, blank=True)
    phonenumber = models.IntegerField(default=9898944123)
    image = models.ImageField(upload_to='Authority/images')
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True)
    choice = models.CharField(max_length=10, choices=CHOICES, default='institute', null=True)
    def __str__(self):
        return self.address

class problem(models.Model):
    user = models.ForeignKey(User, related_name="foodss", related_query_name="foodss", null=True, blank=True,on_delete=models.CASCADE)
    otherDetails = models.OneToOneField(otherDetails, null=True, blank=True, on_delete=models.CASCADE)
    problem_title = models.CharField(max_length=100,default="enter")
    problem_desc = models.TextField(max_length=100)
    images = models.ImageField(upload_to='Authority/images', null=True, blank=True)
    city = models.CharField(max_length=100, default="enter")
    created_on = models.DateTimeField(auto_now_add=False , editable=True,null=True)

    def __str__(self):
        return str(self.user.username)
