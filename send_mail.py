import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail('test email from django',
              'this is the email content',
              'azdxyx@163.com',
              ['710627606@qq.com'])
