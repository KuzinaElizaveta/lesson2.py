#Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.Например, передаем 2, на выходе получаем «Зима»
# не работает 

month_to_season_str = input ("Введите номер месяца: ")
month_to_season = int(month_to_season_str)

if (month_to_season == 1 or month_to_season == 2 or month_to_season == 12):
    print("Зима")
else: 
    if (month_to_season == 3 or month_to_season == 4 or month_to_season == 5):
     print("Весна")
    else: 
        if (month_to_season == 6 or month_to_season == 7 or month_to_season == 8):
         print("Лето")
        else: 
            if (month_to_season == 9 or month_to_season == 10 or month_to_season == 11):
             print("Осень")
             
print (month_to_season) 
