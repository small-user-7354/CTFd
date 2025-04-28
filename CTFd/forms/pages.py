from wtforms import (
    BooleanField,
    HiddenField,
    MultipleFileField,
    SelectField,
    StringField,
    TextAreaField,
)
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm


class PageEditForm(BaseForm):
    title = StringField(
        "عنوان", description="این عنوانی است که در نوار عنوان مرورگر شما نمایش داده می‌شود."
    )
    route = StringField(
        "مسیر",
        description="این آدرس URL است که در نوار آدرس مرورگر شما نمایش داده می‌شود.",
    )
    draft = BooleanField("درفت")
    hidden = BooleanField("پنهان")
    auth_required = BooleanField("احراز هویت لازم است")
    content = TextAreaField("Content")
    format = SelectField(
        "فرمت",
        choices=[("markdown", "Markdown"), ("html", "HTML")],
        default="markdown",
        validators=[InputRequired()],
        description="فرمت رندر صفحه را انتخاب کنید",
    )
    link_target = SelectField(
        "هدف",
        choices=[("", "صفحه کنونی"), ("_blank", "تب جدید")],
        default="",
        validators=[],
        description="کانتکست لینک را انتخاب کنید",
    )


class PageFilesUploadForm(BaseForm):
    file = MultipleFileField(
        "Upload Files",
        description="Attach multiple files using Control+Click or Cmd+Click.",
        validators=[InputRequired()],
    )
    type = HiddenField("Page Type", default="page", validators=[InputRequired()])
