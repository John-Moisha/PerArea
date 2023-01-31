from datetime import timezone

from django import forms
from django.core.files.images import get_image_dimensions
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404

from core import settings
from .models import Check, Verification
from apps.accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import *

class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = (
            'balance',
            'debt',
        )


class VerifAccountForms(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
        )


class VerificationForms(forms.ModelForm):
    error_css_class = 'is-invalid'

    # first_name = forms.CharField(label=_('Name'), widget=forms.TextInput())
    SexChoices = [
        ('U', _('сделайте свой выбор')),
        ('M', _('Мужской')),
        ('F', _('Женский')),
    ]

    sex = forms.CharField(
        label=_('Пол'),
        widget=forms.Select(
            choices=SexChoices,
            attrs={
                # "placeholder": "Сделайте свой выбор",
                "class": "form-control"
            }
        ))

    street_line = forms.CharField(
        label=_('Адресс'),
        widget=forms.TextInput(
            attrs={
                "placeholder": "Улица",
                "class": "form-control"
            }
        ))
    number = forms.CharField(
        label=_('Номер'),
        widget=forms.TextInput(
            attrs={
                "placeholder": "№",
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        label=_('Город'),
        widget=forms.TextInput(
            attrs={
                "placeholder": "Город",
                "class": "form-control"
            }
        ))
    state = forms.CharField(
        label=_('Область'),
        widget=forms.TextInput(
            attrs={
                "placeholder": "Область",
                "class": "form-select w-100 mb-0"
            }
        ))

    passport1 = forms.FileField(
        label="Паспорт 1 стр",
        # required=False,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'exe'],
                message=_('Разрешение файлов дожно быть JPG, JPEG, PNG')),
        ],
        widget=forms.FileInput(
            attrs={
                # "class": "file-field fileinput fileUpload form-control-file",
            }
        )
    )
    passport2 = forms.FileField(
        label="Паспорт 2 стр",
        required=False,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'exe'],
                message=_('Разрешение файлов дожно быть JPG, JPEG, PNG')),
        ],
        widget=forms.FileInput(
            attrs={
                # "class": "file-field fileinput fileUpload form-control-file",
            }
        )
    )
    zipcode = forms.CharField(
        label=_('Индекс'),
        min_length=4,
        max_length=7,
        validators=[RegexValidator(r'^[0-9]*$', message='Возможны только цифры')],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Индекс",
                "class": "form-control"
            }
        ))
    date_of_birth = forms.DateField(
        label=_('Дата рождения'),
        # DATE_FORMAT="d-m-Y",
        input_formats=settings.DATE_INPUT_FORMATS,
        # validators=[RegexValidator(r'^[0-9]*$', message='Возможны только цифры')],
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={
                "placeholder": "ДД-ММ-ГГГГ",
                'data-toggle': "datepicker",
                'class':'form-control',
                # "id": "datepicker"
            }
        ))
    # user = forms.TextInput(get_object_or_404(CustomUser, pk=self.request.user.id))

    class Meta:
        model = Verification
        # fields = '__all__'
        fields = (

            'date_of_birth',
            'sex',
            'street_line',
            'number',
            'city',
            "state",
            'zipcode',
            'passport1',
            'passport2')
        # fields = ('zipcode',)

        def clean_to_date(self):
            data = self.cleaned_data['date_of_birth']
            if data > timezone.now().date():
                raise forms.ValidationError("'to' date cannot be later than today.")
            return data


VerificationFormsSet = inlineformset_factory(
    CustomUser, Verification, form=VerificationForms,
    extra=2, can_delete=True, can_delete_extra=True
)

# class VerificationForms2(forms.ModelForm):
#
#     class Meta:
#         model = Verification
#         exclude = ()
#
# CollectionTitleFormSet = inlineformset_factory(
#     CustomUser, Verification, form=VerificationForms2,
#     fields=['date_of_birth',
#             'sex',
#             'street_line',
#             'number',
#             'city',
#             "state",
#             'zipcode',
#             'passport1',
#             'passport2'],
#     extra=1, can_delete=True
#     )
# ProductMetaInlineFormset = inlineformset_factory(
#     CustomUser,
#     Verification,
#     form=VerificationForms,
#     extra=10,
#     # max_num=5,
#     # fk_name=None,
#     # fields=None, exclude=None, can_order=False,
#     # can_delete=True, max_num=None, formfield_callback=None,
#     # widgets=None, validate_max=False, localized_fields=None,
#     # labels=None, help_texts=None, error_messages=None,
#     # min_num=None, validate_min=False, field_classes=None
# )

        # def save(self, commit=True):
        #     instance = super(VerificationForms, self).save(commit=False)
        #     # instance.user = self.user
        #     instance.user = super(VerifAccountForms, self)
        #     instance.zipcode = 'zipcode'
        #     if commit:
        #         instance.save()
        #     return instance


    # def __init__(self, user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.user = user

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     # instance.user = self.user
    #
    #     if commit:
    #         instance.save()
    #
    #     return instance
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     width, height = get_image_dimensions(self.cleaned_data.get('passport1'))
    #     if width < 400 or height < 400:
    #         raise forms.ValidationError("Image dimensions is too small, minimum is 1300x400")
    #     return cleaned_data


    # def clean(self, *args, **kwargs):
    #     cleaned_data = super().clean()
    #     passport_1 = cleaned_data.get('passport1')
    #     if not passport_1.is_valid():
    #         self.add_error('passport1', 'Ne validnya Forma')
    #     else:
    #         return cleaned_data
        # passport1 = cleaned_data.get('passport1')
        # if not passport1.is_valid():
        #     return forms.ValidationError('Not-Valid')
        # return passport1




# class CombinedFormBase(forms.Form):
#     form_classes = []
#
#     def __init__(self, *args, **kwargs):
#         super(CombinedFormBase, self).__init__(*args, **kwargs)
#         for f in self.form_classes:
#             name = f.__name__.lower()
#             setattr(self, name, f(*args, **kwargs))
#             form = getattr(self, name)
#             self.fields.update(form.fields)
#             self.initial.update(form.initial)
#
#     def is_valid(self):
#         isValid = True
#         for f in self.form_classes:
#             name = f.__name__.lower()
#             form = getattr(self, name)
#             if not form.is_valid():
#                 isValid = False
#         # is_valid will trigger clean method
#         # so it should be called after all other forms is_valid are called
#         # otherwise clean_data will be empty
#         if not super(CombinedFormBase, self).is_valid() :
#             isValid = False
#         for f in self.form_classes:
#             name = f.__name__.lower()
#             form = getattr(self, name)
#             self.errors.update(form.errors)
#         return isValid
#
#     def clean(self):
#         cleaned_data = super(CombinedFormBase, self).clean()
#         for f in self.form_classes:
#             name = f.__name__.lower()
#             form = getattr(self, name)
#             cleaned_data.update(form.cleaned_data)
#         return cleaned_data
