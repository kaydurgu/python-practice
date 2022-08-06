
import sys

class MailItem:
    def __init__(self, mail_from, title, content) -> None:
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False
    def set_read(self, fl_read):
        self.is_read = fl_read
    def __bool__(self):
        return self.is_read
    def __repr__(self) -> str:
        return f'{self.mail_from}- {self.is_read}'

class MailBox:

    __Single = None
    def __new__(cls, *args, **kwargs):
        if MailBox.__Single is None:
            MailBox.__Single = object.__new__(cls, *args , **kwargs)
        return MailBox.__Single

    def __init__(self) -> None:
        self.inbox_list = []
    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        for i in lst_in:
            self.inbox_list.append(MailItem(*i.split(';')))

mail = MailBox()
mail.receive()
inbox_list_filtered = list(filter(bool, mail.inbox_list))
