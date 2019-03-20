# https://www.goodhousekeeping.com/health/diet-nutrition/a46956/how-much-water-should-i-drink/
import math
import schedule
import time
def set_default_cup_size(x=200):
    default_size=x
    return default_size
water_drunk=0
water_frequency=0
percent_goal_reached=0
glass_size=set_default_cup_size()
def cup_size():
    global glass_size
    print('1.100ml')
    print('2.200ml')
    print('3.300ml')
    print('4.400ml')
    print('5.500ml')
    print('6.Customize')
    choice=int(input())
    if choice==1:
        glass_size=100
    elif choice==2:
        glass_size=200
    elif choice==3:
        glass_size=300
    elif choice==4:
        glass_size=400
    elif choice==5:
        glass_size=500
    elif choice==6:
        glass_size=int(input('Enter glass size'))
    else:
        glass_size=set_default_cup_size()
def percent_completed():
    global water_drunk
    global water_intake_litres
    return (water_drunk / water_intake_litres)*100
def water_reminder():
    global water_intake_litres
    global water_frequency
    global water_drunk
    global glass_size
    print('Did you drink your glass of water?')
    print('Press 1 for YES and 2 for NO')
    ans=int(input())
    if ans==1:
        water_drunk+=glass_size
        water_frequency+=1
    else:
        print('Try Drinking your Water!')
    print('Your water frequency is :',water_frequency)
    print('PERCENT GOAL REACHED : ',percent_completed())
def roundup(x):
    return int(math.ceil(x / 10.0)) * 10
print('Enter your weight in:')
print('1.KiloGrams')
print('2.Pounds')
choice=int(input())
def to_pounds(x):
    return x*2.2046
if choice==1:
    weight_kg=int(input('Enter your weight'))
    weight_pounds=to_pounds(weight_kg)
elif choice==2:
    weight_pounds=int(input('Enter your weight'))
else:
    print('Invalid Choice')
water_intake=(weight_pounds/2.2)
age=int(input('Enter your age'))
if age<=0:
    print('Please try again!')
elif age<30:
    water_intake*=40
elif age < 55 and age > 30:
    water_intake*=35
else:
    water_intake*=30
water_intake/=28.3
water_intake_ounces=water_intake
water_intake_litres=roundup(water_intake*29.5735)
print('You need to drink {} millilitres of water everyday!'.format(water_intake_litres))
time_interval=int(input('Remind me of drinking water every __ minutes'))
schedule.every(time_interval).minutes.do(water_reminder)
print('Your water frequency is :',water_frequency)
print('PERCENT GOAL REACHED : ',percent_completed())
while True:
    schedule.run_pending()
    time.sleep(1)


