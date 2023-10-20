#Operadores logicos

#Operador and

a = 10
b = 5

resultado = a > b and b > 0
#tabla and
# v and v = v
# v and f = f
# f and v = f
# f and f = f

print(resultado)

#Operador or

resultado = a > b or b > 0
#tabla or
# v or v = v
# v or f = v
# f or v = v
# f or f = f


print(resultado)

#Operador not

resultado = not(a < b)


print(resultado)

resultado = a==5 and b == 5
print(resultado)


print(resultado)


#Prioridad operaciones

resultado = 2 + 3 * 4 == 14 and not(5>6 or 7<8)
#resultado = False

#Operadores Aritméticos
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -

#Operadores relacionales
# 1. ==
# 2. !=
# 3. <, >, <=, >=

#Operadores lógicos

# 1. not
# 2. and
# 3. or

print(resultado)