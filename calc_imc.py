
#Módulo 1: Lógica Matemática
#Responsável: Pedro Henryke da Costa Gomes
def calcular_imc(p, a):
    imc = p / (a ** 2)
    return imc

#Módulo 2: Classificação de Dados
#Módulo 3: Especialista em Conteúdo
#Responsável: Rafael Henrique Trajano
def classificar(valor_imc):
    if valor_imc <25:
        print("Saudável ✅")
    else:
        print("Acima do peso 🚫")
        
def gerar_aviso(status):
    if imc <25:
        print("Dica: Continue mantendo hábitos saudáveis, como uma dieta equilibrada e exercícios regulares!")
    else:
        print("Dica: Inclua caminhadas na sua rotina e foque em alimentos ricos em fibras. Pequenas mudanças fazem grande diferença!")

#Módulo 4:Engenheiro de Integração
#Responsável: Ryan Nardini Pereira
p = float(input("Qual o Seu Peso atual? "))
a = float(input("Qual sua altura atual? "))
 
imc = calcular_imc(p, a)
print(f"Seu IMC é: {imc:.2f}")
classificar(imc)
gerar_aviso(imc) 
