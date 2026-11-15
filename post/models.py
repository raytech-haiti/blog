from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse





class Articles(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Titre')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    date_update = models.DateTimeField(auto_now_add=True, verbose_name="Date modifier")
    date_create = models.DateTimeField(verbose_name="Date creation", blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publie")
    content = models.TextField(verbose_name="Contenu")
    thumbnail = models.ImageField(verbose_name="Images", blank=True, null=True, upload_to='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        ordering = ['-date_update']


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def author_default(self):
        return self.author.username if self.author else "Auteur inconnu"


    def get_absolute_url(self):
        return reverse('post:home')
