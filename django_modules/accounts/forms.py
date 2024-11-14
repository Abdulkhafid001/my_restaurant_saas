from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import NaijaKitchenUser


class NaijaKitchenUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = NaijaKitchenUser
        fields = UserCreationForm.Meta.fields + ("name",)


class NaijaKitchenUserChangeForm(UserChangeForm):
    class Meta:
        model = NaijaKitchenUser
        fields = UserChangeForm.Meta.fields
