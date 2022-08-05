from django.db import models
from users.models import AppUser
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=128)
    story = models.TextField(max_length=400)
    photo = models.ImageField(upload_to="posts_photos/", blank=True, null=True)  
    user_account = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering = ['-story']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})
    

    