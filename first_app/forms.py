from django import forms
from django.core import validators
# widgets == field to html input
class contactform(forms.Form):
    name=forms.CharField(label='Full Name: ',help_text="Total length must be within 70 characters",required=False,widget=forms.Textarea(attrs={'id':'text_area','class':'class1 class2','placeholder':'Enter Your Name'}))
    # file=forms.FileField()
    email=forms.EmailField()
    # mark=forms.FloatField()
    # age=forms.IntegerField()
    # money=forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput)
    check=forms.BooleanField()
    brithday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICE=[('S','Small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)
    MULCHOICE=[('D','Dhaka'),('C','Chittagong'),('K','Khulna')]
    city=forms.MultipleChoiceField(choices=MULCHOICE,widget=forms.CheckboxSelectMultiple)

# class studentform(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname=self.cleaned_data['name']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name at least 10 Character")
    #     return valname
    # def clean_email(self):
    #     valemail=self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your Email Must Contain .com")
    #     return valemail
    
    # def clean(self):
    #     cleaned_data =super().clean()
    #     valname=self.cleaned_data['name']
    #     valemail=self.cleaned_data['email']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name at least 10 Character")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your Email Must Contain .com")
       
# builtin Function for validation check   
def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("Enter  a Value atleast 10 Char")
# python builtin validation function
class studentform(forms.Form):
    name=forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,
    message="Enter a name at least 10 Character")])
    text=forms.CharField(widget=forms.TextInput,validators=[len_check])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Enter a valid Email")])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message='Age must be max 34'),validators.MinValueValidator(24,message='age more than 24')])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message='File Extention must be pdf and png')])


class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name=self.cleaned_data['name']
        if val_pass != val_conpass:
            raise forms.ValidationError("Password is not match")
        if len(val_name)<10:
            raise forms.ValidationError("Name Must be atleast 10 char")

