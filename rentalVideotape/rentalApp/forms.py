from django import forms
from .models import Genre, Director, Status, Videotape, Rental
from phonenumber_field.modelfields import PhoneNumberField


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name',
                  'surname',
                  'age',
                  'date']
        widgets = {
            'date':
                forms.DateInput(attrs={'type': 'date'})
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class VideotapeForm(forms.ModelForm):
    class Meta:
        model = Videotape
        fields = ['title',
                  'released',
                  'genre',
                  'director',
                  'image',
                  'description',
                  'status']
        widgets = {
            'released':
                forms.DateInput(attrs={'type': 'date'})
        }


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['videotape',
                  'date_start',
                  'date_end',
                  'buyer_name',
                  'buyer_surname',
                  'buyer_email',
                  'buyer_phone']
        widgets = {
            'date_start':
                forms.DateInput(attrs={'type': 'date'}),
            'date_end':
                forms.DateInput(attrs={'type': 'date'}),
            'buyer_email':
                forms.EmailInput(attrs={'type': 'email'}),
        }
