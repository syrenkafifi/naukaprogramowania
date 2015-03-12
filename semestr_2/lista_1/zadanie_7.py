# -*- coding: utf-8 -*-

# narazie sie tym nie przejmuj :-)
# dziala i bez :P
if __name__ == "__main__":
    n = input("Podaj liczbe n (n > 2): ")
    k = raw_input("Podaj liczbe k (k > " + str(n) + "): ")

    for i in range(1,n+1):
        if i%k != 0:
            print i
    # w pythonie2 raw_input zwraraca stringa
    # input z kolei próbuje zeewaluować wartość wprowadzoną jako wyrażenie pythona.
    # brzmi skomplikowanie ale chodzi o to żę jak napisze
    # a = input("Podaj liczbe) i wpisze 3 to dostane a =3
    # a jak wpisze b = raw_input("Podaj liczbe) to dostane b = '3'
    # rwa input uzylem do wciagania entera bo jak wpisywalem pusty znak czyli nie wpisywalem nic i walilem enterem
    # to cos mi sypalo bledem ;-)
    raw_input("Aby zakończyć program, naciśnij klawisz Enter.")
    pass

