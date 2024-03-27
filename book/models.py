from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


# 3. create 2 models in the app for storing data of books and authors
#     -- authors[first_name, last_name, email, books_count, average_rating]
# -- books[name, price, average_rating, count, author(foreign key)
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    books_count=models.PositiveIntegerField()
    average_rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    book_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    average_rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    count=models.PositiveIntegerField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.book_name