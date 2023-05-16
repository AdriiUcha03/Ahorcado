import random


class juegoAhorcado:
    def __init__(self, fnombre):
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

    pista = 'FRUTAS'
    lista_frutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON ' \
                   'MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()

    def jugar(self):

        letras_incorrectas = []
        letras_correctas = []
        p_secreta = random.choice(self.lista_frutas)

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
        while True:
            print('Adivina una letra.')
            letra_intento = input('> ').upper()
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
