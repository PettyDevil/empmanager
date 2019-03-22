from django import forms
from captcha.fields import CaptchaField
class RegisterForm(forms.Form):
    # error_messages包含验证码错误的信息的一个字典
    # 下面表示的是当输入的验证码不对，在浏览器显示“验证码错误”
    captcha = CaptchaField(label='验证码',error_messages={"invalid": "验证码错误"})
