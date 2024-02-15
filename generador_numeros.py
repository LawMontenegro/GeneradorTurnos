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
              

contador_perfumeria = area_perfumeria()
contador_farmacia = area_farmacia()
contador_cosmetica = area_cosmetica()


   


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
    
        print("\n"+"*"*25)
        print("Su turno es:")
        
        
        if funcion_generadora == "P":
            print(next(contador_perfumeria))
        elif funcion_generadora == "F":
            print(next(contador_farmacia))
        else:
            print(next(contador_cosmetica))
            
            
        print("Por favor, espere a ser atendido.") 
        
    

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






  
