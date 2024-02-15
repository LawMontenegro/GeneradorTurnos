import generador_numeros


def volver_inicio():
    print("¿Desea solicitar otro turno? (s/n)")
    opc = input('').lower()
    if opc == 's':
        elegir_categoria()
    if opc == 'n':
        print("¡Gracias por visitar Drogeria Esquina!")


    
    
def bienvenida():
    print("*"*25)
    print("Bienvenida a la Drogeria Esquinera\n")
    elegir_categoria()
    volver_inicio()


def elegir_categoria():
    
    while True:
        print(" [p]-Perfumeria\n [F]-Farmacia \n [C]-Cosmetica")
        try:
            mi_turno = input("¿Qué área desea ser atendido? \n").upper()
            ['P','F','C'].index(mi_turno)
            
        except ValueError:
            print("esa no es una opcion valida")
        except TypeError:
            print("esperas algun argumento y no hay nada?")
        else:
            break
        
    generador_numeros.decorador_servicio(mi_turno)
    generador_numeros.memoria_generador(mi_turno)
        
       
     
        



#if __name__==__main__:
    
bienvenida()
