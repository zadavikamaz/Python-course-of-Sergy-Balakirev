class Viber:
    msgs = []

    @classmethod
    def add_message(cls, msg):
        cls.msgs.append(msg.text)

    @classmethod
    def remove_massage(cls, msg):
        cls.msgs.remove(msg.text)

    @staticmethod
    def set_like(msg):
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls, char):
        print(cls.msgs[-char:])

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)


class Message:
    def __init__(self, text: str, fl_like: bool = False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
print(Viber.total_messages()) #
print(Viber.total_messages() == 1) #
Viber.add_message(Message("Это курс по Python ООП."))
print(Viber.total_messages()) #
Viber.add_message(Message("Что вы о нем думаете?"))
print(Viber.total_messages()) #
Viber.set_like(msg)
Viber.remove_massage(msg)
print(Viber.total_messages()) #
Viber.show_last_message(2)

for i in Viber.msgs:
    print(i)