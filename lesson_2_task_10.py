#2. Дано**:** пользователь делает вклад в размере Х рублей сроком на Y лет под 10% годовых (каждый год размер его вклада увеличивается на 10%, эти деньги прибавляются к сумме вклада, 
#и на них в следующем году тоже будут проценты).
# 3. Задача: написать функцию bank, принимающую аргументы X и Y и возвращающую сумму, которая будет на счету пользователя спустя Y лет.


# x - исходная сумма, y - срок в годах, p - процентная ставка
def task(x,y,p):
    for t in range(y):
        x=(1+p/100)*x
    return x
print (task) 