from django import forms
from django.forms.formsets import formset_factory

class CompanyInfoForm(forms.Form):
	company_name = forms.CharField(label="Company Name")
	company_street_address = forms.CharField(label="Street address")
	company_city = forms.CharField(label="City", help_text="City, ST, ZIP")
	company_region = forms.CharField(label="Region", help_text="Region, State, Province")
	company_country = forms.CharField(label="Country")
	company_phone = forms.CharField(label="Phone")


class ItemForm(forms.Form):
    product_name = forms.CharField(max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Product name',}
            ), required=False)
    quantity = forms.IntegerField(min_value=0)
    unit_price = forms.DecimalField(min_value=0)

ItemFormSet = formset_factory(ItemForm)

class BaseInvoiceForm(forms.Form):
    logo = forms.ImageField(label="Your logo")
    name = forms.CharField(label="Title", initial="INVOICE")
    invoice_no = forms.IntegerField(label="Invoice no", min_value=0, initial=0)
    date = forms.DateField(input_formats='%d/%m/%Y')
