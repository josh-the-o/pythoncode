gg = 'Hi please enter the cost price and selling price'
print(gg)

cp = int(input("\t Enter the cost price of the object \n "))

sp = int(input("\t Enter the selling price of the object \n"))

if sp > cp:
    profit = sp - cp
    profit_per = profit / cp * 100
    print('The amount profited is', profit, 'and the profit percentage is', profit_per, '%')

elif sp < cp:
    loss = cp - sp
    loss_per = loss / cp * 100
    print('The amount lost is', loss, 'and the loss percent is', loss_per, '%')

elif sp == cp:
    print("There is no profit or loss so try again")
