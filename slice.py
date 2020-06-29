toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings) #how many toppings are available

print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

pizzas = list(zip(prices, toppings)) #match toppings to their prices
print(pizzas)

pizzas.sort() #sort from cheapest to most expensive
print(pizzas)

cheapest_pizza = pizzas[0] #find cheapest topping
print(cheapest_pizza)

priciest_pizza = pizzas[-1] #find most expensive topping
print(priciest_pizza)

three_cheapest = pizzas[0:3] #find three cheapest toppings
print(three_cheapest)

num_two_dollar_slices = prices.count(2) #how many $2 slices are there
print(num_two_dollar_slices)