import smtplib
import platform
import psutil
from email.mime.text import MIMEText
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        button = Button(text='Отправить на почту', on_press=self.send_email)
        layout.add_widget(button)

        self.label = Label(text='')
        layout.add_widget(self.label)

        return layout

    def send_email(self, instance):
        # Получение информации об операционной системе
        os_info = platform.platform()

        # Получение информации о размере памяти
        memory_info = psutil.virtual_memory()
        memory_size = memory_info.total

        # Отправка электронной почты
        sender_email = "test00000133@mail.ru"
        sender_password = "8k51CuA8BhF6vWrvpNss"
        recipient_email = "razumfond@mail.ru"

        subject = "Информация об устройстве"
        email_body = f"Информация об устройстве:\nОС: {os_info}\nРазмер памяти: {memory_size} байт"

        try:
            msg = MIMEText(email_body.encode('utf-8'), 'plain', 'utf-8')
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = recipient_email

            server = smtplib.SMTP("smtp.mail.ru", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()

            self.label.text = "Письмо успешно отправлено!"
            print("Письмо успешно отправлено!")
        except Exception as e:
            self.label.text = f"Ошибка при отправке письма: {e}"
            print(f"Ошибка при отправке письма: {e}")

if __name__ == '__main__':
    MyApp().run()
