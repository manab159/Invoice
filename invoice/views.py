from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from invoice.models import Invoice,Invoice_Line
import requests
# Create your views here.
from django.core import serializers

def fetch_data(request):
    if request.method == 'GET' :
        invoice_obj = Invoice_Line.objects.all()
        print(invoice_obj)
        invoice_json = serializers.serialize('json', invoice_obj)
        return JsonResponse(invoice_json,safe=True)
        #return HttpResponse(invoice_json, content_type='application/json')

    if request.method == 'POST' :
        r = requests.get('http://127.0.0.1/invoices/')
        request_dict = r.json()
        invoice_obj = Invoice.objects.get(customer = request_dict['customer'])
        invoice_line_obj = Invoice_Line.objects.get(product = request_dict['product'],quantity=request_dict['quantity']
                                                    ,price_without_tax = float(request_dict['price_without_tax']),
                                                    tax_name=request_dict['tax_name'],tax_amount=request_dict['tax_amount'],
                                                    )



    # if request.method == 'POST':
    #     pass
