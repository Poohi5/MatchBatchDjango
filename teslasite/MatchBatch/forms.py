from django import forms  
from .models import optimized_pair 

class MacthForm(forms.ModelForm):  
    class Meta:  
        model = optimized_pair  
        fields = ['vin', 'rn'] 
        widgets = { 'vin': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'rn': forms.TextInput(attrs={ 'class': 'form-control' }),
      }