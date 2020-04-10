import unittest
import goneirossPy

class TestAlgebra(unittest.TestCase):
    def setup(self):
        self.A = [[1,2,3],[4,5,6],[7,8,9]]
        self.b = [1,2,3]
        self.A2 = [[1,2,3],[0,-2,-3],[0,0,0]]
    def test_gauss(self):
        g = algebra.gauss(self.A,self.b)
        self.assertEqual(self.A,self.A2)

if __name__ == '__main__':
    unittest.main()