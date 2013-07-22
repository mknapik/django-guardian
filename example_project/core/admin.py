from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from guardian.admin import GuardedModelAdmin
from models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
        model = CustomUser


class CustomUserAdmin(GuardedModelAdmin, UserAdmin):
    add_form = CustomUserCreationForm


admin.site.register(CustomUser, CustomUserAdmin)
