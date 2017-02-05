from django.shortcuts import render
from generator import forms

def show_base_template(request):
    base_invoice_form = forms.BaseInvoiceForm(request.POST or None)
    return render(request, 'base.html', {'form': base_invoice_form})
