from wtforms import BooleanField, FileField, SelectField, StringField, TextAreaField
from wtforms.fields.html5 import IntegerField, URLField
from wtforms.widgets.html5 import NumberInput

from CTFd.constants.config import (
    AccountVisibilityTypes,
    ChallengeVisibilityTypes,
    RegistrationVisibilityTypes,
    ScoreVisibilityTypes,
)
from CTFd.constants.languages import SELECT_LANGUAGE_LIST
from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.utils.csv import get_dumpable_tables


class ResetInstanceForm(BaseForm):
    accounts = BooleanField(
        "حساب‌ها",
        description="تمام حساب‌های کاربری و تیمی و اطلاعات مرتبط با آنها را حذف می‌کند.",
    )
    submissions = BooleanField(
        "ارسال‌ها",
        description="تمام رکوردهایی که حساب‌ها امتیاز کسب کرده‌اند یا اقدامی انجام داده‌اند را حذف می‌کند",
    )
    challenges = BooleanField(
        "چالش‌ها", description="تمام چالش‌ها و داده‌های مرتبط را حذف می‌کند"
    )
    pages = BooleanField(
        "Pages", description="تمام صفحات و فایل‌های مرتبط با آنها را حذف می‌کند"
    )
    notifications = BooleanField(
        "اعلان‌ها", description="همه اعلان‌ها را حذف می‌کند"
    )
    submit = SubmitField("تنظیم مجدد CTF")


class AccountSettingsForm(BaseForm):
    domain_whitelist = StringField(
        "لیست مجاز دامنه ایمیل",
        description="فهرست دامنه‌های ایمیل مجاز که کاربران می‌توانند تحت آنها ثبت نام کنند (مثلاً examplectf.com، example.com، *.example.com) با کاما از هم جدا شده‌اند.",
    )
    domain_blacklist = StringField(
        "لیست مسدود شده دامنه ایمیل",
        description="فهرست جدا شده با کاما از دامنه‌های ایمیل غیرمجاز که کاربران نمی‌توانند تحت آنها ثبت نام کنند (مثلاً examplectf.com، example.com، *.example.com)",
    )
    team_creation = SelectField(
        "ایجاد تیم",
        description="کنترل اینکه آیا کاربران می‌توانند تیم‌های خود را ایجاد کنند یا خیر (فقط حالت تیم‌ها)",
        choices=[("true", "فعال‌شده"), ("false", "غیرفعا‌ل‌شده")],
        default="true",
    )
    team_size = IntegerField(
        widget=NumberInput(min=0),
        description="حداکثر تعداد کاربران در هر تیم (فقط حالت تیمی)",
    )
    num_teams = IntegerField(
        "حداکثر تعداد تیم‌ها",
        widget=NumberInput(min=0),
        description="حداکثر تعداد تیم‌های مجاز برای ثبت نام در این CTF (فقط در حالت تیمی)",
    )
    num_users = IntegerField(
        "حداکثر تعداد کاربران",
        widget=NumberInput(min=0),
        description="حداکثر تعداد حساب‌های کاربری مجاز برای ثبت نام در این CTF",
    )
    verify_emails = SelectField(
        "ایمیل‌ها را تأیید کنید",
        description="کنترل کنید که آیا کاربران قبل از بازی باید آدرس ایمیل خود را تأیید کنند یا خیر",
        choices=[("true", "فعال"), ("false", "غیرفعال")],
        default="false",
    )
    team_disbanding = SelectField(
        "انحلال تیم",
        description="کنترل کنید که آیا کاپیتان‌های تیم اجازه دارند تیم‌های خود را منحل کنند یا خیر",
        choices=[
            ("inactive_only", "برای تیم‌های غیرفعال فعال شده است"),
            ("disabled", "غیرفعال"),
        ],
        default="inactive_only",
    )
    name_changes = SelectField(
        "تغییر نام",
        description="کنترل اینکه آیا کاربران و تیم‌ها می‌توانند نام خود را تغییر دهند یا خیر",
        choices=[("true", "فعال"), ("false", "غیرفعال")],
        default="true",
    )
    incorrect_submissions_per_min = IntegerField(
        "ارسال‌های نادرست در هر دقیقه",
        widget=NumberInput(min=1),
        description="تعداد ارسال‌های مجاز در هر دقیقه برای محافظت در برابر حمله‌ی بروت‌فورس (پیش‌فرض: ۱۰)",
    )

    submit = SubmitField("به‌روز‌رسانی")


class ExportCSVForm(BaseForm):
    table = SelectField("جدول پایگاه داده", choices=get_dumpable_tables())
    submit = SubmitField("دانلود CSV")


class ImportCSVForm(BaseForm):
    csv_type = SelectField(
        "نوع CSV",
        choices=[("users", "کاربران"), ("teams", "تیم‌ها"), ("challenges", "چالش‌ها")],
        description="نوع دیتا csv",
    )
    csv_file = FileField("فایل CSV", description="محتوای فایل CSV")


class SocialSettingsForm(BaseForm):
    social_shares = SelectField(
        "اشتراک‌گذاری‌های اجتماعی",
        description="فعال یا غیرفعال کردن لینک‌های اشتراک‌گذاری اجتماعی برای حل چالش‌ها",
        choices=[("true", "فعال"), ("false", "غیرفعال")],
        default="true",
    )
    submit = SubmitField("به‌روز‌رسانی")


class LegalSettingsForm(BaseForm):
    tos_url = URLField(
        "آدرس اینترنتی شرایط خدمات",
        description="آدرس اینترنتی خارجی به سند شرایط خدمات که در جای دیگری میزبانی شده است",
    )
    tos_text = TextAreaField(
        "شرایط خدمات",
        description="متن نمایش داده شده در صفحه شرایط خدمات",
    )
    privacy_url = URLField(
        "آدرس اینترنتی سیاست حفظ حریم خصوصی",
        description="آدرس اینترنتی خارجی به یک سند سیاست حفظ حریم خصوصی که در جای دیگری میزبانی شده است",
    )
    privacy_text = TextAreaField(
        "سیاست حفظ حریم خصوصی",
        description="متن نمایش داده شده در صفحه سیاست حفظ حریم خصوصی",
    )
    submit = SubmitField("به‌روز رسانی")


class VisibilitySettingsForm(BaseForm):
    challenge_visibility = SelectField(
        "دیده‌شدن چالش‌ها",
        description="کنترل کنید که آیا کاربران برای دیدن چالش‌ها باید وارد سیستم شوند یا خیر",
        choices=[
            (ChallengeVisibilityTypes.PUBLIC, "عمومی"),
            (ChallengeVisibilityTypes.PRIVATE, "خصوصی"),
            (ChallengeVisibilityTypes.ADMINS, "فقط ادمین‌ها "),
        ],
        default=ChallengeVisibilityTypes.PRIVATE,
    )
    account_visibility = SelectField(
        "قابلیت دیده شدن اکانت",
        description="کنترل کنید که آیا حساب‌ها (کاربران و تیم‌ها) به همه، فقط به کاربران احراز هویت شده یا فقط به مدیران نمایش داده شوند",
        choices=[
            (AccountVisibilityTypes.PUBLIC, "عمومی"),
            (AccountVisibilityTypes.PRIVATE, "خصوصی"),
            (AccountVisibilityTypes.ADMINS, "فقط ادمین‌ها"),
        ],
        default=AccountVisibilityTypes.PUBLIC,
    )
    score_visibility = SelectField(
        "قابلیت دیدن امتیازات",
        description="کنترل کنید که آیا حل‌ها/امتیازات برای عموم نمایش داده شود، برای کاربران وارد شده، برای همه غیر مدیران پنهان باشد، یا فقط برای مدیران نمایش داده شود",
        choices=[
            (ScoreVisibilityTypes.PUBLIC, "عمومی"),
            (ScoreVisibilityTypes.PRIVATE, "خصوصی"),
            (ScoreVisibilityTypes.HIDDEN, "پنهان"),
            (ScoreVisibilityTypes.ADMINS, "فقط ادمین‌ها "),
        ],
        default=ScoreVisibilityTypes.PUBLIC,
    )
    registration_visibility = SelectField(
        "دیده‌شدن ثبت‌نام‌ها",
        description="کنترل کنید که آیا ثبت نام برای همه فعال است یا غیرفعال",
        choices=[
            (RegistrationVisibilityTypes.PUBLIC, "عمومی"),
            (RegistrationVisibilityTypes.PRIVATE, "خصوصی"),
            (RegistrationVisibilityTypes.MLC, "MajorLeagueCyber فقط"),
        ],
        default=RegistrationVisibilityTypes.PUBLIC,
    )


class LocalizationForm(BaseForm):
    default_locale = SelectField(
        "زبان پیشفرض",
        description="زبانی که در صورت عدم تعیین زبان توسط کاربر در تنظیمات حساب کاربری، مورد استفاده قرار می‌گیرد. به طور پیش‌فرض، CTFd به طور خودکار زبان مورد نظر کاربر را تشخیص می‌دهد.",
        choices=SELECT_LANGUAGE_LIST,
    )
