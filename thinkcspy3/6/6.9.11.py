from unittest import teszt

def osszehasonlitas(a, b):
    if int(a) > int(b):
        return 1
    elif int(a) == int(b):
        return 0
    else:
        return -1

teszt(osszehasonlitas(5, 4) == 1)
teszt(osszehasonlitas(7, 7) == 0)
teszt(osszehasonlitas(2, 3) == -1)
teszt(osszehasonlitas(42, 1) == 1)