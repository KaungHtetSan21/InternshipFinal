from django import forms
from .models import*




class MedicineModelForm(forms.ModelForm):
    class Meta:
        model = Item
      
        fields = '__all__'
        widgets = {
        'category': forms.Select(attrs={'class': 'form-control'}),
        'disease': forms.Select(attrs={'class': 'form-control'}),
        'supplier': forms.Select(attrs={'class': 'form-control'}),  # ဒီထဲလည်းထည့်ဖို့လိုတယ်
        'item_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        'item_name': forms.TextInput(attrs={'class': 'form-control'}),
        'item_quatity': forms.NumberInput(attrs={'class': 'form-control'}),
        'item_price': forms.NumberInput(attrs={'class': 'form-control'}),
        'purchase_price': forms.NumberInput(attrs={'class': 'form-control'}),
        'item_description': forms.Textarea(attrs={'class': 'form-control'}),
        'exp_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    }


class DiseaseModelForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['item_photo', 'disease_name', 'disease_symptom']

class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'supplier_phnumber', 'supplier_location']

# forms.py

class StockInForm(forms.ModelForm):
    class Meta:
        model = StockHistory
        fields = ['item', 'supplier', 'quantity', 'note']  # ✅ Add supplier
        widgets = {
            'note': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'item': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.action = 'in'
        if commit:
            instance.save()
        return instance