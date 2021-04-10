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

    url = models.URLField(max_length = 200)
    title = models.CharField(max_length=80, blank=True, null=True, default='')
    description = models.CharField(max_length=250, blank=True, null=True, default='')
    content = models.TextField(blank=True, null=True, default='')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:page', args=[str(self.id)])

    def __str__(self):
        return ' '.join([
            str(self.title),
            str(self.url),
        ])
