from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

import uuid

class CustomUser(AbstractBaseUser, PermissionsMixin):

    username_validator  = UnicodeUsernameValidator()

    id          = models.UUIDField( default=uuid.uuid4, primary_key=True, editable=False )
    username    = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists.")
        },
    )

    handle_name = models.CharField(verbose_name="氏名", max_length=150) # 未入力可にするなら blank=True を追加

    email       = models.EmailField(_("email address"))

    is_staff    = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site.")
    )

    is_active   = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    is_teacher  = models.BooleanField(verbose_name="講師", default=False)
    is_student  = models.BooleanField(verbose_name="生徒", default=True)

    icon            = models.ImageField(verbose_name="アイコン", upload_to="users/custom_user/icon/", null=True, blank=True)
    introduction    = models.CharField(verbose_name="自己紹介文", max_length=1000, null=True, blank=True)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects     = UserManager()

    EMAIL_FIELD     = "email"
    USERNAME_FIELD  = "username"
    REQUIRED_FIELDS = ["email", "handle_name"] # createsuperuserしたときに入力を求められる項目を設定。デフォルトでusernameは入っている。

    class Meta:
        verbose_name        = _("user")
        verbose_name_plural = _("users")
        #abstract            = True

    def clean(self):
        super().clean()
        self.email  = self.__class__.objects.normalize_email(self.email)
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        return self.handle_name
    
    def get_short_name(self):
        return self.handle_name

    def __str__(self):
        return self.handle_name



