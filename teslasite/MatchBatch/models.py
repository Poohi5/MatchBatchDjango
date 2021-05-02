from django.db import models

class optimized_pair(models.Model):
    vin = models.CharField(max_length=50)
    rn = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.vin} {self.rn}"


