#CALCULATE SQUARE ROOT USING BISECTION METHOD

number = abs(float(input("Calculate square root of? ")))
lowerBound = abs(float(input("Lower bound value? ")))
upperBound = abs(float(input("Upper bound value? ")))

epsilon = 0.001

while True:
    guess = (lowerBound + upperBound) / 2
    difference = guess**2 - number
    if abs(difference) <= epsilon:
        break
    if difference < 0:
        lowerBound = guess
    else:
        upperBound = guess

print('The square25 root is approximately {}.'.format(round(guess, 3)))
