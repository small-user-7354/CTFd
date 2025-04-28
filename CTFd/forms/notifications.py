from wtforms import BooleanField, RadioField, StringField, TextAreaField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField


class NotificationForm(BaseForm):
    title = StringField("عنوان", description="عنوان نوتیفیکیشن")
    content = TextAreaField(
        "محتوا",
        description="محتوای نوتیفیکیشن",
    )
    type = RadioField(
        "نوع نوتیفیکیشن",
        # "Notification Type",
        choices=[("toast", "Toast"), ("alert", "Alert"), ("background", "Background")],
        default="toast",
        description="کاربران چه نوع نوتیفیکیشن را دریافت کنند",
        # "What type of notification should users receive",
        validators=[InputRequired()],
    )
    sound = BooleanField(
        "صدادار",
        default=True,
        description="کاربران صدای نوتیفیکیشن را بشنوند",
        # "Should users hear a sound for the notification",
    )
    submit = SubmitField("ارسال", description="ارسال نوتیفیکیشن")
