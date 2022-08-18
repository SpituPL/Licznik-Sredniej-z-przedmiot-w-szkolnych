from time import sleep
from traceback import print_tb

Ocena_Suma = None
Ocena_Suma = float()

Ocena_Ilosc = None
Ocena_Ilosc = float()

srednia = None
srednia = float()

przedmiot = input("Podaj nazwe przedmiotu: ")
print("Podaj ocene (kliknij Enter, kiedy skonczysz pisać oceny napisz 0)")

while True:
    ocena = float(input("Podaj ocene: "))
    if ocena <= 6:
        if ocena == 0:
            srednia = Ocena_Suma / Ocena_Ilosc
            print("Twoja srednia to:", str(srednia), "z przedmiotu", str(przedmiot) + ".")
            break
        else:
            Ocena_Suma = Ocena_Suma + ocena
            Ocena_Ilosc = Ocena_Ilosc + 1
    else:
        print("Maxymalna wartosc oceny to 6! spróbuj jeszcze raz!")
        continue

historia = open("history_of_srednia_py_code_236489193781038.txt", "w")
if historia.writable():
        historia.write(str(przedmiot) + ": " + str(srednia))
        historia.close()

input()