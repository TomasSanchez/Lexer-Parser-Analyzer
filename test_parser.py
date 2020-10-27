import unittest
import parser
import lexer

#accepted list of tokens
token0 =  'id1 := \'string1\' ; mientras id2 hacer id3 := 32'
token1 = 'mientras mostrar \'string1\' id1 hacer id2 := 8'
token2 = 'si 1  entonces id1 := \'string1\''
token3 = 'id1 := 123 [ id2 ]'
token4 = 'id1 := 1 + 1'
token5 = ' si 5 > 4 entonces id1 := 4 sino id2 := \'string1\''

#rejected list of tokens
token6 = 'id1 := 1 \'string1\' 1'
token7 = 'id1 := \'1\' =='
token8 = 'si 11 entonces id1 sino'
token9 = 'mientras aceptar hacer id1 := 1'

class TestParser(unittest.TestCase):

	def test_accepted0(self):
		self.assertTrue(parser.Parser(token0))
		
	def test_accepted1(self):
		self.assertTrue(parser.Parser(token1))

	def test_accepted2(self):
		self.assertTrue(parser.Parser(token2))

	def test_accepted3(self):
		self.assertTrue(parser.Parser(token3))

	def test_accepted4(self):
		self.assertTrue(parser.Parser(token4))

	def test_accepted5(self):
		self.assertTrue(parser.Parser(token5))

	def test_accepted6(self):
		self.assertFalse(parser.Parser(token6))

	def test_accepted7(self):
		self.assertFalse(parser.Parser(token7))

	def test_rejected8(self):
		self.assertFalse(parser.Parser(token8))

	def test_rejected9(self):
		self.assertFalse(parser.Parser(token9))

	
if __name__ == '__main__':
    unittest.main()

