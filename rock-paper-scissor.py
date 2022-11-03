import random 
f = open('puntaje.txt', 'a', encoding='utf8')
for _ in range(1,4):
    user_action=input("Seleccione (piedra-papel-tijera)")
    possible_actions=["piedra","papel","tijera"]
    computer_action=random.choice(possible_actions)
    # print(computer_action)
    print("\n Tú elegiste",user_action, " ,la computadora eligió ", computer_action,"\n")
    if user_action == computer_action:
        print("Empate !", user_action, "Ambos ganaron !")
        f.write("Empate !")
    elif user_action=="piedra" and computer_action == "papel":
            print("Ganó la computadora ! ")
            f.write("Ganó la computadora !")
    elif user_action=="piedra" and computer_action == "tijera":
            print("Ganaste !")
            f.write("Ganaste !")
    elif user_action=="papel" and computer_action == "piedra":
            print("Ganaste !")
            f.write("Ganaste !")
    elif user_action=="papel" and computer_action == "tijera":
            print("Ganó la computadora")
            f.write("Ganó la computadora !")
    elif user_action=="tijera" and computer_action == "piedra":
            print("Ganó la computadora")
            f.write("Ganó la computadora !")
    elif user_action=="tijera" and computer_action == "papel":
            print("Ganaste !")
            f.write("Ganaste !")
    else:
        print("Error seleccione bien !")