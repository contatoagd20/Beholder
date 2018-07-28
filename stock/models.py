from django.db import models
from django.utils import timezone

class Cathegory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Size(models.Model):
    height = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=200)
    cathegorys = models.ManyToManyField(
        Cathegory,
        through = 'CathegorySize',
        through_fields=('size','cathegory'),
    )

    def __str__(self):
        return self.name
    

class CathegorySize(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    cathegory = models.ForeignKey(Cathegory, on_delete=models.CASCADE)

class RawMaterial(models.Model):
    name = models.CharField(max_length=200)
    cathegorys = models.ManyToManyField(
        Cathegory,
        through = 'CathegoryRawMaterial',
        through_fields=('raw_material','cathegory'),
    ) 

    def __str__(self):
        return self.name

class CathegoryRawMaterial(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    cathegory = models.ForeignKey(Cathegory, on_delete=models.CASCADE)

class Color(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now)
    cathegory = models.ForeignKey(Cathegory, on_delete=models.CASCADE)
    colors = models.ManyToManyField(
        Color,
        through = 'ProductColor',
        through_fields=('product','color'),
    )

    def __str__(self):
        return self.name
        
class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    alert_quantity = models.IntegerField()
