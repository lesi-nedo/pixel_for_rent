from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CreationUserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields='__all__'


class ChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields=('username', 'email', 'first_name', 'last_name', 'date_birthday', 'usernumber', )