from django import forms


class AddressForm(forms.form):
    address = forms.CharField(label='Shipping address',
                              widget=forms.Textarea(attrs={'class': 'form_control', 'rows': 3}), max_length=300)


