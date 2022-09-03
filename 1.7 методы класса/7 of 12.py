from string import ascii_lowercase, digits

CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits

class TextInput:
    def name:
        pass
    def size:
        pass
    def get_html(self):
        return f'<p class='login'><имя поля>: <input type='text' size=<размер поля> />'

    @classmethod
    def check_name(cls, name):
    # длина имени не менее 3 символов и не более 50;
    # в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
        if not 3 <= len(name) <= 50 and all([symbol for symbol in name if symbol in CHARS_CORRECT]):
            raise ValueError("некорректное поле name")


class PasswordInput:
    def name:
        pass
    def size:
        pass
    def get_html(self):
        return f'<p class='password'><имя поля>: <input type='text' size=<размер поля> />'
    @classmethod
    def check_name(cls, name):
        if not 3 <= len(name) <= 50 and all(symbol for symbol in name if symbol in CHARS_CORRECT):
            raise ValueError("некорректное поле name")

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()