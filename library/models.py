from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from library.validators import validate_max_year

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    picture = models.ImageField(upload_to='books/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1500), validate_max_year])
    publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        constraints = [
            UniqueConstraint(fields=['title', 'year', 'author'], name='unique_book')
        ]

    def __str__(self):
        return self.title + '__' + self.author.username
