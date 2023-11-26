'''
Solution 1 self
list=[2, 4, 6, 3, 12, 7, 1]
min=list[0]
for i in range(len(list)):
    if list[i]<min:
        min=list[i]
        index=i
        max=list[i]
        
for i in range(index, len(list)):
    if list[i]>max:
        max=list[i]
        index2=i

if max==min:
    print("No Profit")
elistse:
    print(f"The best time to buy stock is on Day {index+1} with price {min} and sell on Day {index2+1} having price {max}")
'''

# Solution 2
my_list = [7, 1, 5, 3, 6, 4]

min_price = my_list[0]
buy_day = 0
sell_day = 0

for i in range(len(my_list)):
    if my_list[i] < min_price:
        min_price = my_list[i]
        buy_day = i
    elif my_list[i] > min_price:
        sell_day = i

if buy_day >= sell_day:
    print("No Profit")
else:
    print(f"The best time to buy stock is on Day {buy_day + 1} with price {min_price} and sell on Day {sell_day + 1} having price {my_list[sell_day]}")
    