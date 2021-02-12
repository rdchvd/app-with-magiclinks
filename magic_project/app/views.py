from django.shortcuts import render
from django.http import Http404
from django.core.mail import send_mail

from .forms import UserForm
from .models import User, Link


def index(request):
    """Main page view: gets data from form and sends email"""
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]

            user = User.objects.create(email=email)
            link = Link.objects.create(user=user)
            link.create_human_slug()

            user_link = "http://localhost:8000/" + str(link.slug)
            msg = "Hello!\nWelcome to our site!\nYour link to visit:\n" + user_link
            sender = None
            title = "Your link on site"
            send_mail(title, msg, sender, [user.email], fail_silently=False)

    else:
        form = UserForm()

    return render(request, "index.html", {"form": form})


def link(request, slug):
    """View for page sent on email"""
    try:
        link = Link.objects.get(slug=slug)
        link.increment_counter()

    except Link.DoesNotExist:
        raise Http404("Page doesn`t exist")

    return render(request, "index.html", {"views": link.counter})


def custom404(request, exception):
    """Custom view for 404 error page"""
    return render(request, "index.html", {"error": True})
