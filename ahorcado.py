import random
import sys


class juegoAhorcado:
    """
    .. include:: ./README.md
    """
    def __init__(self, fnombre):
        """
        Inicializador de la clase
        :param fnombre: Parametro del nombre que se pasa a la clase.
        """
        self.nombre = fnombre

    lista_estado_ahorcado = [
        r"""
     +--+
     |  |
        |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    salvado = [
        r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    """
    :param n_random: Numero aleatorio entre 0,1,2.
    """
    n_ramdom = random.randint(0, 2)
    pista1 = 'FRUTAS'
    lista_frutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON ' \
                   'MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()
    pista2 = 'MARCAS DE COCHE'
    lista_marcas = 'MCLAREN MERCEDES FORD FERRARI LAMBORGHINI RENAULT ALPINE NISSAN DACIA PEUGOT' \
                   'ALFAROMEO AUDI VOLKSWAGEN FIAT SANYONG HONDA HYUNDAI KOENIGSEGG BUGATTI'.split()
    pista3 = 'MARCAS PC'
    lista_pc = 'MSI RAZER ACER LENOVO PAVILION OMEN ASUS APPLE CORSAIR TRUST MICROSOFT LOGITECH'.split()
    lista = [lista_frutas, lista_marcas, lista_pc]
    # Así selecionamos una de las listas y la pista en base a la lista a usar que haya tocado
    """
    :param lista_usar: Lista seleccionada de forma aleatoria
    """
    lista_usar = lista[n_ramdom]
    if lista_usar == lista_frutas:
        pista = pista1
    elif lista_usar == lista_marcas:
        pista = pista2
    if lista_usar == lista_pc:
        pista = pista3

    def jugar(self):
        """
        Funcion en la que comprobamos los intentos que se van haciendo hasta que se averigua la palabara de la lista
        o se pierde
        """
        letras_incorrectas = []
        letras_correctas = []
        p_secreta = random.choice(self.lista_usar)

        while True:
            self.dibujar(letras_incorrectas, letras_correctas, p_secreta)

            letra_intento = self.pedir_letra(letras_incorrectas + letras_correctas)

            if letra_intento in p_secreta:

                letras_correctas.append(letra_intento)

                ganar = True
                for seccion_letra_correcta in p_secreta:
                    if seccion_letra_correcta not in letras_correctas:
                        ganar = False
                        break
                if ganar:
                    print(self.salvado[0])
                    print('¡Bien hecho! la palabra secreta es :', p_secreta)
                    print('Has ganado ' + self.nombre + '!')
                    break
            else:
                letras_incorrectas.append(letra_intento)

                if len(letras_incorrectas) == len(self.lista_estado_ahorcado) - 1:
                    self.dibujar(letras_incorrectas, letras_correctas, p_secreta)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(p_secreta))
                    break

    def dibujar(self, letras_incorrectas, letras_correctas, p_secreta):
        """
        Donde vamos viendo los intentos que vamos realizando y las letras que vamos intentando
        :param letras_incorrectas: Lista que almacena el conjunto de letras incorrectas que se introducen en
        los intentos
        :param letras_correctas: Lista que modifica los espacios por las letras que se van acertando
        :param p_secreta: Palabra seleccionada de la lista aleatoria
        """
        print(self.lista_estado_ahorcado[len(letras_incorrectas)])
        print('La categoría es: ', self.pista)
        print()

        print('Letras incorrectas: ', end='')
        for let in letras_incorrectas:
            print(let, end=' ')
        if len(letras_incorrectas) == 0 and 0 == len(letras_incorrectas):
            print('No hay letras incorrectas.')
        if len(letras_incorrectas) == len(letras_incorrectas) + 1:
            print('Letras diferentes.')
        if len(letras_incorrectas) == len(letras_incorrectas) + 2:
            print('No coinciden.')

        print('\nIntento ' + str(len(letras_incorrectas)+1) + ' te quedan ' +
              str((len(self.lista_estado_ahorcado)-len(letras_incorrectas))-1) + ' intentos')

        print()

        espacios = ['_'] * len(p_secreta)

        for huecos in range(len(p_secreta)):
            if p_secreta[huecos] in letras_correctas:
                espacios[huecos] = p_secreta[huecos]

        print(' '.join(espacios))

    @staticmethod
    def pedir_letra(ya):
        """
        Función donde pedimos la letra y le hacemos un chequeo de condiciones.
        :param ya: Paramatro ya sirve para comparar las letras que ya se han introducido, es decir que ya sabemos
        :return letra_intento: Si no se cumple ninguna condición if entonces pasa al else que retorna la letra_intento
        """
        while True:
            print('Adivina una letra.')
            letra_intento = input('> ').upper()
            if letra_intento == 'TERMINAR':
                sys.exit("Programa Finalizado")
            if len(letra_intento) != 1:
                print('Introduce una única letra.')
            elif letra_intento in ya:
                print('Esa letra_intento ya la sabías. Elige otra vez.')
            elif not letra_intento.isalpha():
                print('Introduce una LETRA.')

            else:
                return letra_intento


if __name__ == '__main__':
    nombre = str(input("Dime tu nombre: "))
    juego1 = juegoAhorcado(nombre)
    juego1.jugar()
