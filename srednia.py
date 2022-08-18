from time import sleep

Ocena_Suma = None
Ocena_Suma = float()

Ocena_Ilosc = None
Ocena_Ilosc = float()

srednia = None
srednia = float()

historia = open("history_of_srednia_py_code_236489193781038.txt", "w")


przedmiot = input("Podaj nazwe przedmiotu: ")

while True:
    ocena = float(input("Podaj ocene (kliknij Enter, kiedy skonczysz pisać oceny napisz 0): "))
    if ocena == 0:
        srednia = Ocena_Suma / Ocena_Ilosc
        print("Twoja srednia to:", str(srednia), "z przedmiotu", str(przedmiot) + ".")
        break
    else:
        Ocena_Suma = Ocena_Suma + ocena
        Ocena_Ilosc = Ocena_Ilosc + 1

if historia.writable():
        historia.write(str(przedmiot) + ": " + str(srednia))
        historia.close()

input()