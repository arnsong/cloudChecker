from django import forms
from cloudCheck import models

class CloudForm(forms.Form):
    
    cloud_classification = forms.ChoiceField(label='Cloud classification', 
                                             widget=forms.Select, choices=models.CLOUDCOVER_CLASSIFICATION)
    cloud_comments = forms.CharField(max_length=140, widget=forms.Textarea(attrs={'cols':45, 
                                                                                  'rows': 4,}))

    class Meta:
        model = models.Image
        field = [ 'isCloudy' ]
