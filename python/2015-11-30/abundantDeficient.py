import sys

def getDivisors(z):
    '''
    Really dumb way. Will improve after inital checkin
    '''
    for i in range(1, int(z/2)+1):
        if z % i == 0:
            yield i

for x in range(2, int(sys.argv[1]) + 2):
    divisorSum = 0
    number = int(sys.argv[x])
    for y in getDivisors(number):
        divisorSum += y

    if(divisorSum < number):
        print(str(number) + ' deficient')
    elif (divisorSum > number):
        print(str(number) + ' abundant by ' + str(divisorSum - number))
    else:
        print(str(number) + ' perfect')