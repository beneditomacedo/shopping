from django.db import models

class Store(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address

class Order(models.Model):
    date = models.DateField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    number = models.IntegerField()
    serie = models.IntegerField()
    key = models.CharField(max_length=44)
    quantity_items = models.IntegerField()
    value = models.DecimalField(decimal_places=2,max_digits=11)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.key

class Item(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=255)
    value = models.DecimalField(decimal_places=2,max_digits=11)
    total_value = models.DecimalField(decimal_places=2,max_digits=11)

    def __str__(self):
        return self.description