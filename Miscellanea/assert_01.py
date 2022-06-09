def div(a: int , b: int ) -> int:
    assert b!=0, 'Нельзя делить на ноль'  # if assert con -> True Нельзя делить на ноль 
    return int(a / b)
div (1, 0)

'''
Метод                       Проверка на 

assertEqual(x, y)	        x == y	

assertNotEqual(x, y)	    x != y	

assertTrue(x)	            bool(x) равно True	

assertFalse(x)	            bool(x) равно False	

assertIs(x, y)	            x это y	

assertIsNot(x, y)	        x это не y	

assertIsNone(x)	            x это None	

assertIsNotNone(x)	        x это не None	

assertIn(x, y)	            x в y	

assertNotIn(x, y)	        x не в y	

assertIsInstance(x, y)	    isinstance(x, y)	

assertNotIsInstance(x,y)	не isinstance(x, y)
'''
#
