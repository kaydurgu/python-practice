import functools

#html tags 

def table(func):
    @functools.wraps(func)
    def wraper(*args , **kwargs):
        print('<table>')
        func(*args ,**kwargs)
        print ('</table>')
    return wraper
def header(func):
    def wraper(*args , **kwargs):
        print('<h1>')
        func(*args ,**kwargs)
        print ('</h1>')
    return wraper
@table
@header
def say(name):
    print('***** '+ name )

#say = header(say) - this means @header

say('Zhanbolot')
"""
<table>
<h1>
 ***** Zhanbolot
</h1>
</table>
"""