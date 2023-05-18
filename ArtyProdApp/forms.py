from django.forms import ModelForm
from .models import Project, Contact, Services
from django import forms
from django.contrib.admin import widgets

class ProjectForm(ModelForm): 
    end_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            selected_services = instance.service.all()
            self.initial['service'] = ', '.join(str(service) for service in selected_services)

    def save(self, commit=True):
        instance = super().save(commit=False)
        service_names = self.cleaned_data.get('service')
        # Perform any necessary processing with service_names
        instance.save()
        self.save_m2m()
        return instance
    
    class Meta : 
        model = Project 
        fields = ['label', 'service', 'description', 'end_date']
        labels = {
            'label' : 'Label', 
            'service' : 'Service',
            'description' : 'Description', 
            'end_date' : 'End Date', 
        } 
        widgets = {
            'label' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the label of your project here'}), 
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the description of your project here'}),
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'text']
        labels = {
            'subject': 'Subject',
            'text': 'Message',
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the subject of your message here'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content of your message here'}),
        }
        