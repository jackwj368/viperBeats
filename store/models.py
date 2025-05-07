from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    audio_file = models.FileField(upload_to='wavs/')

    def __str__(self):
        return self.title