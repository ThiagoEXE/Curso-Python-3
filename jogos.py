import forca;
import adivinhacao;

def escolher_jogo():
    print("*********************************")
    print("*****Escolha seu jogo!*****")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo você quer?"))

    def soma(val1, val2):
        return val1 +  val2

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    else:
        print(soma(2,4))
if(__name__ == '__main__'):
    escolher_jogo()
