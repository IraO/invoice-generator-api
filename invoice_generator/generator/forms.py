from django import forms

class BaseInvoiceForm(forms.Form):
    logo = forms.ImageField(label="Your logo")
    name = forms.CharField(label="Title", initial="INVOICE")
    invoice_no = forms.IntegerField(label="Invoice no", min_value=0, initial=0)
