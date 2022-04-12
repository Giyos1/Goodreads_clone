from django import forms
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
# class UserCreateForm(forms.Form):
#     username = forms.CharField(max_length=200)
#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     email = forms.EmailField(max_length=200)
#     password = forms.CharField(max_length=120)
#
#     def save(self):
#         username = self.cleaned_data.get('username')
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#
#         user = User.objects.create(
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#         )
#
#         user.set_password(password)
#         user.save()
