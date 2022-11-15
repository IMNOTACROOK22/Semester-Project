from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    percentDiscount = models.DecimalField(default=0.0, max_digits = 2, decimal_places=2)

    def __str__(self):
        return self.code