"""

* Assignment: OOP Slots Define
* Complexity: easy
* Lines of code: 11 lines
* Time: 13 min

English:
    1. Use code from "Input" section (see below)
    2. Define class `Iris` with attributes: `sepal_length, sepal_width, petal_length, petal_width, species`
    3. All attributes must be in `__slots__`
    4. Define method `__repr__` which prints class name and all values positionally, ie. `Iris(5.8, 2.7, 5.1, 1.9, 'virginica')`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Input" (patrz poniżej)
    2. Zdefiniuj klasę `Iris` z atrybutami: `sepal_length, sepal_width, petal_length, petal_width, species`
    3. Wszystkie atrybuty muszą być w `__slots__`
    4. Zdefiniuj metodę `__repr__` wypisującą nazwę klasy i wszystkie wartości atrybutów pozycyjnie, np. `Iris(5.8, 2.7, 5.1, 1.9, 'virginica')`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> result = [Iris(*row) for row in DATA[1:]]
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
     Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
     Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
     Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
     Iris(6.4, 3.2, 4.5, 1.5, 'versicolor'),
     Iris(4.7, 3.2, 1.3, 0.2, 'setosa')]

    >>> iris = result[0]
    >>> iris
    Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

    >>> iris.__slots__
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

    >>> [getattr(iris, x) for x in iris.__slots__]
    [5.8, 2.7, 5.1, 1.9, 'virginica']

    >>> {x: getattr(iris, x) for x in iris.__slots__}
    {'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'}

    >>> iris.__dict__
    Traceback (most recent call last):
    AttributeError: 'Iris' object has no attribute '__dict__'

    >>> values = tuple(getattr(iris, x) for x in iris.__slots__)
    >>> print(f'Iris{values}')
    Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

Hint:
    * In `__repr__()` use tuple comprehension to get `self.__slots__` values
"""


# Given
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]


# Solution
class Iris:
    __slots__ = ('sepal_length', 'sepal_width', 'petal_length',
                 'petal_width', 'species')

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def __repr__(self):
        values = tuple(getattr(self, x) for x in self.__slots__)
        return f'Iris{values}'
