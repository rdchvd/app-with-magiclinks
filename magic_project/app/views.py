from django.shortcuts import render
from .forms import UserForm
from .models import User, Link
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from magic_project import settings

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.create(email=email)
            link = Link.objects.create(user=user)
            link.create_human_slug()
            sender = settings['EMAIL_HOST_USER']
            user_link = 'http://localhost:8000/' + str(link.slug)
            msg = 'Hello!\nWelcome to our site!\nYour link to visit:\n' + user_link
            send_mail('Your link on site', msg, sender, [user.email], fail_silently=False)
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})

def link(request, slug):
    try:
        link = Link.objects.get(slug=slug) 
        print(link)
        link.increment_counter()
    except Link.DoesNotExist:
        raise Http404('doesn`t exist')
    return render(request, 'index.html', {'views': link.counter})
    