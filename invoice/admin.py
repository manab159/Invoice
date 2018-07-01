from django.contrib import admin
from .models import Invoice, Invoice_Line
# Register your models here.

class CustInvoice(admin.ModelAdmin):
    list_display = ('id' ,'customer' ,'date','invoice_number','total_quantity','total_amount','total_tax')
    readonly_fields = ('id','customer','date')


admin.site.register(Invoice,CustInvoice)
admin.site.register(Invoice_Line)