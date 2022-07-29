from typing import Callable, Iterable, List, Sequence, Union, Tuple, Dict, NewType

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Gabriel Rocha'

# Sequências
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Gabriel']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Gabriel')

# Dicionarios e Conjuntos

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]

pessoa: Dict[str, Union[str, int]] = {'nome': 'Gabriel Rocha',
                                      'sobrenome': 'Silva',
                                      'idade': 30}

ppessoa2: MeuDict = {'nome': 'Gabriel Rocha',
                     'sobrenome': 'Silva',
                     'idade': 30,
                     'l': [1, 2]}

# Meu tipo

UserId = NewType('UserId', int)
user_id = UserId(232213213)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def soma(x: int, y: int) -> int:
    return(x + y)


print(retorna_funcao(soma)(10, 20))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} esta falando...')


def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar([1, 2, 3]))
print(iterar2([1, 2, 3]))
print(iterar2([5, 6, 7]))
