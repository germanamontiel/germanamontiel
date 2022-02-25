import random
import csv

def read_csv():
    
    csvfile = open('cine_lista.csv')
    
    trivia = list(csv.DictReader(csvfile))
    ancho = -1
    largo = int(len(trivia))
    numero_random = random.randint(ancho,largo)
    print('')
    print(' En la pelicula', trivia[numero_random]["b"])
    print('')
    print('*', trivia[numero_random]["c"])
    print('')
    print(' 1.', trivia[numero_random]["d"])
    print(' 2.', trivia[numero_random]["e"])
    print(' 3.', trivia[numero_random]["f"])
    print(' 4.', trivia[numero_random]["g"])
    print(' 5.', trivia[numero_random]["h"])
    
    csvfile.close()
     
def write_csv(nombre, resultado_final):
    
    csvfile = open('jugadores_trivia.csv', 'w', newline='')

    header = ['name', 'resultado']
    
    writer = csv.DictWriter(csvfile, fieldnames=header)

    writer.writeheader()

    fila = {}
    fila['name'] = nombre
    fila['resultado'] = resultado_final
    writer.writerow(fila)
    
    csvfile.close()

def game_on():

        print('')
        nuevo_jugador = str(input('Ingrese su nombre: '))
        nuevo = nuevo_jugador
        print('')
        print(nuevo, 'esta listo para jugar!!')
        return nuevo
                               
def preguntas():

    print('')
    numero = int(input('Ingrese cantidad de preguntas a responder: '))    
    cantidad_nueva = numero
    return cantidad_nueva     

def respuesta(eleccion, resultado):

    suma_total = resultado
    incorrecto = 0
    correcto = 0
    
    if eleccion == 1:
        print('')
        
        
        incorrecto -= 2
        
    elif eleccion == 2:
        print('')
        
        incorrecto -= 2        

    elif eleccion == 3:
        print('')
        
        incorrecto -= 2

    elif eleccion == 4:
        print('')
        
        incorrecto -= 2

    elif eleccion == 5:
        print('')
        
        correcto += 5

    else:
        print('')
        print('Creo que estas perdiendo tu tiempo')
    
    if incorrecto <= 4:
        suma_total = "Perdiste"
        return suma_total

    elif correcto >= 5:
        suma_total = 'Ganaste'
        return suma_total
    else:
        print('Sigue participando, muchas gracias por jugar')
        
if __name__ == '__main__':
    
    print('Bienvenido a mi nuevo juego')
    valor = ''
    print('')
    valor = str(input('Desea jugar si/no? '))

    while valor == 'si':
        
            nombre = game_on()
            cantidad = preguntas()
        
            print('Elegiste responder', cantidad, 'preguntas') 
          
            while cantidad > 0 and cantidad < 10:
                cantidad -= 1
                read_csv()
                                
                print('')
                eleccion_jugador = int(input('Ingrese opcion correcta: '))        

            else:

                resultado = 0  
                resultado_final = 0
                resultado_final = respuesta(eleccion_jugador, resultado)   
                                           
                write_csv(nombre, resultado_final)
                
                print('')
                print('Tu', resultado_final, 'esta partida, vuelve a intentarlo')
    else:
        print('Gracias por jugar')         
 

