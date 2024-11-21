import random

class BingoCage:
    
    def __init__(self,items) -> None:
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self):
        return self.pick()

    
if __name__=='__main__':
    # Criando uma instancia de BingoCage com uma range de 0 - 3
    bingo = BingoCage(range(3))

    # Capiturando um item da lista
    print(bingo.pick())

    # Capiturando outro item da lista chamando a propria instancia
    print(bingo())

    # Certificando que a instancia de BingoCage pode ser chamada
    print(callable(bingo))