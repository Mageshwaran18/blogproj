from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
    domain = forms.CharField(max_length=100)
    AVAILABLE_CHOICES = [
        ('available', 'Available'),
        ('working', ' Currently Working on a Project'),
    ]
    available = forms.ChoiceField(choices=AVAILABLE_CHOICES)
    city = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    skills = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    domain_interest= forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    projects_done = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    skillss = forms.CharField(max_length=30, widget=forms.Textarea, required=False)
    projects = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    choicess=[
        ('ECE','ECE'),
        ('MECH','Mech'),
        ('CSE','CSE'),
        ('AIDS','AIDS'),
    ]
    department=forms.ChoiceField(choices=choicess)
    choicesss=[
        ('I','I'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
    ]
    year=forms.ChoiceField(choices=choicesss)
    linkedin = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    github = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    about = forms.CharField(max_length=250,widget=forms.Textarea,required=True)
    profile_picture = forms.ImageField(required=False)

    def clean_skills(self):
        skills = self.cleaned_data.get('skills')
        return [skill.strip() for skill in skills.split(',') if skill.strip()]

    def clean_domain_interest(self):
        domain_interest = self.cleaned_data.get('domain_interest')
        return [domain.strip() for domain in domain_interest.split(',') if domain.strip()]

    def clean_projects_done(self):
        projects_done = self.cleaned_data.get('projects_done')
        return [project.strip() for project in projects_done.split(',') if project.strip()]
