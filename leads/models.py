from django.db import models
# from django.contrib.auth import get_user_model  # Built in user model
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# User = get_user_model()  # Built in user model

'''It is highly recommended to created you own users to avoid complexity in
big application'''


class User(AbstractUser):
    # We can modify this class in future according to our need
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    # SOURCE_CHOICES = (
    #     ('YouTube', 'Youtube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
    # )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    # agent = models.ForeignKey(Agent, on_delete=models.CASCADE, SET_DEFAULT, default=0, SET_NULL, null=True)
    '''IF the Agent class is defined before the Lead class we did not have to declare the Agent class in the foreignKey
    in double quotes. Also we can set it as default value or null value when the Agent gets deleted. The CASCADE 
    will automatically delete the lead when the associated Agents gets deleted'''

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    #
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username


def post_user_created_signal(sender, instance, created, **kwargs):
    # print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
