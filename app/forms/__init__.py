from flask_wtf import FlaskForm
from flask_login import LoginManager
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required

'''
Flask-WTF能保护所有表单免受跨站请求伪造（Cross-Site Request Forgery, CSRF）的攻击。
程序需设置一个密匙，在config中有参数。
'''

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'
login_manager.login_message = 'Unauthorized User'
login_manager.login_message_category = "info"


class LoginForm(FlaskForm):
    username = StringField('账号', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('登录')


class CreateAccountForm(FlaskForm):
    username = StringField('账号', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('注册')
