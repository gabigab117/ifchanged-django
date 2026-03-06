from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Article"
        ordering = ['-created_at']
