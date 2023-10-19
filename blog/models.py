from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200, default="youShouldn'tSeeThis")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, default='weslee')
    task = models.TextField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})