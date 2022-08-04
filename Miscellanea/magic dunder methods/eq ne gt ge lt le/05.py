
from collections import defaultdict
class Morph:
    
    def __init__(self , *words) -> None:

        self.__words = defaultdict(bool)
        self.__sily_words = list(words)
        for x in words:self.__words[x.lower()] = True
        
    def __eq__(self, __o: str) -> bool:
        return self.__words[__o.strip('.?,!@').lower()]
    def __ne__(self, __o: str) -> bool:
        return not self.__words[__o.strip('.?,!@').lower()]
    def get_words(self):
        return tuple(self.__sily_words)
    def add_word(self, word):
        self.__sily_words.append(word)
        self.__words[word] = True
dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'
                        ),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'
                        ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                                 )]
text = input()

words_in = [x for x in text.split() if x in dict_words]

print (len(words_in))