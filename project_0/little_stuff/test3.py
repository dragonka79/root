

for i in range (1,101):

    A = i % 3 == 0
    B = i % 5 == 0

    if A and B:
        print('fizzbuzz')
    elif A:
        print('fizz')
    elif B:
        print('buzz')
    else:
        print(i)
