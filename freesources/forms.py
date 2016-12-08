from django import forms
from datetime import datetime
from django.db import connection

EXP_TYPE = (
	('Temporary', 'Temporary'),
	('Permanent', 'Permanent'),
	('Recurrent', 'Recurrent'),
)
TAG_ID = (
	('1', 'AED'),
	('2', 'Free Food'),
	('3', 'Event'),
	('4', 'Restroom'),
	('5', 'Vaccines'),
	('6', 'Health Check-ups'),
	('7', 'Water'),
)
class ItemForm(forms.Form):
    # tag_id = forms.ModelChoiceField(connection.cursor().execute("SELECT tag_id FROM Tag"))
    tag_name = forms.ChoiceField(choices = TAG_ID,
                widget=forms.Select(attrs={'class':'form-control'}))
    expiration_type = forms.ChoiceField(choices = EXP_TYPE, 
                widget=forms.Select(attrs={'class':'form-control exp_type','id':'exp_type'}))
    latitude = forms.FloatField(required = False,
                widget=forms.HiddenInput(attrs={'class':'form-control lat' , 'id': 'lat'}))
    longitude = forms.FloatField(required = False,
                widget=forms.HiddenInput(attrs={'class':'form-control lng', 'id': 'lng'}))

    # tag = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=255)
    start_time = forms.DateTimeField(required = False,
                input_formats=['%Y-%m-%dT%H:%M'], 
                widget=forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local','id':'start_time'}),
                initial=datetime.now().time())
    #expiration = forms.DateTimeField(widget=forms.widgets.DateTimeInput(input_formats=["%d %b %Y %H:%M:%S %Z"]))
    expiration = forms.DateTimeField(required = False, input_formats=['%Y-%m-%dT%H:%M'],widget=forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local','id':'expiration'}),initial=datetime.now().time())
    description = forms.CharField(required = False, widget=forms.TextInput(attrs={'class':'form-control'}),max_length=1024)
    location = forms.CharField(required = False, widget=forms.TextInput(attrs={'class':'form-control location', 'id': 'location'}),max_length=255)

class ItemFormMark(forms.Form):
    # tag_id = forms.ModelChoiceField(connection.cursor().execute("SELECT tag_id FROM Tag"))
    tag_name = forms.ChoiceField(choices = TAG_ID, widget=forms.Select(attrs={'class':'form-control'}))
    expiration_type = forms.ChoiceField(choices = EXP_TYPE, widget=forms.Select(attrs={'class':'form-control exp_type_mark','id':'exp_type_mark'}))
    latitude = forms.FloatField(required = False, widget=forms.HiddenInput(attrs={'class':'form-control lat_mark' , 'id': 'lat_mark'}))
    longitude = forms.FloatField(required = False, widget=forms.HiddenInput(attrs={'class':'form-control lng_mark', 'id': 'lng_mark'}))

    # tag = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=255)
    start_time = forms.DateTimeField(required = False, input_formats=['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local','id':'start_time_mark'}),initial=datetime.now().time())
    #expiration = forms.DateTimeField(widget=forms.widgets.DateTimeInput(input_formats=["%d %b %Y %H:%M:%S %Z"]))
    expiration = forms.DateTimeField(required = False, input_formats=['%Y-%m-%dT%H:%M'],widget=forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local','id':'expiration_mark'}),initial=datetime.now().time())
    description = forms.CharField(required = False, widget=forms.TextInput(attrs={'class':'form-control'}),max_length=1024)
    location = forms.CharField(required = False, widget=forms.TextInput(attrs={'class':'form-control location_mark', 'id': 'location_mark'}),max_length=255)

class TagSuggestion(forms.Form):
    tag_title = forms.CharField(required = False, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'tag_name'}),max_length=225)
    tag_description = forms.CharField(required = False, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'tag_description'}),max_length=225)
