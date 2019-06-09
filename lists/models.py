from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    AUTHOR = 1
    PUBLISHER = 2
    USER_TYPES = ((AUTHOR, 'Author'),(PUBLISHER, 'Publisher'),)
    user_type = models.CharField(choices=USER_TYPES, max_length=100)
    no_of_books = models.IntegerField(default=0)

    @classmethod
    def get_authors(cls,):
        return cls.objects.filter(uset_type=cls.AUTHOR)

    def can_write_books(self):
        return self.user_type == self.AUTHOR
