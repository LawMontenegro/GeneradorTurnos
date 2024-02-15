'''
Codigo para generar numeros de turnos dentro de una  farmacia

'''


lista_categorias = ["Perfumeria", "Farmacia", "Cosmeticos"]

def area_perfumeria():
    for turno in range(1,10000):
        yield f"P-{turno}"
        
def area_farmacia():
    for turno in range(1,10000):
        yield f"F-{turno}"
        
def area_cosmetica():
    for turno in range(1,10000):
        yield f"C-{turno}"
              



   
def elegir_categoria():
    categoria = "x"
    while not categoria.isnumeric() or int(categoria) not in range(1, len(lista_categorias) + 1):
        for item, x in enumerate(lista_categorias):
            print(f"[{item+1}]-{x} ")
        categoria = input('')
    return lista_categorias[int(categoria)-1]

def generador_turno(categoria):

    
    @memoria_generador
    @decorador_servicio
    def generador_perfumeria():
        num = 1
        while num < 101:
            yield num
            num += 1
    
    @memoria_generador
    @decorador_servicio
    def generador_farmacia():
        num = 1
        while num < 101:
            yield num
            num += 1
    
    @memoria_generador
    @decorador_servicio 
    def generador_cosmetica():
        num = 1
        while num < 101:
            yield num
            num += 1
    
    if categoria == "Perfumeria":
        
        print(f"P-{next(generador_perfumeria)}")

    elif categoria == "Farmacia":

        print(f"F-{next(generador_farmacia)}")

    elif categoria == "Cosmeticos":
        print(f"C-{next(generador_cosmetica)}")
    
    volver_inicio()
    



def decorador_servicio(funcion_generadora):
    def envoltura():
        print("Su turno es:")
        generador = funcion_generadora()
        for elemento in generador:
            yield elemento
        print("Por favor, espere a ser atendido.") 
        
    return envoltura

def memoria_generador(generator_func):
    generator = generator_func()
    memo = None
    while True:
        try:
            if memo is None:
                memo = next(generator)
            else:
                yield memo
                memo = None
        except StopIteration:
            generator = generator_func()
            memo = None

def volver_inicio():
    print("¿Desea solicitar otro turno? (s/n)")
    opc = input('').lower()
    if opc == 's':
        categoria_seleccionada = elegir_categoria()
        generador_turno(categoria_seleccionada)
    if opc == 'n':
        print("¡Gracias por visitar Drogeria Esquina!")

def bienvenida():
    print("Bienvenida a la Drogeria Esquinera")
    print("¿Qué área desea atender? \n")




  
    
bienvenida()
categoria_seleccionada = elegir_categoria()
generador_turno(categoria_seleccionada)