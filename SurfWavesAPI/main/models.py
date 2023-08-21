from django.db import models
import json


# Create your models here.

# Dewata Waves Forcats History
class DewataItem(models.Model):
    surfspot = models.CharField(max_length=20, default='Dewata')
    date = models.DateField(auto_now=True)
    time = models.CharField(max_length=20, default='08:30 AM')
    swell1_height = models.DecimalField(max_digits=4, decimal_places=2)
    swell1_period = models.PositiveIntegerField()
    swell2_height = models.DecimalField(max_digits=4, decimal_places=2)
    swell2_period = models.PositiveIntegerField()
    swell3_height = models.DecimalField(max_digits=4, decimal_places=2)
    swell3_period = models.PositiveIntegerField()

    @property
    def to_dict(self):
        data = {
            'surfspot': json.loads(self.surfspot),
            'date': json.loads(self.date),
            'time': json.loads(self.time),
            'swell1_height': {
                'value': json.loads(self.swell1_height),
                'unit': 'meter'},
            'swell1_period': {
                'value': json.loads(self.swell1_period),
                'unit': 'second'},
            'swell2_height': {
                'value': json.loads(self.swell2_height),
                'unit': 'meter'},
            'swell2_period': {
                'value': json.loads(self.swell2_period),
                'unit': 'second'},
            'swell3_height': {
                'value': json.loads(self.swell3_height),
                'unit': 'meter'},
            'swell3_period': {
                'value': json.loads(self.swell3_period),
                'unit': 'second'}
        }
        return data

    def __str__(self):
        return f'{self.id}: {self.surfspot} {self.swell1_height} {self.swell1_period}'
