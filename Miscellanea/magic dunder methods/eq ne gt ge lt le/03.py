
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

class StringText:
    def __init__(self, lst) -> None:
        self.lst = lst
    def __repr__(self) -> str:
        return ' '.join(self.lst) + ':' + str(len(self))
    def __len__(self):
        return len([x for x in self.lst if x not in '–?!,.;'])
    def __gt__(self, __o: object) -> bool:
        return len(self) > len(__o)
    def __ge__(self, __o: object) -> bool:
        return len(self) >= len(__o)
    def __lt__(self, __o: object) -> bool:
        return len(self) < len(__o)
    def __le__(self, __o: object) -> bool:
        return len(self) <= len(__o)

    
lst_text = [StringText(string.strip('–?!,.;').split()) for string in stich]
lst_text_sorted = sorted(lst_text,  reverse=True)
lst_text_sorted = [' '.join(lst.lst) for lst in lst_text_sorted]