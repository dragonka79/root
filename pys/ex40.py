#       A SZÓTÁR MÓDI
#
# mystuff = {'apple': "I AM APPLES!"}
# print(mystuff['apple'])

#       A MODUL MÓDI

#
# import mystuff
# mystuff.apple()
# print(mystuff.tangerine)



#
#
# class MyStuff(object):
# #Az object a python2 compatibilitás miatt kell csak, de elhagyható
#
#     def __init__(self):
#         self.tangerine = "And now a thousand years between"
#
#     def apple(self):
#         print("I AM CLASSY APPLES!")
#
# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)



class Pont:
    """A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására. """

    def __init__(self):
        """ Egy új, origóban álló pont létrehozása. """
        self.x = 0
        self.y = 0

p = Pont() # A Pont osztály egy objektumának létrehozása (példányosítás)
q = Pont() # Egy második Pont objektum készítése

# Minden Pont objektum saját x és y attribútumokkal rendelkezik
print(p.x, p.y, q.x, q.y)
