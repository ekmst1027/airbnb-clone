from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # DB에 저장되지 않게 설정
    class Meta:
        abstract = True
