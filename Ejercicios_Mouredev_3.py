'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 '''

def poligono(figura):
    ancho = int(input('Introduce el ancho de la figura: '))
    alto = int(input('Introduce el alto de la figura: '))
    resultado = ancho * alto
    print (f'El área es {ancho} * {alto}', '=',resultado)

poligono('rectángulo')
