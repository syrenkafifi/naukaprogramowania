# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = input("Podaj liczbe n (n > 2): ")
    k = input("Podaj liczbe k (k > " + str(n) + "): ")

    for i in range(1,n+1):
        if i%k != 0:
            print i

    raw_input("Aby zakończyć program, naciśnij klawisz Enter.")

