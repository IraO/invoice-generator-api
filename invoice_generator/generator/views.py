from django.shortcuts import render, redirect
from generator import forms as generator_forms

def index(request):
    return redirect('home')

def home(request):
	return render(request, 'index.html', {})

def show_base_template(request):
    base_invoice_form = generator_forms.BaseInvoiceForm(request.POST or None)
    sender_company_form = generator_forms.CompanyInfoForm(request.POST or None)
    receiver_company_form = generator_forms.CompanyInfoForm(request.POST or None) 
    item_formset = generator_forms.ItemFormSet(request.POST or None)
    return render(request, 'generator/simple_template.html', {'base_form': base_invoice_form, 
    	'sender_company_form': sender_company_form, 'receiver_company_form': receiver_company_form,
    	'item_formset': item_formset})
