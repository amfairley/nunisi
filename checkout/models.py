from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
