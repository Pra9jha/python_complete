from django.db import models

# Create your models here.

class product(models.Model) :
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2,max_digits=1000)
    description =models.TextField(blank=True, null=True)
    summary=models.TextField()
    featured=models.BooleanField()

    # def __str__(self):
    #     return self.title
    #


