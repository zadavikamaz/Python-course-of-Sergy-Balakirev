from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number: str) -> bool:
        n_s = number.split('-')
        if len(n_s) == 4 and all(
                [(str.isdigit(n) and len(n) == 4) for n in n_s]
        ):
            return True
        return False

    @classmethod
    def check_name(cls, name) -> bool:
        a = []
        for n in name.split():
            for m in n:
                if m in cls.CHARS_FOR_NAME:
                    a.append(True)
                else:
                    a.append(False)

        if len(name.split()) == 2 and all(a):
            return True
        return False


is_number = CardCheck.check_card_number("1244-5678-9012-0000")
is_name = CardCheck.check_name("SERGEY BALAKIREV")
print(is_number)
print(is_name)
