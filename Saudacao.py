hora = input("Digite que horas são: ")
if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print("Horario deve estar entre 0 e 23")
    else:
        if hora <= 11:
            print(f"Bom Dia são {hora}")
        elif hora <= 17:
            print(f"Boa Tarde são {hora}")
        else:
            print(f"Boa Noite são {hora}")
else:
    print("Digite uma hora valida")
