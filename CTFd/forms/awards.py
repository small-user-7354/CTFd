from wtforms import RadioField, StringField, TextAreaField
from wtforms.fields.html5 import IntegerField

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField


class AwardCreationForm(BaseForm):
    name = StringField("نام")
    value = IntegerField("مقدار")
    category = StringField("کتگوری")
    description = TextAreaField("توضیحات")
    submit = SubmitField("ساختن")
    icon = RadioField(
        "Icon",
        choices=[
            ("", "None"),
            ("shield", "Shield"),
            ("bug", "Bug"),
            ("crown", "Crown"),
            ("crosshairs", "Crosshairs"),
            ("ban", "Ban"),
            ("lightning", "Lightning"),
            ("skull", "Skull"),
            ("brain", "Brain"),
            ("code", "Code"),
            ("cowboy", "Cowboy"),
            ("angry", "Angry"),
        ],
    )
