# 1.Forvo_DEVASC_feladatok: Python classok_1

# 1. Írjunk egy class-t amely definiálja egy router model-jét, sw verzióját
# és ip-jét. Ezzel hozzunk létre egy rtr1 nevű routert és irassuk ki a
# legegyszerűbb módon az előbb definiált adatait, amelyek a következők:
#
# model = iosV
# swversion = 15.6.7
# ip_add = 10.10.10.1

class Router:
    ''' Router Class '''
    def __init__(self, model, swversion, ip_add):
        ''' initialize values '''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
print(rtr1.model, rtr1.swversion, rtr1.ip_add)


# 2. Az előbbi feladatot írjuk át, adjunk hozzá a classhoz egy getdesc nevű
# függvényt, amely korrektül kiírja a router adatait, így nézzen ki:
#
# Rtr1
# Router Model :iosV
# Software Version :15.6.7
# Router Management Address:10.10.10.1


class Router:
    ''' Router Class '''
    def __init__(self, model, swversion, ip_add):
        ''' initialize values '''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add
    def getdesc(self):
        '''  return a formatted description of the router   '''
        desc = f'Router Model: {self.model}\n'\
               f'Software version: {self.swversion}\n'\
               f'Router Management Address: {self.ip_add}'
        return desc

rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
print('Rtr1',end = '\n')
print(rtr1.getdesc())
