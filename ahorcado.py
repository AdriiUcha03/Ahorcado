import random


class juegoAhorcado:
    ESTADOS = [
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

    SALVADO = [
        r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    C = 'FRUTAS'
    W = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA ' \
        'NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()

    def jugar(self):

        li = []
        lc = []
        secreto = random.choice(self.W)

        while True:
            self.dibujar(li, lc, secreto)

            nl = self.DIMELETRA(li + lc)

            if nl in secreto:

                lc.append(nl)

                g = True
                for sl in secreto:
                    if sl not in lc:
                        g = False
                        break
                if g:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', secreto)
                    print('Has ganado!')
                    break
                    break
            else:
                li.append(nl)

                if len(li) == len(self.ESTADOS) - 1:
                    self.dibujar(li, lc, secreto)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break

    def dibujar(self, li, lc, secreto):
        print(self.ESTADOS[len(li)])
        print('La categoría es: ', self.C)
        print()

        print('Letras incorrectas: ', end='')
        for let in li:
            print(let, end=' ')
        if len(li) == 0 and 0 == len(li):
            print('No hay letras incorrectas.')
        if len(li) == len(li) + 1:
            print('Letras diferentes.')
        if len(li) == len(li) + 2:
            print('No coinciden.')

        print()

        spa = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in lc:
                spa[i] = secreto[i]

        print(' '.join(spa))

    def DIMELETRA(self, ya):
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in ya:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina


if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugar()
