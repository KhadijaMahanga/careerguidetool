from django import forms

Gender_Options = [('', 'Select Gender'),('F', 'Female'), ('M', 'Male'),]
Region_Options = [('', 'Select Region'),('Mwanza', 'Mwanza'),('Arusha','Arusha'),('DAR ES SALAAM','DAR ES SALAAM'),('Dodoma','Dodoma'),
('Singida','Singida'),
('Mtwara','Mtwara'),
('Mara','Mara'),
('Morogoro','Morogoro'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),]
Career_Options = [('Doctor', 'Doctor'), ('Pilot', 'Pilot')]

class InputForm(forms.Form):
    gender = forms.CharField(label='gender', widget=forms.Select(choices=Gender_Options), required=False)
    region = forms.ChoiceField(label='region', choices=Region_Options, required=False)
    career = forms.CharField(label='career', widget=forms.Select(choices=Career_Options), required=True)
