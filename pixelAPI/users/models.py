from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.mail import send_mail
import re
from django.utils.translation import ugettext_lazy as _

#TODO: Add some extra fields and create CustomUserManager.

class MyUserManager(BaseUserManager):
    """
        My User Manager, Do Not Forget To Add New Fields Here
    """
    use_in_migrations = True
    def _create_user(self, username, first_name, last_name, email, date_birthday, usernumber, password, **extra):
        reqValues = [email, first_name, last_name, date_birthday]
        field_val = dict(zip(self.model.REQUIRED_FIELDS, reqValues))
        for field_name, value in field_val.items():
            if not value:
                raise ValueError('The {value} must be set.')
        if not username:
            raise ValueError('The username must be set.')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_birthday=date_birthday,
            usernumber=usernumber,
            last_login=timezone.now(),
            **extra
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, first_name, last_name, email, date_birthday, usernumber, password, **extra):
        extra.setdefault('is_staff', False)
        extra.setdefault('is_admin', False)
        return self._create_user(username, first_name, last_name, email, date_birthday, usernumber, password, **extra)


    def create_superuser(self, username, first_name, last_name, email, date_birthday, usernumber, password, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_admin', True)
        if extra.get('is_staff') is not True:
            raise ValueError('Superuser must have is_stuff = True.')
        if extra.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin = True')
        return self._create_user(username, first_name, last_name, email, date_birthday, usernumber, password, **extra)

    def create_stuff(self, username, first_name, last_name, email, date_birthday, usernumber, password, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_admin', False)
        if extra.get('is_staff') is not True:
            raise ValueError('Stuff member must have is_stuff = True.')
        return self._create_user(username, first_name, last_name, email, date_birthday, usernumber, password, **extra)


class User(AbstractBaseUser, PermissionsMixin):
    #FIELDS
    username = models.CharField(verbose_name='Username', max_length=40, unique=True, validators=[RegexValidator(regex=r'^[a-z]\w+', message=_('Wrong Username, Try Again.[Max Length: 40 characters, Must Start With: 4 Characters, Allowed: Alphanumeric, Underscore]'), code='invalid_username', flags=re.IGNORECASE)])
    usernumber = models.CharField(verbose_name="Telephone Number", max_length=15, unique=True, validators=[RegexValidator(regex=r'^\+[0-9]{4,15}$', message=_('Calling Code Required[EX: +44]  And Up to 15 digits'), code='invalid')], blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=150, validators=[RegexValidator(regex=r'^[a-z][a-z]+$', message=_('Wrong Name, Try Again.[Max Length: 150 characters, Must Have At Least 2 characters.]'), code='invalid', flags=re.IGNORECASE)])
    last_name = models.CharField(_('last name'), max_length=150, validators=[RegexValidator(regex=r'^[a-z][a-z]+$', message=_('Wrong Name, Try Again.[Max Length: 150 characters, Must Have At Least 2 characters.]'), code='invalid', flags=re.IGNORECASE)])
    email = models.EmailField(_('email address'))
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_admin = models.BooleanField(default=False);
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now, editable=False)
    date_birthday = models.DateField(verbose_name=_('Date Of Birth'), default='1900-01-01')

    last_login = models.DateTimeField(_('last login.'), null=True, blank=True)
    
    objects = MyUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'date_birthday', 'usernumber']
    #META
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    #METHODS

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staffMem(self):
        "Is the user a member of staff?"
        return self.is_staff

    def _str_(self):
        return f'Username: {self.username} Name: {self.name} Last Name: {self.last_name}'
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

# Create your models here.
