import os
import time

def agendar_desligamento(tempo):
    segundos = tempo * 60
    print(f"O computador será desligado em: {tempo} minutos.")
    time.sleep(segundos-5) # Aguarda até 5 segundos antes do desligamento
    os.system("shutdown -s -t S" if os.name == "nt" else "shutdown -n now")

def cancelar_desligamento():
    print("Cancelando o desligamento.")
    os.system("shutdown -a" if os.name == "nt" else "shutdown -c")

def menu():
    while True:
        print("\nDesligamento Automático")
        print("1. Agendar")
        print("2. Cancelar")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            try:
                minutos = int(input("Em quantos minutos deseja desligar o computador? "))
                agendar_desligamento(minutos)
            except ValueError:
                print("Por favor, insira um número válido: ")
        elif escolha == "2":
            cancelar_desligamento()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()