print('Welcome to my store')

shopping= input('Do you have an account already? ')
if shopping != 'yes':
    print('sign up')

print('please insert your log in details')


print('please select items to add in your cart, use -1 when you are done')

total_prices = 0

prices = [50,2,20,30,100,5,6]
stock = ['dresses','tomatoes','fruits','milk','kfc','bread','thing']

for i in range(len(prices)):
    print(str(i+1)+'.',stock[i], ':','R'+str(prices[i]))

while True:
    product_index = int(input('Select your product:'))
    if product_index==-1:
        break
    print('you have selected: ', stock[product_index-1])
    total_prices = total_prices + prices[product_index-1]

print('your total prices is',total_prices ,'added to your cart')



