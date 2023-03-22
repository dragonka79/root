
def olvas_pozint():
    number = input("Please give a positive number >>> ")
    correct = "Correct, {0} is a valid positive integer.".format(number)
    sajat_hiba = ValueError("{0} is not a valid positive integer.".format(number))
    empty_hit = "It was an empty return or a string"
    try:
        if int(number) > 0:
           print(correct)
        else:
            print(sajat_hiba)
    except:
        print(empty_hit)
olvas_pozint()
