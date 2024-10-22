
dot_name = (".com", ".ru", ".net")

def check_mail(mail):
    return (mail.find('@') != -1) and mail.endswith(dot_name)

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if not (check_mail(recipient) and check_mail(sender)):
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient, ' Проверьте написание @почты')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient)

send_email('asldgjlasj', 'sa@ldgk.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')