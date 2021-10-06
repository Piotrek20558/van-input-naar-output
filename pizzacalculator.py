#Piotrek Lysakowski Pizza Calculator

print('Small pizza = 4')
print('Medium pizza = 5')
print('Large pizza = 6')

pizzaSmall = float(input('aantal small pizzas '))
smallpizza = 4
pizzaMedium = float(input('aantal medium pizzas '))
mediumpizza = 5
pizzaLarge = float(input('aantal large pizzas '))
largepizza = 6

print('aantal small pizzas: ' + str(int(pizzaSmall)))
print('kosten small pizza: ' + str((pizzaSmall)*(smallpizza)))

print('aantal medium pizzas: ' + str(int(pizzaMedium)))
print('kosten medium pizza: ' + str((pizzaMedium)*(mediumpizza)))
 
print('aantal large pizzas: ' + str(int(pizzaLarge)))
print('kosten large pizza: ' + str((pizzaLarge)*(largepizza)))

print('aantal pizzas ' + str(int((pizzaSmall) + (pizzaMedium) + (pizzaLarge))))
print('total ' + str((pizzaSmall) * (smallpizza) + (pizzaMedium) * (mediumpizza) + (pizzaLarge) * (largepizza)))
