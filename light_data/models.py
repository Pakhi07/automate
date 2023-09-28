from django.db import models

# Create your models here.
class Data(models.Model):
    eqip_name = models.CharField(max_length=100)
    volt = models.FloatField()
    state = models.BinaryField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.eqip_name
    