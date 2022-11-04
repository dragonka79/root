import time

def sajat_szum(xs):
    szum = 0
    for i in xs:
        szum += i
    return szum

def sajat_szum2(xs):
    """ Egymást követő egész számokból álló lista összege"""
    szum2 = int((xs[-1] * (xs[-1] + 1)) / 2)
    return szum2

sz = 10000000 # Legyen 10 millió eleme a listának
testadat = range(sz)

t0 = time.perf_counter()
sajat_eredmeny = sajat_szum(testadat)
t1 = time.perf_counter()
print("saját_eredmény = {0} (eltelt idő = {1:.4f} másodperc"
        .format(sajat_eredmeny, t1 - t0))


t2 = time.perf_counter()
gepi_eredmeny = sum(testadat)
t3 = time.perf_counter()
print("gépi_eredmény = {0} (eltelt idő = {1:.4f} másodperc)"
        .format(gepi_eredmeny, t3-t2))


t4 = time.perf_counter()
sajat_eredmeny2 = sajat_szum2(testadat)
t5 = time.perf_counter()
print("saját_eredmény2 = {0} (eltelt idő = {1:.4f} másodperc"
        .format(sajat_eredmeny2, t5 - t4))