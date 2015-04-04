from __future__ import division
from django.db import models
from django.utils.timezone import localtime, now
from django.contrib.auth.models import User

from .validators import validate_score


class Group(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Technique(models.Model):

    radio_id = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=100)
    staff = models.ForeignKey(Group, related_name='techniques', null=True)
    person_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    note = models.CharField(max_length=200, blank=True)
    check_condition = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @property
    def patrols_number(self):
        return self.tests.all().count()

    @property
    def last_patrol(self):
        return self.tests.latest('created_date').created_date_hms


class Patrol(models.Model):

    group = models.ForeignKey(Group, related_name='patrols')
    name = models.CharField(max_length=100)
    hour_condition = models.BooleanField(default=True)

    class Meta:
        ordering = ('group', 'name')

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.group)

    @property
    def technique_score(self):
        return sum([t.technique_score for t in self.tests.all()], 0)

    @property
    def style_score(self):
        return sum([t.style_score for t in self.tests.all()], 0)

    @property
    def total_score(self):
        return self.technique_score + self.style_score

    @property
    def tests_num(self):
        return self.tests.all().count()

    @property
    def avg_technique_score(self):
        if self.tests_num > 0:
            return self.technique_score / self.tests_num
        else:
            return 0

    @property
    def avg_style_score(self):
        if self.tests_num > 0:
            return self.style_score / self.tests_num
        else:
            return 0

    @property
    def check_condition(self):
        if self.tests.filter(technique__check_condition=True).count() > 0:
            return True
        else:
            return False

    @property
    def conditions(self):
        return self.hour_condition and self.check_condition

    @property
    def ranking(self):
        if not self.conditions:
            return -1
        else:
            return 1 + len([p for p in Patrol.objects.all() if p.conditions == True and p.total_score > self.total_score])


class Test(models.Model):

    patrol = models.ForeignKey(Patrol, related_name='tests')
    technique = models.ForeignKey(Technique, related_name='tests')

    technique_score = models.IntegerField(validators=[validate_score])
    style_score = models.IntegerField(validators=[validate_score])

    created_date = models.DateTimeField(auto_now_add=True, default=now)
    modified_date = models.DateTimeField(auto_now=True, default=now)
    user = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ('-created_date',)
        unique_together = ('patrol', 'technique')

    def __unicode__(self):
        return "%s --- %s --- %s" % (
            self.patrol, self.technique.name, self.created_date_hms
        )

    @property
    def created_date_hms(self):
        return "{0:%X}".format(localtime(self.created_date))

    @property
    def modified_date_hms(self):
        return "{0:%X}".format(localtime(self.modified_date))
