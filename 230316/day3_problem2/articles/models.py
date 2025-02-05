# from django.db import models

# # Create your models here.
# class Movie(models.Model):
#     title = models.CharField(max_length=50)
#     genre = models.CharField(max_length=10)

#     def __str__(self):
#         return f'{self.id}번째 영화 - {self.title} {self.genre}'
    

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'