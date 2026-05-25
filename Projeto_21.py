import tkinter as tk
from tkinter import messagebox

largura = 1300
altura = 600
escala = 60
x_origem = largura * 0.05
y_origem = altura * 0.9

PontosOcupadosMeio = []

Pontos_da_Linha = []

Linhas_Total = []

Linhas_Horizontais = []
Linhas_Verticais = []

Linha_Completa_Horizontal = []
Linha_Atual_Horizontal = []
Linha_Horizontal_Somar = []
Linha_Completa_Horizontal_Ordenada = []
Linha_Completa_Horizontal_Ordenada_Final = []
Linha_Horizontal_Sem_Repetição = []
Linha_Horizontal_Sem_Repetição_Final = []

Linha_Completa_Vertical = [] 
Linha_Atual_Vertical = []
Linha_Vertical_Somar = []
Linha_Completa_Vertical_Ordenada = [] 
Linha_Completa_Vertical_Ordenada_Final = []
Linha_Vertical_Sem_Repetição = []
Linha_Vertical_Sem_Repetição_Final = []

LinhaMesmoYFinal = []
LinhaMesmoY2 = []

Lista_Guarda_H = []

Resistores_Já_Inseridos_P1 = []
Resistores_Já_Inseridos_P2 = []

Pontos_da_Fonte = [[1,2], [1,3], [1,4]]

linha_preview_id = None
    

def Inserir_Resistor():

    try:
        horizontal = False
        vertical = False
        negativo = False
        One_PontoProibido = False
        PontoProibido = False
        k = False
        Resistor_Já_Inserido = False
        Resistência_Inválida = False
        Resistencia_Negativa = False
        NaFonte = False

        x1 = int(Input_x1.get())
        y1 = int(Input_y1.get())

        x2 = int(Input_x2.get())
        y2 = int(Input_y2.get())

        try:
            R = int(Input_Resistor.get())
            if R <= 0:
                Resistencia_Negativa = True
        except ValueError:
            Resistência_Inválida = True    

        if x1 == x2:
            vertical = True
        if y1 == y2:
            horizontal = True 

        if x1 < 0:
            negativo = True
        if x2 < 0:
            negativo = True
        if y1 < 0:
            negativo = True
        if y2 < 0:
            negativo = True 

        for verificador in PontosOcupadosMeio:
            if ([x1, y1] == verificador) or ([x2, y2] == verificador):
                One_PontoProibido = True

        if One_PontoProibido == True:
            PontoProibido = True
        else:
            PontoProibido = False

        for verificador2 in Resistores_Já_Inseridos_P1:
            if ([x1, y1] == verificador2) or ([x2, y2] == verificador2):
                j = (Resistores_Já_Inseridos_P1.index(verificador2))
                print(j)
                
                if (Resistores_Já_Inseridos_P2[j] == [x1, y1]) or (Resistores_Já_Inseridos_P2[j] == [x2, y2]):
                    k = True 

        if (k == True):
            Resistor_Já_Inserido = True
        else:                   
            Resistor_Já_Inserido = False

        print(Resistor_Já_Inserido)

        if (([x1, y1]) in Pontos_da_Fonte) or (([x2, y2]) in Pontos_da_Fonte) or (([(((x1+x2)/2)), (((y1+y2)/2))]) in Pontos_da_Fonte):
            NaFonte = True

        if (horizontal == True) and (vertical == False) and (negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (Resistência_Inválida == False) and (Resistencia_Negativa == False) and (NaFonte == False):
            if (x1 - x2 == 2) or (x2 - x1 == 2):    
                
                Resistores_Já_Inseridos_P1.append([x1, y1])
                Resistores_Já_Inseridos_P2.append([x2, y2])
                Desenhar_Resistor_Horizontal()

            else:
                messagebox.showinfo("Erro", "Tamanho inválido!")    

        if (horizontal == False) and (vertical == True) and (negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (Resistência_Inválida == False) and (Resistencia_Negativa == False) and (NaFonte == False):
            if (y1 - y2 == 2) or (y2 - y1 == 2):    
                
                Resistores_Já_Inseridos_P1.append([x1, y1])
                Resistores_Já_Inseridos_P2.append([x2, y2])
                Desenhar_Resistor_Vertical()

            else:
                messagebox.showinfo("Erro", "Tamanho inválido!")

        if (horizontal == True) and (vertical == True) and (negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (Resistência_Inválida == False) and (Resistencia_Negativa == False) and (NaFonte == False):            
            messagebox.showinfo("Olá", "Pontos devem ser diferentes!")

        if (horizontal == False) and (vertical == False) and (negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (Resistência_Inválida == False) and (Resistencia_Negativa == False) and (NaFonte == False):            
            messagebox.showinfo("Erro", "Resistores devem ser estar na vertical ou horizontal!")

        if (negativo == True) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (Resistência_Inválida == False) and (Resistencia_Negativa == False) and (NaFonte == False):
            messagebox.showinfo("Erro", "Digite somente números positivos!")

        if (PontoProibido == True) and (Resistor_Já_Inserido == False) and (Resistência_Inválida == False) and (Resistencia_Negativa == False) and (NaFonte == False):
            messagebox.showinfo("Erro", "Resistor já inserido no local!")

        if (Resistor_Já_Inserido == True) and (Resistência_Inválida == False) and (Resistencia_Negativa == False) and (NaFonte == False):
            messagebox.showinfo("Erro", "Resistor já inserido no local, não pode!")
        
        #print(type(R))
        if (Resistencia_Negativa == True) and (Resistência_Inválida == False) and (NaFonte == False):
            messagebox.showinfo("Erro", "Digite um valor positivo para a resistência")

        if (Resistência_Inválida == True) and (NaFonte == False):
            messagebox.showinfo("Erro", "Digite um valor válido (um número) para a resistência")

        if (NaFonte == True):
            messagebox.showinfo("Erro", "Resistor em cima da fonte de tensão!")         
                        

        print(Resistência_Inválida)

        print(Resistores_Já_Inseridos_P1)
        print("\n")
        print(Resistores_Já_Inseridos_P2)
    except ValueError:     
        messagebox.showinfo("Erro", "Digite números válidos!")






def Atualizar_Preview(event=None):
    global linha_preview_id
    
    # Se já existir um preview na tela, apaga ele primeiro
    if linha_preview_id is not None:
        Tela.delete(linha_preview_id)
        linha_preview_id = None

    try:
        horizontal = False
        vertical = False
        negativo = False
        One_PontoProibido = False
        PontoProibido = False
        Resistor_Já_Inserido = False
        LinhaNoMeioDoResistor = False
        Linha_Embaixo_do_Resistor = False
        Linha_Dentro_De_Outra = False
        NaFonte = False
        TamanhoResistor = False

        Pontos_da_Linha.clear()
        # Tenta ler os dados dos inputs atuais
        x1 = int(Input_x1.get())
        y1 = int(Input_y1.get())
        x2 = int(Input_x2.get())
        y2 = int(Input_y2.get())
        
        xpc1 = x_origem + (x1 * escala)
        ypc1 = y_origem - (y1 * escala)
        xpc2 = x_origem + (x2 * escala)
        ypc2 = y_origem - (y2 * escala)



        if x1 == x2:
            vertical = True
        if y1 == y2:
            horizontal = True

        if (x1 - x2 == 2) or (x2 - x1 == 2):
            TamanhoResistor = True 

        if x1 < 0:
            negativo = True
        if x2 < 0:
            negativo = True
        if y1 < 0:
            negativo = True
        if y2 < 0:
            negativo = True

        for verificador3 in PontosOcupadosMeio:
            if ([x1, y1] == verificador3) or ([x2, y2] == verificador3):
                One_PontoProibido = True

        if One_PontoProibido == True:
            PontoProibido = True
        else:
            PontoProibido = False


        if (horizontal == True) and (vertical == False):
            if x1 > x2:
                Xmaior = x1
                Xmenor = x2

            if x1 < x2:
                Xmaior = x2
                Xmenor = x1    


            for xis in range(Xmenor, Xmaior + 1):
                Pontos_da_Linha.append([xis, y1])

            Linha_Dentro_De_Outra = all(item in Linhas_Horizontais for item in Pontos_da_Linha)    

            if any(item in PontosOcupadosMeio for item in Pontos_da_Linha):
                LinhaNoMeioDoResistor = True    



        if (horizontal == False) and (vertical == True):
            if y1 > y2:
                Ymaior = y1
                Ymenor = y2

            if y1 < y2:
                Ymaior = y2
                Ymenor = y1
    

            for yps in range(Ymenor, Ymaior + 1):
                Pontos_da_Linha.append([x1, yps])

            Linha_Dentro_De_Outra = all(item in Linhas_Verticais for item in Pontos_da_Linha)                


            if any(item in PontosOcupadosMeio for item in Pontos_da_Linha):
                LinhaNoMeioDoResistor = True         
        






        for P1, P2 in zip(Resistores_Já_Inseridos_P1, Resistores_Já_Inseridos_P2):
            if (P1 == [x1, y1]) and (P2 == [x2, y2]):
                Resistor_Já_Inserido = True
                break

            elif (P1 == [x2, y2]) and (P2 == [x1, y1]):
                Resistor_Já_Inserido = True
                break

            


        for i in range(len(Resistores_Já_Inseridos_P1)):
            if (Resistores_Já_Inseridos_P1[i] in Pontos_da_Linha) and (Resistores_Já_Inseridos_P2[i] in Pontos_da_Linha):
                Linha_Embaixo_do_Resistor = True
                break



        if (([x1, y1]) in Pontos_da_Fonte) or (([x2, y2]) in Pontos_da_Fonte) or (([(((x1+x2)/2)), (((y1+y2)/2))]) in Pontos_da_Fonte):
            NaFonte = True


        #Tela.create_oval(xpc1-3, ypc1-3, xpc1+3, ypc1+3, fill = "#67836F", outline ="#000000", width=2)


        if ((horizontal == True) or (vertical == True)) and ((negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (LinhaNoMeioDoResistor == False) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False)) and (TamanhoResistor == True):    
            linha_preview_id = Tela.create_line(xpc1, ypc1, xpc2, ypc2, fill="#00FF47", width=3, dash=(60, 10))
        elif ((horizontal == True) or (vertical == True)) and ((negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (LinhaNoMeioDoResistor == False) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False)) and (TamanhoResistor == False):    
            linha_preview_id = Tela.create_line(xpc1, ypc1, xpc2, ypc2, fill="#0938FF", width=3, dash=(60, 10))    
        else:
            linha_preview_id = Tela.create_line(xpc1, ypc1, xpc2, ypc2, fill="#FF0000", width=3, dash=(60, 10))

    except ValueError:
        pass




def Inserir_Linha():

    try:
        horizontal = False
        vertical = False
        negativo = False
        One_PontoProibido = False
        PontoProibido = False
        Resistor_Já_Inserido = False
        LinhaNoMeioDoResistor = False
        Linha_Embaixo_do_Resistor = False
        Linha_Dentro_De_Outra = False
        NaFonte = False

        Pontos_da_Linha.clear()

        x1 = int(Input_x1.get())
        y1 = int(Input_y1.get())

        x2 = int(Input_x2.get())
        y2 = int(Input_y2.get())

        if x1 == x2:
            vertical = True
        if y1 == y2:
            horizontal = True 

        if x1 < 0:
            negativo = True
        if x2 < 0:
            negativo = True
        if y1 < 0:
            negativo = True
        if y2 < 0:
            negativo = True

        for verificador3 in PontosOcupadosMeio:
            if ([x1, y1] == verificador3) or ([x2, y2] == verificador3):
                One_PontoProibido = True

        if One_PontoProibido == True:
            PontoProibido = True
        else:
            PontoProibido = False


        if (horizontal == True) and (vertical == False):
            if x1 > x2:
                Xmaior = x1
                Xmenor = x2

            if x1 < x2:
                Xmaior = x2
                Xmenor = x1    


            for xis in range(Xmenor, Xmaior + 1):
                Pontos_da_Linha.append([xis, y1])

            Linha_Dentro_De_Outra = all(item in Linhas_Horizontais for item in Pontos_da_Linha)    

            if any(item in PontosOcupadosMeio for item in Pontos_da_Linha):
                LinhaNoMeioDoResistor = True    



        if (horizontal == False) and (vertical == True):
            if y1 > y2:
                Ymaior = y1
                Ymenor = y2

            if y1 < y2:
                Ymaior = y2
                Ymenor = y1
    

            for yps in range(Ymenor, Ymaior + 1):
                Pontos_da_Linha.append([x1, yps])

            Linha_Dentro_De_Outra = all(item in Linhas_Verticais for item in Pontos_da_Linha)                


            if any(item in PontosOcupadosMeio for item in Pontos_da_Linha):
                LinhaNoMeioDoResistor = True         
        






        for P1, P2 in zip(Resistores_Já_Inseridos_P1, Resistores_Já_Inseridos_P2):
            if (P1 == [x1, y1]) and (P2 == [x2, y2]):
                Resistor_Já_Inserido = True
                break

            elif (P1 == [x2, y2]) and (P2 == [x1, y1]):
                Resistor_Já_Inserido = True
                break

            


        for i in range(len(Resistores_Já_Inseridos_P1)):
            if (Resistores_Já_Inseridos_P1[i] in Pontos_da_Linha) and (Resistores_Já_Inseridos_P2[i] in Pontos_da_Linha):
                Linha_Embaixo_do_Resistor = True
                break



        if (([x1, y1]) in Pontos_da_Fonte) or (([x2, y2]) in Pontos_da_Fonte) or (([(((x1+x2)/2)), (((y1+y2)/2))]) in Pontos_da_Fonte):
            NaFonte = True    


        print("horizontal:", horizontal)
        print("vertical:", vertical)
        print("negativo:", negativo)
        print("PontoProibido:", PontoProibido)
        print("LinhaNoMeioDoResistor:", LinhaNoMeioDoResistor)
        print("Linha_Embaixo_do_Resistor:", Linha_Embaixo_do_Resistor)
        print("Linha_Dentro_De_Outra:", Linha_Dentro_De_Outra)    

                                        

        if (horizontal == True) and (vertical == False) and (negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (LinhaNoMeioDoResistor == False) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False):
            Desenhar_Linha_Horizontal()
            

        if (horizontal == False) and (vertical == True) and (negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (LinhaNoMeioDoResistor == False) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False):
            Desenhar_Linha_Vertical()

                

        if (horizontal == True) and (vertical == True) and (negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (LinhaNoMeioDoResistor == False) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False):            
            messagebox.showinfo("Olá", "Pontos devem ser diferentes!")

        if (horizontal == False) and (vertical == False) and (negativo == False) and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (LinhaNoMeioDoResistor == False) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False):            
            messagebox.showinfo("Erro", "Linhas devem ser estar na vertical ou horizontal!")

        if (negativo == True)  and (PontoProibido == False) and (Resistor_Já_Inserido == False) and (LinhaNoMeioDoResistor == False) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False):
            messagebox.showinfo("Erro", "Digite somente números positivos!")

        if (PontoProibido == True) and (Resistor_Já_Inserido == False) and (LinhaNoMeioDoResistor == False) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False):
            messagebox.showinfo("Erro", "Resistor já inserido no meio do local!")

        if (Resistor_Já_Inserido == True) and (LinhaNoMeioDoResistor == False) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False):
            messagebox.showinfo("Erro", "Resistor já inserido no local!")

        if (LinhaNoMeioDoResistor == True) and (Linha_Embaixo_do_Resistor == False) and (Linha_Dentro_De_Outra == False) and (NaFonte == False):
            messagebox.showinfo("Erro", "Resistor já inserido no local, não pode!")

        if (Linha_Embaixo_do_Resistor == True) and (Linha_Dentro_De_Outra == False) and (NaFonte == False):
            messagebox.showinfo("Erro", "Linha abaixo de resistor, não pode!")

        if (Linha_Dentro_De_Outra == True) and (NaFonte == False):
            messagebox.showinfo("Erro", "Linha no mesmo local!")

        if (NaFonte == True):
            messagebox.showinfo("Erro", "Linha em cima da fonte de tensão!")                     

    except ValueError:
        messagebox.showinfo("Erro", "Digite números válidos!")        


Janela = tk.Tk()
Janela.title("ResistSIM")

Myframe = tk.Frame(Janela)
Myframe.grid(row = 0, column = 0)

def Limpar_Tudo():
    Tela.delete("InseridoPorUsuario")
    Resistores_Já_Inseridos_P1.clear()
    Resistores_Já_Inseridos_P2.clear()
    PontosOcupadosMeio.clear()
    Pontos_da_Linha.clear()
    Linhas_Total.clear()
    Linhas_Verticais.clear()
    Linhas_Horizontais.clear()
    Linha_Completa_Horizontal.clear()
    Linha_Atual_Horizontal.clear()
    Linha_Completa_Horizontal_Ordenada_Final.clear()
    Linha_Horizontal_Sem_Repetição.clear()
    Linha_Horizontal_Sem_Repetição_Final.clear()
    Lista_Guarda_H.clear()
    LinhaMesmoYFinal.clear()
    LinhaMesmoY2.clear()

def Desenhar_Linha_Horizontal():
    global Linha_Completa_Horizontal, Linha_Atual_Horizontal 
    global Linha_Horizontal_Somar, Linha_Completa_Horizontal_Ordenada 
    global Linha_Completa_Horizontal_Ordenada_Final, Linha_Horizontal_Sem_Repetição 
    global Linha_Horizontal_Sem_Repetição_Final, Lista_Guarda_H, LinhaMesmoYFinal, LinhaMesmoY2

    global linha_preview_id
    if linha_preview_id is not None:
        Tela.delete(linha_preview_id)
        linha_preview_id = None

    Lista_Guarda_H_Temp = []
    x1 = int(Input_x1.get())
    x2 = int(Input_x2.get())
    y = int(Input_y1.get())
    Linha_Completa_Horizontal.clear()
    Linha_Atual_Horizontal.clear()
    Linha_Horizontal_Somar.clear()
    Linha_Completa_Horizontal_Ordenada.clear()
    Linha_Completa_Horizontal_Ordenada_Final.clear()
    Linha_Horizontal_Sem_Repetição.clear()
    Linha_Horizontal_Sem_Repetição_Final.clear()
    Lista_Guarda_H_Temp.clear()
    LinhaMesmoY2.clear()
    interseção = False

    Xmenor = min(x1, x2)
    Xmaior = max(x1, x2)
    
    xpc1 = x_origem + (x1 * escala)
    ypc = y_origem - (y * escala)
    xpc2 = x_origem + (x2 * escala)


    Tag_Linha = f"linha_{Xmenor},{y};{Xmaior},{y}"
    linha_id = Tela.create_line(xpc1, ypc, xpc2, ypc, fill = "#000000", width = 3, tags = (Tag_Linha, "InseridoPorUsuario"))

    while len(Lista_Guarda_H) <= y:
        Lista_Guarda_H.append([])

    PontosUsuárioLinha = [Xmenor, Xmaior]
    Lista_Guarda_H[y].append([Xmenor, Xmaior])

    for xis in range(Xmenor, Xmaior + 1):
        Linha_Atual_Horizontal.append([xis, y])

    
    if any(ponto in Linhas_Horizontais for ponto in Linha_Atual_Horizontal): #interseção
        interseção = True
    #if interseção == True:


    mudou = True

    while mudou:
        mudou = False
        Lista_Guarda_H_Temp = [sub[:] for sub in Lista_Guarda_H]

        
        for verifica in Lista_Guarda_H_Temp[y]:
            if verifica == PontosUsuárioLinha:
                continue
            if (PontosUsuárioLinha[0] <= verifica[1]) and (PontosUsuárioLinha[1] > verifica[1]):
                Tela.delete(f"linha_{verifica[0]},{y};{verifica[1]},{y}")
                Tela.delete(f"linha_{PontosUsuárioLinha[0]},{y};{PontosUsuárioLinha[1]},{y}")

                #Lista_Guarda_H[y].remove([PontosUsuárioLinha[0], PontosUsuárioLinha[1]])
                #Lista_Guarda_H[y].remove([verifica[0], verifica[1]])
                if [PontosUsuárioLinha[0], PontosUsuárioLinha[1]] in Lista_Guarda_H[y]:
                    Lista_Guarda_H[y].remove([PontosUsuárioLinha[0], PontosUsuárioLinha[1]])

                if [verifica[0], verifica[1]] in Lista_Guarda_H[y]:
                    Lista_Guarda_H[y].remove([verifica[0], verifica[1]])

                if verifica[0] < PontosUsuárioLinha[0]:
                    xpc1MaisNovo = x_origem + (verifica[0] * escala)
                    ypc = y_origem - (y * escala)                        
                    xpc2MaisNovo = x_origem + (PontosUsuárioLinha[1] * escala)

                    Tag_Linha = f"linha_{verifica[0]},{y};{PontosUsuárioLinha[1]},{y}"
                    linha_id = Tela.create_line(xpc1MaisNovo, ypc + 20, xpc2MaisNovo, ypc + 20, fill = "#FF0000", width = 3, tags = (Tag_Linha, "InseridoPorUsuario"))
                    nova_linha = [verifica[0], PontosUsuárioLinha[1]]
                    Lista_Guarda_H[y].append([verifica[0], PontosUsuárioLinha[1]])
                else:
                    xpc1MaisNovo = x_origem + (PontosUsuárioLinha[0] * escala)
                    ypc = y_origem - (y * escala)
                    xpc2MaisNovo = x_origem + (PontosUsuárioLinha[1] * escala)

                    Tag_Linha = f"linha_{PontosUsuárioLinha[0]},{y};{PontosUsuárioLinha[1]},{y}"
                    linha_id = Tela.create_line(xpc1MaisNovo, ypc + 20, xpc2MaisNovo, ypc + 20, fill = "#FF0000", width = 3, tags = (Tag_Linha, "InseridoPorUsuario"))
                    nova_linha = [verifica[0], PontosUsuárioLinha[1]]
                    Lista_Guarda_H[y].append([PontosUsuárioLinha[0], PontosUsuárioLinha[1]])
                PontosUsuárioLinha = nova_linha   
                mudou = True
                break













            elif (verifica[0] <= PontosUsuárioLinha[1]) and (verifica[1] > PontosUsuárioLinha[1]):
                Tela.delete(f"linha_{verifica[0]},{y};{verifica[1]},{y}")
                Tela.delete(f"linha_{PontosUsuárioLinha[0]},{y};{PontosUsuárioLinha[1]},{y}")

                Lista_Guarda_H[y].remove([PontosUsuárioLinha[0], PontosUsuárioLinha[1]])                    
                Lista_Guarda_H[y].remove([verifica[0], verifica[1]])

                if verifica[0] < PontosUsuárioLinha[0]:
                    xpc1MaisNovo = x_origem + (verifica[0] * escala)
                    ypc = y_origem - (y * escala)
                    xpc2MaisNovo = x_origem + (verifica[1] * escala)

                    Tag_Linha = f"linha_{verifica[0]},{y};{verifica[1]},{y}"
                    linha_id = Tela.create_line(xpc1MaisNovo, ypc + 20, xpc2MaisNovo, ypc + 20, fill = "#FF0000", width = 3, tags = (Tag_Linha, "InseridoPorUsuario"))
                    nova_linha = [verifica[0], verifica[1]]
                    Lista_Guarda_H[y].append([verifica[0], verifica[1]])
                else:
                    xpc1MaisNovo = x_origem + (PontosUsuárioLinha[0] * escala)
                    ypc = y_origem - (y * escala)
                    xpc2MaisNovo = x_origem + (verifica[1] * escala)

                    Tag_Linha = f"linha_{PontosUsuárioLinha[0]},{y};{verifica[1]},{y}"
                    linha_id = Tela.create_line(xpc1MaisNovo, ypc + 20, xpc2MaisNovo, ypc + 20, fill = "#FF0000", width = 3, tags = (Tag_Linha, "InseridoPorUsuario"))
                    nova_linha = [PontosUsuárioLinha[0], verifica[1]]
                    Lista_Guarda_H[y].append([PontosUsuárioLinha[0], verifica[1]])
                PontosUsuárioLinha = nova_linha
                mudou = True
                break       





                #elif










        Linha_Horizontal_Somar = [xis for xis in Linhas_Horizontais if xis[1] == y]
        Linha_Completa_Horizontal = Linha_Horizontal_Somar + Linha_Atual_Horizontal
        #print(Linha_Completa_Horizontal)
        for eliminador in Linha_Completa_Horizontal:
            if (eliminador not in Linha_Horizontal_Sem_Repetição):
                Linha_Horizontal_Sem_Repetição.append(eliminador)
        Linha_Horizontal_Sem_Repetição_Final = sorted(Linha_Horizontal_Sem_Repetição, key= lambda ex: ex[0])

        if Linha_Completa_Horizontal:
            PXmenor = min(Linha_Completa_Horizontal, key= lambda ex: ex[0])
            PXmaior = max(Linha_Completa_Horizontal, key= lambda ex: ex[0])

            NewXmenor = PXmenor[0]
            NewXmaior = PXmaior[0]
            NewY = y
            #ListaNovaLinhaHorizontal[y].append([NewXmenor, NewXmaior])

        if len(Linha_Horizontal_Sem_Repetição_Final) < (NewXmaior - NewXmenor + 1):
            print("Mais de 1 linha")  
        else:         
            print("Só 1 linha")
          
           
            #New_Tag_Linha = f"linha_{NewXmenor},{y};{NewXmaior},{y}"
            #linha_id = Tela.create_line(xpc1, ypc + 10, xpc2, ypc + 10, fill = "#4C00FF", width = 3, tags = (New_Tag_Linha, "InseridoPorUsuario"))
            #Lista_Guarda_H[y].clear()
            #Lista_Guarda_H[y].append([NewXmenor, NewXmaior]) 

        print(f"Linha horizontal aumentada: {Linha_Horizontal_Sem_Repetição_Final}")
        

    """
    else: #sem interseção
        for testi in range(Xmenor, Xmaior + 1):
            Linhas_Horizontais.append([testi, y])
            print(linha_id)
        print(f"Linhas_Horizontais: {Linhas_Horizontais}")
        LinhaMesmoY = [p for p in Linhas_Horizontais if p[1] == y]
    """    
    for testi in range(Xmenor, Xmaior + 1):
        Linhas_Horizontais.append([testi, y])
        print(linha_id)
    print(f"Linhas_Horizontais: {Linhas_Horizontais}")
    LinhaMesmoY = [p for p in Linhas_Horizontais if p[1] == y]
    for eliminador in LinhaMesmoY:
        if (eliminador not in LinhaMesmoY2):
            LinhaMesmoY2.append(eliminador)
    LinhaMesmoYFinal = sorted(LinhaMesmoY2, key= lambda ex: ex[0])
    if len(LinhaMesmoYFinal) < (max(p[0] for p in LinhaMesmoYFinal)- min(p[0] for p in LinhaMesmoYFinal) + 1):
        print("Mais de 1 linha")  
    else:         
        print("Só 1 linha")
    print(f"LinhaMesmoY: {LinhaMesmoYFinal}")        
    

    
        
            

def Desenhar_Linha_Vertical():

    global Linha_Completa_Vertical, Linha_Atual_Vertical 
    global Linha_Vertical_Somar, Linha_Completa_Vertical_Ordenada 
    global Linha_Completa_Vertical_Ordenada_Final, Linha_Vertical_Sem_Repetição 
    global Linha_Vertical_Sem_Repetição_Final

    global linha_preview_id
    if linha_preview_id is not None:
        Tela.delete(linha_preview_id)
        linha_preview_id = None

    x = int(Input_x1.get())
    y1 = int(Input_y1.get())
    y2 = int(Input_y2.get())

    Linha_Completa_Vertical.clear()
    Linha_Atual_Vertical.clear()
    Linha_Vertical_Somar.clear()
    Linha_Completa_Vertical_Ordenada.clear()
    Linha_Completa_Vertical_Ordenada_Final.clear()
    Linha_Vertical_Sem_Repetição.clear()
    Linha_Vertical_Sem_Repetição_Final.clear()

    if y1 > y2:
        Ymaior = y1
        Ymenor = y2

    if y1 < y2:
        Ymaior = y2
        Ymenor = y1
    
    xpc = x_origem + (x * escala)
    ypc1 = y_origem - (y1 * escala)
    ypc2 = y_origem - (y2 * escala)

    Tag_Linha = f"linha_{Ymenor},{x};{Ymaior},{x}"

    
    linha_id = Tela.create_line(xpc, ypc1, xpc, ypc2, fill = "#000000", width = 3, tags = (Tag_Linha, "InseridoPorUsuario"))
    for yp in range(Ymenor, Ymaior + 1):
        Linha_Atual_Vertical.append([x, yp])
        #print(linha_id)   



    if any(ponto in Linhas_Verticais for ponto in Linha_Atual_Vertical):
        Linha_Vertical_Somar = [yp for yp in Linhas_Verticais if yp[0] == x]
        Linha_Completa_Vertical = Linha_Vertical_Somar + Linha_Atual_Vertical
        #print(Linha_Completa_Vertical)
        for eliminador in Linha_Completa_Vertical:
            if (eliminador not in Linha_Vertical_Sem_Repetição):
                Linha_Vertical_Sem_Repetição.append(eliminador)
        Linha_Vertical_Sem_Repetição_Final = sorted(Linha_Vertical_Sem_Repetição, key= lambda ex: ex[1])        

        print(f"Linha vertical aumentada: {Linha_Vertical_Sem_Repetição_Final}")

    for testi in range(Ymenor, Ymaior + 1):
        Linhas_Verticais.append([x, testi])
        print(linha_id)        
    

def Desenhar_Resistor_Horizontal():
    global linha_preview_id
    if linha_preview_id is not None:
        Tela.delete(linha_preview_id)
        linha_preview_id = None

    x1 = int(Input_x1.get())
    x2 = int(Input_x2.get())
    y = int(Input_y1.get())

    xpixel1 = x_origem + (x1 * escala)
    ypixel = y_origem - (y * escala)
    xpixel2 = x_origem + (x2 * escala)

    R = int(Input_Resistor.get())

    Delta = xpixel2 - xpixel1

    xp1R = xpixel1
    yp1R = ypixel

    xp2R = xp1R + (Delta * 0.2)
    yp2R = ypixel

    xp3R = xp1R + (Delta * 0.3)
    yp3R = ypixel - (0.5 * escala)

    xp4R = xp1R + (Delta * 0.4)
    yp4R = ypixel

    xp5R = xp1R + (Delta * 0.5)
    yp5R = ypixel - (0.5 * escala)

    Tela.create_text(xp5R, yp5R - (escala*0.25), text = (f"{R}Ω"), tag = "InseridoPorUsuario")

    xp6R = xp1R + (Delta * 0.6)
    yp6R = ypixel

    xp7R = xp1R + (Delta * 0.7)
    yp7R = ypixel - (0.5 * escala)

    xp8R = xp1R + (Delta * 0.8)
    yp8R = ypixel

    xp9R = xpixel2
    yp9R = ypixel

    x_ocupado = (x1 + x2)/2
    y_ocupado = y

    PontosOcupadosMeio.append([x_ocupado, y_ocupado])

    #for ([X, Y] in range(len(Linhas_Total))):
    #if (X, Y)
    

    Tela.create_line(xp1R, yp1R, xp2R, yp2R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp2R, yp2R, xp3R, yp3R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")
   
    Tela.create_line(xp3R, yp3R, xp4R, yp4R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp4R, yp4R, xp5R, yp5R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp5R, yp5R, xp6R, yp6R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp6R, yp6R, xp7R, yp7R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp7R, yp7R, xp8R, yp8R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp8R, yp8R, xp9R, yp9R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")













def Desenhar_Resistor_Vertical():
    global linha_preview_id
    if linha_preview_id is not None:
        Tela.delete(linha_preview_id)
        linha_preview_id = None

    x = int(Input_x1.get())
    y1 = int(Input_y1.get())
    y2 = int(Input_y2.get())

    ypixel1 = y_origem - (y1 * escala)
    xpixel = x_origem + (x * escala)
    ypixel2 = y_origem - (y2 * escala)

    R = int(Input_Resistor.get())

    Delta = ypixel2 - ypixel1

    xp1R = xpixel
    yp1R = ypixel1

    xp2R = xpixel
    yp2R = yp1R + (Delta * 0.2)

    xp3R = xpixel + (0.5 * escala)
    yp3R = yp1R + (Delta * 0.3)

    xp4R = xpixel
    yp4R = yp1R + (Delta * 0.4)

    xp5R = xpixel + (0.5 * escala)
    yp5R = yp1R + (Delta * 0.5)

    Tela.create_text(xp5R + (escala*0.33), yp5R, text = (f"{R}Ω"), tag = "InseridoPorUsuario")

    xp6R = xpixel
    yp6R = yp1R + (Delta * 0.6)

    xp7R = xpixel + (0.5 * escala)
    yp7R = yp1R + (Delta * 0.7)

    xp8R = xpixel
    yp8R = yp1R + (Delta * 0.8)

    xp9R = xpixel
    yp9R = ypixel2


    x_ocupado = x
    y_ocupado = (y1 + y2)/2


    PontosOcupadosMeio.append([x_ocupado, y_ocupado])


    Tela.create_line(xp1R, yp1R, xp2R, yp2R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp2R, yp2R, xp3R, yp3R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")
   
    Tela.create_line(xp3R, yp3R, xp4R, yp4R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp4R, yp4R, xp5R, yp5R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp5R, yp5R, xp6R, yp6R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp6R, yp6R, xp7R, yp7R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp7R, yp7R, xp8R, yp8R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")

    Tela.create_line(xp8R, yp8R, xp9R, yp9R, fill = "#000000", width = 3, tag = "InseridoPorUsuario")    
    

Info = tk.Label(Myframe, text = "P1 (x, y)")
Info.grid(row = 0, column = 0)

Input_x1 = tk.Entry(Myframe, width = 5)
Input_x1.grid(row = 0, column = 1)
Input_x1.bind("<KeyRelease>", Atualizar_Preview)

Info3 = tk.Label(Myframe, text = ",")
Info3.grid(row = 0, column = 2)

Input_y1 = tk.Entry(Myframe, width = 5)
Input_y1.grid(row = 0, column = 3)
Input_y1.bind("<KeyRelease>", Atualizar_Preview)

espaço = tk.Label(Myframe, text = "           ")
espaço.grid(row = 0, column = 4)

Info2 = tk.Label(Myframe, text = "P2 (x, y)")
Info2.grid(row = 0, column = 5)

Input_x2 = tk.Entry(Myframe, width = 5)
Input_x2.grid(row = 0, column = 6)
Input_x2.bind("<KeyRelease>", Atualizar_Preview)

Info3 = tk.Label(Myframe, text = ",")
Info3.grid(row = 0, column = 7)

Input_y2 = tk.Entry(Myframe, width = 5)
Input_y2.grid(row = 0, column = 8)
Input_y2.bind("<KeyRelease>", Atualizar_Preview)

espaço2 = tk.Label(Myframe, text = "           ")
espaço2.grid(row = 0, column = 9)

Info4 = tk.Label(Myframe, text = "Resistência (Ω)")
Info4.grid(row = 0, column = 10)

Input_Resistor = tk.Entry(Myframe, width = 5)
Input_Resistor.grid(row = 0, column = 11)

espaço3 = tk.Label(Myframe, text = "           ")
espaço3.grid(row = 0, column = 12)

botao2 = tk.Button(Myframe, text = "Inserir Resistor", command = Inserir_Resistor)
botao2.grid(row = 0, column = 13)

espaço4 = tk.Label(Myframe, text = "           ")
espaço4.grid(row = 0, column = 14)

botao3 = tk.Button(Myframe, text = "Inserir Linha", command = Inserir_Linha)
botao3.grid(row = 0, column = 15)

espaço5 = tk.Label(Myframe, text = "           ")
espaço5.grid(row = 0, column = 16)

botao4 = tk.Button(Myframe, text = "Limpar", command = Limpar_Tudo)
botao4.grid(row = 0, column = 17)


Tela = tk.Canvas(Janela, width = largura, height = altura, bg = "#ffffff")
Tela.grid(row = 1, column = 0)




Tela.create_line(0, y_origem, largura, y_origem, fill = "#000000", width = 2) #horizontal
Tela.create_line(x_origem, altura, x_origem, 0, fill = "#000000", width = 2) #vertical

for i in range(int(x_origem), int(largura), int(escala)):
    Tela.create_line(i, (y_origem + 7), i, (y_origem - 7), fill = "#252525", width = 2) #horizontal+

for i in range(int(y_origem), 0, int(-escala)):
    Tela.create_line((x_origem + 7), i, (x_origem - 7), i, fill = "#252525", width = 2) #vertical+


for i in range(int(x_origem), int(largura), int(escala)):
    Tela.create_line(i, altura, i, 0, fill = "#CFCFCF", width = 1) #horizontal+

for i in range(int(y_origem), 0, int(-escala)):
    Tela.create_line(0, i, largura, i, fill = "#CFCFCF", width = 1) #vertical+




for i in range(int(x_origem), 0, int(-escala)):
    Tela.create_line(i, (y_origem + 7), i, (y_origem - 7), fill = "#252525", width = 2) #horizontal-  

for i in range(int(y_origem), altura, int(escala)):
    Tela.create_line((x_origem + 7), i, (x_origem - 7), i, fill = "#252525", width = 2) #vertical-      


for i in range(int(x_origem) + escala, int(largura), int(escala)):
    Tela.create_text(i, y_origem + 15, text = int((i - x_origem)/escala)) #nº horizontal

for i in range(int(y_origem) - escala, 0, int(-escala)):
    Tela.create_text(x_origem - 15, i, text = int(-(i - y_origem)/escala)) #nº vertical            


Tela.create_text(x_origem - 10, y_origem + 10, text = 0)


for i in range(int(x_origem), 0, int(-escala)):
    Tela.create_line(i, altura, i, 0, fill = "#CFCFCF", width = 1) #horizontal-

for i in range(int(y_origem), altura, int(escala)):
    Tela.create_line(0, i, largura, i, fill = "#CFCFCF", width = 1) #vertical- 

ypixel1f = y_origem - (1 * escala)
xpixelf = x_origem + (1 * escala)
ypixel2f = y_origem - (2.93 * escala)

xtraco1pixel1f = x_origem + (0.65 * escala)
xtraco1pixel2f = x_origem + (1.35 * escala)
ytraco1pixelf = y_origem - (3.07 * escala)

xtraco2pixel1f = x_origem + (0.8 * escala)
xtraco2pixel2f = x_origem + (1.2 * escala)
ytraco2pixelf = y_origem - (2.93 * escala)


ypixel3f = y_origem - (3.07 * escala)
ypixel4f = y_origem - (5 * escala)

Tela.create_line(xpixelf, ypixel1f, xpixelf, ypixel2f, fill = "#000000", width = 3)
Tela.create_line(xtraco1pixel1f, ytraco1pixelf, xtraco1pixel2f, ytraco1pixelf, fill = "#000000", width = 3)
Tela.create_line(xtraco2pixel1f, ytraco2pixelf, xtraco2pixel2f, ytraco2pixelf, fill = "#000000", width = 3)

Tela.create_line(xpixelf, ypixel3f, xpixelf, ypixel4f, fill = "#000000", width = 3)


Janela.mainloop()
