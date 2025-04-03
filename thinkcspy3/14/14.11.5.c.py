import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

my_tickets = [
    [42, 43, 44, 45, 46, 47], 
    [42, 4, 44, 45, 46, 47], 
    [42, 4, 7, 45, 46, 47], 
    [48, 43, 44, 45, 46, 13],
    [2, 3, 8, 12, 5, 14]
    ]

huzas = [42,4,7,11,1,13]

def lotto_talalatok(huzas, tickets):
    talalatok_szama = []
    for i in range(len(tickets)):
        talalat = 0   
        for j in huzas:        
            if j in tickets[i]:
                talalat += 1
        talalatok_szama.append(talalat)
    return talalatok_szama

teszt(lotto_talalatok([42,4,7,11,1,13], my_tickets) == [1,2,3,1,0])

