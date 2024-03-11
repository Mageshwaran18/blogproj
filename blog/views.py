from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Case, When, Value, CharField
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)
form=UserForm()

def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


def room(request):
    return render(request, 'blog/room.html')



class PostListView(LoginRequiredMixin, ListView):
    model = UserInfo
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by(
            Case(
                When(available='available', then=Value(1)),
                When(available='working', then=Value(2)),
                default=Value(3),
                output_field=CharField()
            ),
            '-created_at'
        )
        return queryset


class PostDetailView(LoginRequiredMixin, DetailView):
    model = UserInfo
    template_name='blog/index.html'
    context_object_name = 'UserInfo'


def createProfile(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        print("Form is submitted")
        if form.is_valid():
            # Check if UserInfo with given name and email already exists
            info_obj, created = UserInfo.objects.get_or_create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                defaults={
                    'domain': form.cleaned_data['domain'],
                    'available': form.cleaned_data['available'],
                    'city': form.cleaned_data['city'],
                    'phone_number': form.cleaned_data['phone_number'],
                    'skillss': form.cleaned_data['skillss'],
                    'projects': form.cleaned_data['projects'],
                    'year':form.cleaned_data['year'],
                    'linkedin':form.cleaned_data['linkedin'],
                    'github':form.cleaned_data['github'],
                    'department':form.cleaned_data['department'],
                    'about':form.cleaned_data['about'],
                    'profile_picture':form.cleaned_data['profile_picture']
                }
            )
            # If UserInfo already exists, update its attributes
            if not created:
                info_obj.domain = form.cleaned_data['domain']
                info_obj.available = form.cleaned_data['available']
                info_obj.city = form.cleaned_data['city']
                info_obj.phone_number = form.cleaned_data['phone_number']
                info_obj.skillss = form.cleaned_data['skillss']
                info_obj.projects = form.cleaned_data['projects']
                info_obj.department = form.cleaned_data['department']
                info_obj.year = form.cleaned_data['year']
                info_obj.linkedin = form.cleaned_data['linkedin']
                info_obj.github = form.cleaned_data['github']
                info_obj.about = form.cleaned_data['about']
                info_obj.profile_picture = form.cleaned_data['profile_picture']

                info_obj.save()

            # Clear and update related fields
            info_obj.skills.clear()
            info_obj.projects_done.clear()
            info_obj.domain_interest.clear()

            for skill_name in form.cleaned_data['skills']:
                skill_obj, created = Skill.objects.get_or_create(skill_name=skill_name)
                info_obj.skills.add(skill_obj) 
            for project_name in form.cleaned_data['projects_done']:
                project_obj, created = ProjectsDone.objects.get_or_create(project_name=project_name)
                info_obj.projects_done.add(project_obj)            
            for domain_name in form.cleaned_data['domain_interest']:
                domain_obj, created = DomainInterest.objects.get_or_create(domain_name=domain_name)
                info_obj.domain_interest.add(domain_obj)      

            return redirect('blog-home')
        else:
            form = UserForm(initial={
                'name': request.user.username,
                'email': request.user.email,
            })
            print(form.errors)
    else:
        form = UserForm(initial={
            'name': request.user.username,
            'email': request.user.email,
        })
        print("Form is not submitted")

    return render(request, 'blog/form.html', {'form': form})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserInfo

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = UserInfo
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def chat_room(request):
    usernames = UserInfo.objects.all()
    messages = Message.objects.select_related('sender').all()
    return render(request, 'blog/chat.html', {'messages': messages,'usernames': usernames})


def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('message')
        if content:
            message = Message.objects.create(sender=request.user, content=content)
    return redirect('chat')

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    # Check if the current user is the one who posted the message
    if request.user == message.sender:
        message.delete()

    return redirect('chat')