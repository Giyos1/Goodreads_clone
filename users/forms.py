from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    re_password = forms.CharField(max_length=120)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        """
        clean data overide
        """

        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Usernameli foydalanuvchi mavjud')
        if not password.__eq__(re_password):
            raise forms.ValidationError('not match.')
        return self.cleaned_data

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
#     re_password = forms.CharField(max_length=120)
#
#     def clean(self):
#         """
#         clean data overide
#         """
#
#         password = self.cleaned_data['password']
#         re_password = self.cleaned_data['re_password']
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username):
#             raise forms.ValidationError('Usernameli foydalanuvchi mavjud')
#         if not password.__eq__(re_password):
#             raise forms.ValidationError('not match.')
#         return self.cleaned_data
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


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if username is not None and password:
            user = authenticate(
                self.request, username=username, password=password
            )
            if user is None:
                raise forms.ValidationError('mavjud emas')

            if not user.is_active:
                raise forms.ValidationError('vaqti tugagan')

        return self.cleaned_data

    def get_user(self):
        return self.user
