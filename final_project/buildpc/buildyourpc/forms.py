from django import forms
from .models import *


class ComputerForm(forms.ModelForm):
    ram_memory = forms.ModelMultipleChoiceField(queryset=MemoryRAM.objects.all())
    storage = forms.ModelMultipleChoiceField(queryset=Storage.objects.all())

    class Meta:
        model = Computer
        exclude = ['ram_quantity', 'storage_quantity']
