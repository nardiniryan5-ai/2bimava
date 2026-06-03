
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
#Módulo 3: Especialista em Conteúdo
#Responsável: Brayan De Santana Da Silva
def gerar_aviso(status):
    if imc <25:
        print("Dica: Continue mantendo hábitos saudáveis, como uma dieta equilibrada e exercícios regulares!")
    else:
        print("Dica: Inclua caminhadas na sua rotina e foque em alimentos ricos em fibras. Pequenas mudanças fazem grande diferença!")
        
