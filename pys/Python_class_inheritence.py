# Python_class_inheritence
# 1. Írjunk 2 olyan python class-t (router a parent, az sw a child),
# amely kimenetként ezt adja:
#
# Rtr1
# Router Model :iosV
# Software Version :15.6.7
# Router Management Address:10.10.10.1
#
# Sw1
# Switch Model :Cat9300
# Software Version :16.9.5
# Switch Management Address:10.10.10.8

class Router:
    ''' Router Class '''
    def __init__(self, model, swversion, ip_add):
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

    def getdesc(self):
        ''' return a formatted description of the router '''
        desc = (f'Router Model: {self.model}\n'
                f'Software Version: {self.swversion}\n'
                f'Router Management Address: {self.ip_add}\n')
        return desc

class Switch(Router):
    def getdesc(self):
        '''return a formatted description of the switch'''
        desc = (f'Switch Model:{self.model}\n'
                f'Software Version: {self.swversion}\n'
                f'Switch Management Address:{self.ip_add}\n')
        return desc

rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
sw1 = Switch('Cat9300', '16.9.5', '10.10.10.8')

print('\nRtr1\n', rtr1.getdesc(), '\t')
print('Sw1\n', sw1.getdesc(), '\t')
