from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, Imie, Nazwisko, Adres, Telefon, Email, Platnosc, Login):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not Email:
            raise ValueError('Users must have an email address')

        user = self.model(
            Imie=Imie,
            Nazwisko=Nazwisko,
            Adres=Adres,
            Telefon=Telefon,
            Email=Email,
            Platnosc=Platnosc,
            Login=Login,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, id_pracownika, imie, nazwisko, adres, telefon, zarobki, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            id_pracownika=id_pracownika,
            imie=imie,
            nazwisko=nazwisko,
            adres=adres,
            telefon=telefon,
            zarobki=zarobki,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin