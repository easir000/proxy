from django import forms

class URLForm(forms.Form):
    
    
    url_1 = forms.URLField(label='Enter URL', required=True, initial='https://', widget=forms.TextInput(attrs={'pattern': 'https://.*', 'title': 'Please enter a URL starting with "https://"'}))
    url_2 = forms.URLField(label='Enter URL', required=True, initial='https://', widget=forms.TextInput(attrs={'pattern': 'https://.*', 'title': 'Please enter a URL starting with "https://"'}))
    url_3 = forms.URLField(label='Enter URL', required=True, initial='https://', widget=forms.TextInput(attrs={'pattern': 'https://.*', 'title': 'Please enter a URL starting with "https://"'}))
