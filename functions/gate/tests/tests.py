from unittest import TestCase
from functions.gate import *
from functions.print_log import log_info

#----------------------------------------------------------------------#
# Unittest
#----------------------------------------------------------------------#
def setUpModule():
    log_info('Test Gate: setUpModule')

def tearDownModule():
        log_info('Test Gate: tearDownModule')

class TestGate(TestCase):
    def setUp(self):
        log_info('Test Gate: setUp')

    def tearDown(self):
        log_info('Test Gate: tearDown')

    def test_or1(self):
        """ OR回路 """
        log_info("test_or")
        self.assertEqual(or_gate(0, 0), 0)

    def test_or2(self):
        """ OR回路 """
        log_info("test_or")
        self.assertEqual(or_gate(1, 0), 1)

    def test_or3(self):
        """ OR回路 """
        log_info("test_or")
        self.assertEqual(or_gate(0, 1), 1)

    def test_or4(self):
        """ OR回路 """
        log_info("test_or")
        self.assertEqual(or_gate(1, 1), 1)

    def test_and1(self):
        """ AND回路 """
        log_info("test_and")
        self.assertEqual(and_gate(0, 0), 0)

    def test_and2(self):
        """ AND回路 """
        log_info("test_and")
        self.assertEqual(and_gate(1, 0), 0)

    def test_and3(self):
        """ AND回路 """
        log_info("test_and")
        self.assertEqual(and_gate(0, 1), 0)

    def test_and4(self):
        """ AND回路 """
        log_info("test_and")
        self.assertEqual(and_gate(1, 1), 1)

    def test_nand1(self):
        """ NAND回路 """
        log_info("test_nand")
        self.assertEqual(nand_gate(0, 0), 1)

    def test_nand2(self):
        """ NAND回路 """
        log_info("test_nand")
        self.assertEqual(nand_gate(1, 0), 1)

    def test_nand3(self):
        """ NAND回路 """
        log_info("test_nand")
        self.assertEqual(nand_gate(0, 1), 1)

    def test_nand4(self):
        """ NAND回路 """
        log_info("test_nand")
        self.assertEqual(nand_gate(1, 1), 0)

    def test_xor1(self):
        """ XOR回路 """
        log_info("test_xor")
        self.assertEqual(xor_gate(0, 0), 0)

    def test_xor2(self):
        """ XOR回路 """
        log_info("test_xor")
        self.assertEqual(xor_gate(1, 0), 1)

    def test_xor3(self):
        """ XOR回路 """
        log_info("test_xor")
        self.assertEqual(xor_gate(0, 1), 1)

    def test_xor4(self):
        """ XOR回路 """
        log_info("test_xor")
        self.assertEqual(xor_gate(1, 1), 0)
