from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11)
    address = forms.CharField(max_length=200)


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField()
    image = forms.ImageField()
