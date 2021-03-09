import unittest

from editDistance import editDistance

class TestEditDistance(unittest.TestCase):
    def test_equal(self):
        str1 = 'example'
        str2 = 'example'
        self.assertEqual(editDistance(str1, str2), 0, "example->example: 0")

    def test_simple(self):
        str1 = 'sunday'
        str2 = 'saturday'
        self.assertEqual(editDistance(str1, str2), 3, "sunday->saturday: 3")
        str1 = 'cat'
        str2 = 'cct'
        self.assertEqual(editDistance(str1, str2), 1, "cat->cct: 1")
        str1 = 'kitten'
        str2 = 'sitting'
        self.assertEqual(editDistance(str1, str2), 3, "kitten->sitting: 3")
        str1 = 'zzzzHEllooWurlld'
        str2 = 'HelloWorld'
        self.assertEqual(editDistance(str1, str2), 8, "zzzzHEllooWurlld->HelloWorld: 8")

    def test_gene(self):
        # example from https://www.cs.princeton.edu/courses/archive/spr05/cos126/assignments/sequence.html
        str1 = 'AACAGTTACC'
        str2 = 'TAAGGTCA'
        self.assertEqual(editDistance(str1, str2), 5, "AACAGTTACC->TAAGGTCA: 5")

    def test_empty(self):
        str1 = ''
        str2 = 'example'
        self.assertEqual(editDistance(str1, str2), len(str2), "\'\'->example: {:d}".format(len(str2)))
        str1 = 'example'
        str2 = ''
        self.assertEqual(editDistance(str1, str2), len(str1), "\'\'->example: {:d}".format(len(str1)))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestEditDistance('test_equal'))
    suite.addTest(TestEditDistance('test_simple'))
    suite.addTest(TestEditDistance('test_gene'))
    suite.addTest(TestEditDistance('test_empty'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())