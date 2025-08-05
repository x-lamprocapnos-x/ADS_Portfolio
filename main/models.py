# main/models.py
from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/')
    description = models.TextField()
    case_study = models.TextField() # Will be URL when done
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:project_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.project.title} - Image"