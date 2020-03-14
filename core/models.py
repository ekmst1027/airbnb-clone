from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # DB에 저장되지 않게 설정
    class Meta:
        abstract = True
