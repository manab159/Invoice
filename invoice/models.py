from django.db import models

# Create your models here.


class Invoice(models.Model) :
    id = models.IntegerField(blank=True,null=True)
    customer = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    invoice_number = models.AutoField(primary_key=True)
    total_quantity = models.FloatField(blank=True,null=True)
    total_amount = models.FloatField(blank = True,null = True)
    total_tax = models.FloatField(blank = True,null =True)

    def __str__(self):
        return str(self.customer)


class Invoice_Line(models.Model) :
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length = 50,blank=True,null =True)
    quantity = models.FloatField(blank=True,null=True)
    price_without_tax = models.FloatField(blank=True,null=True)
    tax_name = models.CharField(max_length=50,blank=True,null=True)
    tax_amount = models.FloatField(blank=True,null=True)
    line_total = models.FloatField(blank=True,null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


