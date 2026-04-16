class Vector:
    vector = []

    def __init__(self, numeros):
        self.vector = [numero for numero in numeros]

    def __repr__(self):
        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        str_ = '['
        for componente in self.vector:
            str_ += ' ' + str(componente)
        str_ += ' ]'
        return str_

    def __eq__(self, other):
        return isinstance(other, Vector) and self.vector == other.vector

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.vector, other.vector)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.vector, other.vector)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([a * other for a in self.vector])
        elif isinstance(other, Vector):
            return Vector([a * b for a, b in zip(self.vector, 
other.vector)])
        else:
            raise TypeError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __matmul__(self, other):
        if not isinstance(other, Vector):
            raise TypeError
        return sum(a * b for a, b in zip(self.vector, other.vector))

    def __floordiv__(self, other):
        dot = self @ other
        norm_sq = other @ other
        factor = dot / norm_sq
        return other * factor

    def __mod__(self, other):
        return self - (self // other)


import unittest

class TestVector(unittest.TestCase):

    def test_multiplicacion(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])

        self.assertEqual(v1 * 2, Vector([2, 4, 6]))
        self.assertEqual(v1 * v2, Vector([4, 10, 18]))

    def test_producto_escalar(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])

        self.assertEqual(v1 @ v2, 32)

    def test_componentes(self):
        v1 = Vector([2, 1, 2])
        v2 = Vector([0.5, 1, 0.5])

        self.assertEqual(v1 // v2, Vector([1.0, 2.0, 1.0]))
        self.assertEqual(v1 % v2, Vector([1.0, -1.0, 1.0]))


if __name__ == "__main__":
    unittest.main()

        

    
    
