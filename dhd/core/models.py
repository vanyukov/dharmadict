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
    title = models.CharField(max_length=80, blank=True, null=True, default='')
    keywords = models.CharField(max_length=255, blank=True, null=True, default='')
    description = models.CharField(max_length=255, blank=True, null=True, default='')
    content = models.TextField(blank=True, null=True, default='')

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
    def __str__(self):
        return ' | '.join([
            str(self.code),
            str(self.name),
        ])

    def json(self):
        res = {
            'id': self.pk,
            'code': self.code,
            'name': self.name,
        }
        return res

class Term(models.Model):
    wylie = models.CharField(max_length = 216)
    sa2ru = models.CharField(max_length = 216, blank=True, default='')
    sa2en = models.CharField(max_length = 216, blank=True, default='')
    sanscrit = models.CharField(max_length = 216, blank=True, default='')
    tibetan = models.CharField(max_length = 216, blank=True, default='')

    def meanings(self):
        return Meaning.objects.filter(term=self)


    def __str__(self):
        return ' | '.join([
            str(self.wylie),
            str(self.tibetan),
            str(self.sanscrit),
        ])

    def json(self):
        res = {
            'id': self.pk,
            'wylie': self.wylie,
            'sa2ru': self.sa2ru,
            'sa2en': self.sa2en,
            'sanscrit': self.sanscrit,
            'tibetan': self.tibetan,
        }
        for m in self.meanings():
            res['meanings'] = m.json()
        return res


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

    def json(self):
        res = {
            'id': self.pk,
            # 'term': self.term.json(),
            'translator': self.translator.json(),
            'language': self.language.json(),
            'meaning': self.meaning,
            'interpretation': self.interpretation,
            'context': self.context,
            'rationale': self.rationale,
        }
        return res


    def __str__(self):
        return ' | '.join([
            str(self.term),
            str(self.language),
            str(self.meaning),
        ])
