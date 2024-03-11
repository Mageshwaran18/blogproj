from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Skill(models.Model):
    skill_name = models.CharField(max_length=255, default=' ')

    def __str__(self):
        return self.skill_name

class ProjectsDone(models.Model):
    project_name = models.CharField(max_length=255, default=' ')

    def __str__(self):
        return self.project_name

class DomainInterest(models.Model):
    domain_name = models.CharField(max_length=100, default=' ')

    def __str__(self):
        return self.domain_name

class UserInfo(models.Model):
    name = models.CharField(max_length=100,default=None)
    email = models.EmailField(default=None)
    domain = models.CharField(max_length=100,default=None)
    city = models.CharField(max_length=100,default=None)    
    phone_number = models.CharField(max_length=15,default=None)
    skills = models.ManyToManyField(Skill, blank=True,default=None)
    projects_done = models.ManyToManyField(ProjectsDone, blank=True,default=None)
    domain_interest = models.ManyToManyField(DomainInterest, blank=True,default=None)
    skillss=models.CharField(max_length=120,default=None)
    projects=models.CharField(max_length=120,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    choices = [
        ('available', 'Available'),
        ('working', 'Working on the Project'),
    ]
    choicess=[
        ('ECE','ECE'),
        ('MECH','Mech'),
        ('CSE','CSE'),
        ('AIDS','AIDS'),
    ]
    choicesss=[
        ('I','I'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
    ]
    available = models.CharField(max_length=20, choices=choices,default='available')
    department=models.CharField(max_length=20, choices=choicess,default='CSE')
    year=models.CharField(max_length=20, choices=choicesss,default='I')
    linkedin=models.CharField(max_length=100,default='',null=True)
    github=models.CharField(max_length=100,default='',null=True)
    about=models.TextField(max_length=200,default=None,null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null = True)

    def __str__(self):
        return self.name
