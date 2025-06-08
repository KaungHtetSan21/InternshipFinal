from django import forms
from .models import*




class MedicineModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','disease','item_photo', 'item_name', 'item_quatity','item_price','item_description','exp_date']


class DiseaseModelForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['item_photo', 'disease_name', 'disease_symptom']