from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    SKIll_LEVEL = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    )

    COUNTRY = (
        ('Kenya', 'Kenya'),
        ('Rwanda', 'Rwanda'),
      ('Uganda', 'Uganda'),
        
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50,null=True)
    gender =  models.CharField(max_length=20,choices=GENDER,null=True)
    assessor = models.BooleanField(default=False)
    country = models.CharField(max_length=20,choices=COUNTRY,null=True)
    language = models.TextField(max_length=500, blank=False)
    skill_level = models.CharField(max_length=20, choices=SKIll_LEVEL)
    institution = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username


# Hooking the following methods to the Django defined User model
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()