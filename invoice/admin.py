from django.contrib import admin
from .models import Invoice, Invoice_Line
# Register your models here.

# class CustInvoice(admin.ModelAdmin);
#     list_display = ('id' ,'customer' ,'date','invoice')


admin.site.register(Invoice)
admin.site.register(Invoice_Line)