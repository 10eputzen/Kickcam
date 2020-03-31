from django.db import models
from datetime import datetime
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.utils.translation import gettext as _

#

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
		
class Replay(models.Model):
	audio = models.CharField(max_length=100, blank=True, default='')
	duration = models.PositiveSmallIntegerField(default=5, blank=False, null=True)
	frames = models.PositiveSmallIntegerField(default=10, blank=False, null=True)
	date = models.DateTimeField(auto_now_add=False, blank = True)
	filePath = models.CharField(max_length=100, blank=True, default='')



	class Meta:
		ordering = ('date',)


class Features(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0, blank=True)

    class Meta:
        ordering = ('-created',)


