import logging
import datetime
import json
from datetime import datetime
from import_export import resources

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import migrations, models

class CustomUser(AbstractUser):
    img = models.ImageField(upload_to='static/img', blank=True, null=True, default='static/img/user.jpg')
    middle = models.CharField(max_length=150, blank=True)
    note = models.TextField(blank=True, null=True, default='')

    deleted = models.BooleanField(default=False)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:edit_user', args=[str(self.id)])

    def full_name(self):
        return ' '.join([self.last_name, self.first_name, self.middle])
    

class Page(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='creator')
    modified = models.DateTimeField(null=True, blank=True)
    modificator = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='modificator')
    published = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    topmenu = models.BooleanField(default=False)
    url = models.CharField(max_length = 200)
    title = models.CharField(max_length=80, blank=True, default='')
    keywords = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    content = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:page', args=[str(self.id)])

    def json_no_content(self):
        res = {
            'id': self.pk,
            'created': str(self.created),
            'creator': self.creator.pk if self.creator else None,
            'modified': str(self.modified),
            'modificator': self.modificator.pk if self.modificator else None,
            'published': self.published,
            'deleted': self.deleted,
            
            'url': self.url,
            'title': self.title,
            'description': self.description,
            'keywords': self.keywords,
        }
        return res

    def json(self):
        res = {
            'id': self.pk,
            'created': str(self.created),
            'creator': self.creator.pk if self.creator else None,
            'modified': str(self.modified),
            'modificator': self.modificator.pk if self.modificator else None,
            'published': self.published,
            'deleted': self.deleted,
            
            'url': self.url,
            'title': self.title,
            'description': self.description,
            'keywords': self.keywords,
            'content': self.content,
        }
        return res
        
    def __str__(self):
        return ' | '.join([
            str(self.url),
            str(self.title),
        ])

class Language(models.Model):
    code = models.CharField(max_length = 5)
    name = models.CharField(max_length = 16)

class Term(models.Model):
    wylie = models.CharField(max_length = 216)
    sanscrit = models.CharField(max_length = 216)
    tibetian = models.CharField(max_length = 216)
    sa2ru = models.CharField(max_length = 216)
    sa2en = models.CharField(max_length = 216)


class Meaning(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term')
    translator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transtator')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language')
    meaning = models.CharField(max_length = 216)
    # толкование
    interpretation = models.TextField(blank=True, null=True, default='')
    # контекст
    context = models.TextField(blank=True, null=True, default='')
    # обоснование
    rationale = models.TextField(blank=True, null=True, default='')
