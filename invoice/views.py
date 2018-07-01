from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from invoice.models import Invoice,Invoice_Line
from django.db.models import Sum
from django.db import transaction
from django.core import serializers
import datetime

@transaction.atomic()
def fetch_data(request):
    if request.method == 'GET' :
        invoice_obj = Invoice.objects.all()
        print(invoice_obj)
        invoice_json = serializers.serialize('json', invoice_obj)
        return JsonResponse(invoice_json,safe=False)
        #return HttpResponse(invoice_json, content_type='application/json')

    if request.method == 'POST' :
        print(request.POST[''])
        # request_dict = r.json()
        try :
            if Invoice.objects.filter(customer = request.POST['customer']).exists():
                invoice_obj = Invoice.objects.get(customer = request.POST['customer'])
            else :
                invoice_obj = Invoice(customer = request.POST['customer'])

            invoice_line_obj = Invoice_Line.objects.get(product = request.POST['product'],quantity=request.POST['quantity']
                                                        ,price_without_tax = float(request.POST['price_without_tax']),
                                                        tax_name=request.POST['tax_name'],tax_amount=request.POST['tax_amount'],
                                                        line_total=request.POST['line_total'],invoice=invoice_obj)
            invoice_line_obj.save()
            invoice_obj.total_quantity = Invoice_Line.objects.aggregate(Sum('quantity'))['quantity__sum']
            invoice_obj.total_amount = Invoice_Line.objects.aggregate(Sum('line_total'))['line_total']
            invoice_obj.date = datetime.datetime.now()
            invoice_obj.save()
            return JsonResponse(invoice_obj,safe=False)
        except :
            error={'error' : 'invoice cannot be saved'}
            return JsonResponse(error,safe=False)

@transaction.atomic()
def fetch_invoice_data(request,id):

    if request.method=='GET' :
        if Invoice.objects.filter(id=id).exists():
            invoice_obj = Invoice.objects.filter(id=id)
            invoice_json = serializers.serialize('json', invoice_obj)
            return JsonResponse(invoice_json, safe=False)


    if request.method=='PUT' :
        if not Invoice_Line.objects.filter(invoice=id).exists():
            invoice_line_obj = Invoice_Line(invoice=id)
            invoice_line_obj.save()



    if request.method=='DELETE':
        if  Invoice.objects.filter(id=id).exists():
            Invoice.objects.get(id=id).delete()
            message = {'message' : 'Deleted Successfully'}
            return JsonResponse(message,safe=False)
        else :
            message = {'message' : 'ID Cannot be found'}
            return JsonResponse(message , safe=False)



