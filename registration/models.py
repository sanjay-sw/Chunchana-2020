from django.db import models
from datetime import date
from PIL import *

SemChoice = (
    ('2nd Semester', 'Second Semester'),
    ('4th Semester', 'Fourth Semester'),
    ('6th Semester', 'Sixth Semester'),
    ('8th Semester', 'Eighth Semester'),
)


class ParticipantInfo(models.Model):
    ParticipantName = models.CharField(max_length=100, null=True)
    ParticipantEmail = models.EmailField(max_length=50, null=True)
    ParticipantPhNo = models.CharField(max_length=10, null=True)
    ParticipantUSN = models.CharField(max_length=10, null=True)
    ParticipantDOB = models.DateField(default=date.today, null=True)
    ParticipantSem = models.CharField(max_length=50, choices=SemChoice, default='2ndSem', null=True)
    ParticipantImage = models.ImageField(upload_to='Images/', height_field=None, width_field=None, max_length=1000)

    Event1 = models.BooleanField(default=False, blank=False)
    Event2 = models.BooleanField(default=False, blank=False)
    Event3 = models.BooleanField(default=False, blank=False)
    Event4 = models.BooleanField(default=False, blank=False)
    Event5 = models.BooleanField(default=False, blank=False)
    Event6 = models.BooleanField(default=False, blank=False)
    Event7 = models.BooleanField(default=False, blank=False)
    Event8 = models.BooleanField(default=False, blank=False)
    Event9 = models.BooleanField(default=False, blank=False)
    Event10 = models.BooleanField(default=False, blank=False)
    Event11 = models.BooleanField(default=False, blank=False)
    Event12 = models.BooleanField(default=False, blank=False)
    Event13 = models.BooleanField(default=False, blank=False)
    Event14 = models.BooleanField(default=False, blank=False)
    Event15 = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.ParticipantName
