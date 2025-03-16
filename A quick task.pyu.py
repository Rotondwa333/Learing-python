weight = input('weight : ')

unit = input('(k)g or (l)bs: ')
if unit.upper() == 'k':
    converted = float(weight)/0.45
    print('wweight in Lbs : '+str(converted))
else:
    converted = float(weight)*0.45
    print("weight in kg is: " + str(converted))
