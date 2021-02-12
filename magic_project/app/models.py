from django.db import models
from django.db.models.fields import CharField, EmailField, IntegerField
import random


class User(models.Model):
    """Model for user data"""

    email = EmailField(unique=True)

    @property
    # returns hash of inputted email
    def magic_link(self):
        return hash(self.email)

    def __str__(self):
        return "email: {0}\nhash: {1}".format(self.email, self.magic_link)


class Link(models.Model):
    """Model creates link for user"""

    slug = CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    counter = IntegerField(default=0, blank=True)

    def __str__(self):
        return self.slug

    def increment_counter(self):
        #  function increments num of user gets page
        self.counter += 1
        self.save()
        return self.counter

    def readable_link(self):
        # function gets 3 random words from wordlist
        # and makes a slug
        diapazone = int(str(self.user.magic_link).replace("-", "")[:3])
        string = open("app/wordlist.txt", "r").read()
        lst = string.split("\n")
        final_lst = []
        for i in range(3):
            num = random.randrange(diapazone)
            final_lst.append(lst[num])
        return "-".join(final_lst)

    def create_human_slug(self):
        # function checks if not created slug exists
        while True:
            self.slug = self.readable_link()
            if len(Link.objects.filter(slug=self.slug)) == 0:
                break
        self.save()
        return self.slug
