import datetime
import json
import logging
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import migrations, models
from django.templatetags.i18n import language
from import_export import resources


class CustomUser(AbstractUser):
    img = models.ImageField(
        upload_to='static/img', blank=True, null=True, default='static/img/user.jpg')
    middle = models.CharField(max_length=150, blank=True)
    note = models.TextField(blank=True, null=True, default='')
    isTranslator = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    page = models.ForeignKey('Page', on_delete=models.CASCADE,
                             null=True, blank=True, related_name='user_page')

    @staticmethod
    def translators():
        return CustomUser.active_users().filter(isTranslator=True)

    @staticmethod
    def active_users():
        return CustomUser.objects.filter(deleted=False)

    @staticmethod
    def terms():
        pass
        # return Terms.objects.filter(customUser deleted=False)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:edit_user', args=[str(self.id)])

    def full_name(self):
        return ' '.join([self.last_name, self.first_name, self.middle]).strip()

    def json_full_name_only(self):
        res = {
            'id': self.pk,
            'full_name': self.full_name(),
        }
        return res

    def json(self):
        res = {
            'id': self.pk,
            'username': self.username,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'middle': self.middle,
            'note': self.note,
            'img': str(self.img),
            'isTranslator': self.isTranslator,
            # 'deleted': self.deleted,
            'page': self.page.url if self.page else None,
        }
        return res


class Page(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='creator')
    modified = models.DateTimeField(null=True, blank=True)
    modificator = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='modificator')
    published = models.BooleanField(default=False)
    mainMenuLink = models.BooleanField(default=False)
    mainPageLink = models.BooleanField(default=False)

    deleted = models.BooleanField(default=False)

    url = models.CharField(max_length=200)
    title = models.CharField(max_length=140, blank=True, null=True, default='')
    shortTitle = models.CharField(
        max_length=20, blank=True, null=True, default='')
    keywords = models.CharField(
        max_length=255, blank=True, null=True, default='')
    description = models.CharField(
        max_length=255, blank=True, null=True, default='')
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
            'shortTitle': self.shortTitle,
            'description': self.description,
            'keywords': self.keywords,
        }
        return res

    def json(self):
        us = CustomUser.objects.filter(page_id=self.id)
        if len(us):
            res = {
                'id': self.pk,
                'created': str(self.created),
                'creator': self.creator.pk if self.creator else None,
                'modified': str(self.modified),
                'modificator': self.modificator.pk if self.modificator else None,
                'published': self.published,
                'deleted': self.deleted,
                'img': str(us[0].img),
                'first_name': str(us[0].first_name),
                'middle_name': str(us[0].middle),
                'last_name': str(us[0].last_name),

                'url': self.url,
                'title': self.title,
                'shortTitle': self.shortTitle,
                'description': self.description,
                'keywords': self.keywords,
                'content': self.content,
            }
        else:
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
                'shortTitle': self.shortTitle,
                'description': self.description,
                'keywords': self.keywords,
                'content': self.content,
            }
        return res

    def __str__(self):
        return ' | '.join([
            str(self.url),
            str(self.shortTitle if self.shortTitle else self.title),
        ])


class Language(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=16)

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
    wylie = models.CharField(max_length=216, unique=True)
    sa2ru1 = models.CharField(max_length=216, blank=True, default='')
    sa2ru2 = models.CharField(max_length=216, blank=True, default='')
    sa2ru3 = models.CharField(max_length=216, blank=True, default='')
    sa2en1 = models.CharField(max_length=216, blank=True, default='')
    sa2en2 = models.CharField(max_length=216, blank=True, default='')
    sa2en3 = models.CharField(max_length=216, blank=True, default='')
    sanscrit = models.CharField(max_length=216, blank=True, default='')
    tibetan = models.CharField(max_length=216, blank=True, default='')

    @staticmethod
    def by_wylie(wylie):
        try:
            return Term.objects.get(wylie=wylie)
        except Term.DoesNotExist as exc:
            return None

    @staticmethod
    def get_or_createnew(wylie):
        t = Term.by_wylie(wylie)
        if not t:
            t = Term(wylie=wylie)
            t.save()
            return t
        return t

    # def meanings(self):
    #     return Meaning.objects.filter(term=self)

    def sa2ru(self):
        res = self.sa2ru1
        if self.sa2ru2:
            res += "; %s" % self.sa2ru2
        if self.sa2ru3:
            res += "; %s" % self.sa2ru3
        return res

    def sa2en(self):
        res = self.sa2en1
        if self.sa2en2:
            res += "; %s" % self.sa2en2
        if self.sa2en3:
            res += "; %s" % self.sa2en3
        return res

    def __str__(self):
        return ' | '.join([
            str(self.wylie),
            str(self.sa2ru()),
            str(self.sa2en()),
            str(self.tibetan),
            str(self.sanscrit),
        ])

    def json(self, with_translator_info=False):
        res = {
            'id': self.pk,
            'wylie': self.wylie,
            'sa2ru': self.sa2ru(),
            'sa2en': self.sa2en(),
            'sanscrit': self.sanscrit,
            'tibetan': self.tibetan,
            'search_rank': self.rank,
        }
        res['meanings'] = []
        for m in self.meanings.all():
            res['meanings'].append(
                m.json(with_translator_info=with_translator_info))
        return res


class Meaning(models.Model):
    term = models.ForeignKey(
        Term, on_delete=models.CASCADE, related_name='meanings')
    translator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='meanings')
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name='language')
    meaning = models.CharField(max_length=512)
    # коментарий
    comment = models.TextField(blank=True, null=True, default='')
    # толкование
    interpretation = models.TextField(blank=True, null=True, default='')
    # контекст
    context = models.TextField(blank=True, null=True, default='')
    # обоснование
    rationale = models.TextField(blank=True, null=True, default='')

    @staticmethod
    def get_or_createnew(term, translator, language, meaning, comment=None):
        try:
            m = Meaning.objects.get(
                term=term, translator=translator, language=language, meaning=meaning)
            if comment:
                m.comment = comment
                m.save()
            return m
        except Meaning.DoesNotExist as exc:
            m = Meaning(term=term, translator=translator,
                        language=language, meaning=meaning)
            if comment:
                m.comment = comment
            m.save()
            return m

    def json(self, with_translator_info=False):
        res = {}
        if with_translator_info:
            res = {
                'id': self.pk,
                # 'term': self.term.json(),
                'translator': self.translator.json(),
                'language': self.language.json(),
                'meaning': self.meaning,
                'comment': self.comment,
                'interpretation': self.interpretation,
                'context': self.context,
                'rationale': self.rationale,
            }
        else:
            res = {
                'id': self.pk,
                #                'language': self.language.json(),
                'meaning': self.meaning,
                'comment': self.comment,
                'interpretation': self.interpretation,
                'context': self.context,
                'rationale': self.rationale,
            }

        return res

    def __str__(self):
        return ' | '.join([
            str(self.pk),
            str(self.term),
            # str(self.language),
            # str(self.translator),
            str(self.meaning),
            # str(self.comment),
        ])
