# Напишите код, который меняет значение переменных местами (var_1 должен быть равен 99 и var_2 — 37).

var_1 = 37
var_2 = 99

print('var_1 =', var_1 , 'var_2 =', var_2 )
var_1 = var_1 + var_2    
var_2 = var_1 - var_2    
var_1 = var_1 - var_2    

print('После обмена данными между переменными','var_1 =', var_1 , 'var_2 =', var_2 )

