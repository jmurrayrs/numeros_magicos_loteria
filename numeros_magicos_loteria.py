import csv
import random
from datetime import datetime
import os

def carregar_apostas_csv(arquivo):
    apostas = []
    try:
        with open(arquivo, 'r') as f:
            leitor = csv.reader(f)
            for linha in leitor:
                aposta = [int(num) for num in linha]
                apostas.append(aposta)
        return apostas
    except FileNotFoundError:
        print(f"\nErro: Arquivo {arquivo} não encontrado!")
        return None
    except Exception as e:
        print(f"\nErro ao ler o arquivo: {str(e)}")
        return None

def encontrar_numeros_magicos(apostas):
    numeros_magicos = []
    for numero in range(1, 61):
        numero_magico = True
        for aposta in apostas:
            if numero in aposta:
                numero_magico = False
                break
        if numero_magico:
            numeros_magicos.append(numero)
    return numeros_magicos

def salvar_resultado(numeros_magicos):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"numeros_magicos_{timestamp}.txt"
    
    with open(nome_arquivo, 'w') as f:
        f.write("Números Mágicos encontrados:\n")
        f.write(", ".join(map(str, numeros_magicos)))
        f.write(f"\nTotal de números mágicos: {len(numeros_magicos)}")
    
    print(f"\nResultados salvos em: {nome_arquivo}")

def gerar_apostas_aleatorias(quantidade):
    apostas = []
    for _ in range(quantidade):
        aposta = sorted(random.sample(range(1, 61), 6))
        apostas.append(aposta)
    return apostas

def salvar_apostas_csv(apostas, nome_arquivo):
    try:
        with open(nome_arquivo, 'w', newline='') as f:
            escritor = csv.writer(f)
            escritor.writerows(apostas)
        print(f"\nApostas salvas com sucesso em: {nome_arquivo}")
    except Exception as e:
        print(f"\nErro ao salvar arquivo: {str(e)}")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    while True:
        limpar_tela()
        print("\n=== Sistema de Análise da Loteria ===")
        print("1. Gerar novas apostas aleatórias")
        print("2. Carregar apostas de arquivo CSV")
        print("3. Encontrar números mágicos")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção (1-4): ")
        
        if opcao == "1":
            try:
                qtd = int(input("\nQuantas apostas deseja gerar? "))
                nome_arquivo = input("Nome do arquivo para salvar (ex: apostas.csv): ")
                
                print("\nGerando apostas...")
                apostas = gerar_apostas_aleatorias(qtd)
                salvar_apostas_csv(apostas, nome_arquivo)
                
                input("\nPressione Enter para continuar...")
                
            except ValueError:
                print("\nErro: Digite um número válido!")
                input("\nPressione Enter para continuar...")
                
        elif opcao == "2":
            nome_arquivo = input("\nNome do arquivo para carregar: ")
            apostas = carregar_apostas_csv(nome_arquivo)
            
            if apostas:
                print(f"\nForam carregadas {len(apostas)} apostas!")
            
            input("\nPressione Enter para continuar...")
            
        elif opcao == "3":
            nome_arquivo = input("\nNome do arquivo com as apostas para análise: ")
            apostas = carregar_apostas_csv(nome_arquivo)
            
            if apostas:
                print("\nAnalisando números mágicos...")
                numeros_magicos = encontrar_numeros_magicos(apostas)
                salvar_resultado(numeros_magicos)
                
                print("\nNúmeros mágicos encontrados:", numeros_magicos)
                print(f"Total de números mágicos: {len(numeros_magicos)}")
            
            input("\nPressione Enter para continuar...")
            
        elif opcao == "4":
            print("\nSaindo do sistema...")
            break
        
        else:
            print("\nOpção inválida!")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    exibir_menu()
