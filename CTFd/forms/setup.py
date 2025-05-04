from flask_babel import lazy_gettext as _l
from wtforms import (
    FileField,
    HiddenField,
    IntegerField,
    PasswordField,
    RadioField,
    SelectField,
    StringField,
    TextAreaField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired
from wtforms.widgets.html5 import NumberInput

from CTFd.constants.config import (
    AccountVisibilityTypes,
    ChallengeVisibilityTypes,
    RegistrationVisibilityTypes,
    ScoreVisibilityTypes,
)
from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.utils.config import get_themes


class SetupForm(BaseForm):
    ctf_name = StringField(
        _l("Event Name"), description=_l("The name of your CTF event/workshop")
    )
    ctf_description = TextAreaField(
        _l("Event Description"), description=_l("Description for the CTF")
    )
    user_mode = RadioField(
        _l("User Mode"),
        choices=[("teams", _l("Team Mode")), ("users", _l("User Mode"))],
        default="teams",
        description=_l(
            "Controls whether users join together in teams to play (Team Mode) or play as themselves (User Mode)"
        ),
        validators=[InputRequired()],
    )

    name = StringField(
        _l("Admin Username"),
        description=_l("Your username for the administration account"),
        validators=[InputRequired()],
    )
    email = EmailField(
        _l("Admin Email"),
        description=_l("Your email address for the administration account"),
        validators=[InputRequired()],
    )
    password = PasswordField(
        _l("Admin Password"),
        description=_l("Your password for the administration account"),
        validators=[InputRequired()],
    )

    ctf_logo = FileField(
        _l("Logo"),
        description=_l(
            "Logo to use for the website instead of a CTF name. Used as the home page button. Optional."
        ),
    )
    ctf_banner = FileField(
        _l("Banner"), description=_l("Banner to use for the homepage. Optional.")
    )
    ctf_small_icon = FileField(
        _l("Small Icon"),
        description=_l(
            "favicon used in user's browsers. Only PNGs accepted. Must be 32x32px. Optional."
        ),
    )
    ctf_theme = SelectField(
        _l("Theme"),
        description=_l("CTFd Theme to use. Can be changed later."),
        choices=list(zip(get_themes(), get_themes())),
        ## TODO: Replace back to DEFAULT_THEME (aka core) in CTFd 4.0
        default="core-beta",
        validators=[InputRequired()],
    )
    theme_color = HiddenField(
        _l("Theme Color"),
        description=_l(
            "Color used by theme to control aesthetics. Requires theme support. Optional."
        ),
    )

    verify_emails = SelectField(
        _l("تایید ایمیل"),
        description="کنترل کنید که آیا کاربران قبل از شرکت در نظرسنجی باید آدرس ایمیل خود را تأیید کنند یا خیر",
        choices=[("true", "فعال"), ("false", "غیرفعال")],
        default="false",
    )
    team_size = IntegerField(
        widget=NumberInput(min=0),
        description="تعداد کاربران در هر تیم (فقط حالت تیمی) اختیاری.",
    )
    challenge_visibility = SelectField(
        "قابلیت دیده‌شدن چالش",
        description="کنترل کنید که آیا کاربران برای دیدن چالش‌ها باید وارد سیستم شوند یا خیر",
        choices=[
            (ChallengeVisibilityTypes.PUBLIC, "عمومی"),
            (ChallengeVisibilityTypes.PRIVATE, "خصوصی"),
            (ChallengeVisibilityTypes.ADMINS, "فقط ادمین‌ها"),
        ],
        default=ChallengeVisibilityTypes.PRIVATE,
    )
    account_visibility = SelectField(
        "قابلیت دیده‌شدن حساب",
        description="کنترل کنید که آیا حساب‌ها (کاربران و تیم‌ها) به همه، فقط به کاربران احراز هویت شده یا فقط به مدیران نمایش داده شوند.",
        choices=[
            (AccountVisibilityTypes.PUBLIC, "عمومی"),
            (AccountVisibilityTypes.PRIVATE, "خصوصی"),
            (AccountVisibilityTypes.ADMINS, "فقط ادمین‌ها"),
        ],
        default=AccountVisibilityTypes.PUBLIC,
    )
    score_visibility = SelectField(
        "قابلیت مشاهده امتیاز",
        description="کنترل کنید که آیا حل‌ها/امتیازات برای عموم نمایش داده شود، برای کاربران وارد شده، برای همه غیر مدیران پنهان باشد، یا فقط برای مدیران نمایش داده شود",
        choices=[
            (ScoreVisibilityTypes.PUBLIC, "عمومی"),
            (ScoreVisibilityTypes.PRIVATE, "خصوصی"),
            (ScoreVisibilityTypes.HIDDEN, "پنهان"),
            (ScoreVisibilityTypes.ADMINS, "فقط ادمین‌ها"),
        ],
        default=AccountVisibilityTypes.PUBLIC,
    )
    registration_visibility = SelectField(
        "قابلیت مشاهده ثبت نام",
        description="کنترل کنید که آیا ثبت نام برای همه فعال است یا غیرفعال",
        choices=[
            (RegistrationVisibilityTypes.PUBLIC, "عمومی"),
            (RegistrationVisibilityTypes.PRIVATE, "خصوصی"),
            (RegistrationVisibilityTypes.MLC, "MajorLeagueCyber فقط"),
        ],
        default=RegistrationVisibilityTypes.PUBLIC,
    )

    start = StringField(
        _l("زمان شروع"),
        description=_l("زمان شروع CTF شما (اختیاری)"),
    )
    end = StringField(
        _l("زمان پایان"),
        description=_l("زمان پایان CTF شما (اختیاری)"),
    )
    submit = SubmitField(_l("Finish"))
