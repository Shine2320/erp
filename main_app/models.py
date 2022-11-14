from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users require an email field")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


# class Permission(models.Model):
#     ACCOUNTS = 0
#     HR = 1
#     SALES = 2
#     PURCHASE = 3
#     REPORTS = 4
#     PERMISSIONS = (
#         (ACCOUNTS, "accounts"),
#         (HR, "hr"),
#         (SALES, "sales"),
#         (PURCHASE, "purchase"),
#         (REPORTS, "reports"),
#     )
#     permission = models.SmallIntegerField(choices=PERMISSIONS, null=True, blank=True)

#     def __str__(self):
#         return f"{self.get_permission_display()}"


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    objects = UserManager()
    accounts = models.BooleanField(default=False)
    hr = models.BooleanField(default=False)
    sales = models.BooleanField(default=False)
    purchase = models.BooleanField(default=False)
    reports = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

