
#Módulo 1: Lógica Matemática
#Responsável: Pedro Henryke da Costa Gomes
def calcular_imc(p, a):
    imc = p / (a ** 2)
    return imc

#Módulo 2: Classificação de Dados
#Responsável: Rafael Henrique Trajano
def classificar(valor_imc):
    if valor_imc <25:
        print("Saudável ✅")
    else:
        print("Acima do peso 🚫")
        
