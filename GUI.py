from PIL import Image,ImageFont,ImageDraw
import tkinter as tk

def onclick():
    nota[1] = nota[1].tk.get()
    nota[2] = nota[2].tk.get()
    nota[3] = nota[3].tk.get()

#PASSANDO AS COORDENADAS DAS NOTAS
CAMINHO_MODELO = "3.png"
#FONTE
FONTE = "Exo-Black.otf"
TAMANHO_FONTE = 500

QUANTIDADE_DE_NOTAS = 3
#COORDENADAS DA IMPRESSAO
COORDENADAS= [[0,0],[0,50],[0,100],[0,150]]


janela = tk.Tk()
janela.geometry("400x400")
janela.title("BOLETIM CULTURA INGLESA")

#CAPTURANDO NOME DO ALUNO

tk.Label(text="Nome do aluno").place(x=5,y=0)
nome = tk.Entry(janela).place(x=0,y=20)
#ABASTECENDO OS DADOS DE NOTAS
nota = [0,0,0,0]
for i in range (QUANTIDADE_DE_NOTAS):
    tk.Label(text=f"Digite a {i+1}° Nota").place(x=5, y=70+(i*100)-20)
    nota[i] = tk.Entry(janela).place(x=0,y=70+(i*100))
    



#CALCULANDO A MEDIA ARITMETICA
#nota[3] = (nota[0] + nota[1] + nota[2]) / 3

#ABRINDO A IMAGEM
imagem = Image.open(CAMINHO_MODELO)

#DEFININDO IMAGEM DE SOBREPOSIÇAO
desenho = ImageDraw.Draw(imagem)

#DEFININDO FONTE
fonte = ImageFont.truetype(FONTE,TAMANHO_FONTE)

indice_nota=0


for [x,y] in COORDENADAS:
    desenho.text((x,y),str(nota[indice_nota]), font= fonte)
    indice_nota+=1

imagem.save(f"{nome}.png")

tk.Button(text="Submit", command=onclick()).grid(ipadx=1,ipady=3)

janela.mainloop()



