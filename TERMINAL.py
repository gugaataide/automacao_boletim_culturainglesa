from PIL import Image,ImageFont,ImageDraw



#PASSANDO O MODELO DE BOLETIM
CAMINHO_MODELO = r"C:\Users\User\Desktop\Projeto Boletim automatico\3.png"
#FONTE
FONTE = "Exo-Black.otf"
TAMANHO_FONTE = 500

QUANTIDADE_DE_NOTAS = 3
#COORDENADAS DA IMPRESSAO
COORDENADAS= [[0,0],[0,50],[0,100],[0,150]]


#CAPTURANDO NOME DO ALUNO

nome = input("Digite o nome do aluno: ")
#ABASTECENDO OS DADOS DE NOTAS
nota = [0,0,0,0]
for i in range (QUANTIDADE_DE_NOTAS):
    nota[i] = int (input(f"Digite a {i+1}° Nota: "))
    



#CALCULANDO A MEDIA ARITMETICA
nota[3] = (nota[0] + nota[1] + nota[2]) / QUANTIDADE_DE_NOTAS

#ABRINDO A IMAGEM
imagem = Image.open(CAMINHO_MODELO)

#DEFININDO IMAGEM DE SOBREPOSIÇAO
desenho = ImageDraw.Draw(imagem)

#DEFININDO FONTE
fonte = ImageFont.truetype("Exo-Black.otf",500)

indice_nota=0


for [x,y] in COORDENADAS:
    desenho.text((x,y),str(nota[indice_nota]))
    indice_nota+=1

imagem.save(f"{nome}.png")




