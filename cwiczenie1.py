import sys
import logging
logging.basicConfig(level=logging.DEBUG)

while True:
    dzialanie=input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
    if(dzialanie=='1' or dzialanie=='2' or dzialanie=='3'or dzialanie=='4'):
        break

logging.debug("wartosc wybrana %s" % dzialanie)


while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        liczba1 = float(input('Podaj wartość pierwszą: '))
        logging.debug("liczba 1: %s" % liczba1)


    except ValueError:
        print("Wartosc musi być liczbą całkowitą lub zmiennoprzecinkową. Wybierz jeszcze raz.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        liczba2 = float(input('Podaj wartość drugą: '))
        logging.debug("liczba 2: %s" % liczba2)

    except ValueError:
        print("Wartosc musi być liczbą całkowitą lub zmiennoprzecinkową. Wybierz jeszcze raz.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break


if dzialanie=="1":
    logging.debug('Dodaje %s i %s', liczba1, liczba2)
    wynik=float(liczba1)+float(liczba2)
    logging.debug("wynik sumowania: %s" % wynik)

if dzialanie=="2":
    logging.debug('Odejmuję %s od %s', liczba1, liczba2)
    wynik=float(liczba1)-float(liczba2)
    logging.debug("wynik odejmowania: %s" % wynik)

if dzialanie=="1":
    logging.debug('Dodaje %s i %s', liczba1, liczba2)
    wynik=float(liczba1)+float(liczba2)
    logging.debug("wynik sumowania: %s" % wynik)

if dzialanie=="3":
    logging.debug('Mnożenie %s i %s', liczba1, liczba2)
    wynik=float(liczba1)*float(liczba2)
    logging.debug("wynik mnożenia: %s" % wynik)

if dzialanie=="4":
    logging.debug('Dzielenie %s przez %s', liczba1, liczba2)
    wynik=float(liczba1)/float(liczba2)
    logging.debug("wynik dzielenia: %s" % wynik)
