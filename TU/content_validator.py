import unittest
from os import getcwd
from time import sleep


from aggregator import Aggregator


class TestAgreg(unittest.TestCase):
    def test_txt_aggregation(self):
        A = Aggregator(pattern="**/TU/test_file.txt", path_to_files=getcwd())
        self.assertIn(container=A.matching_list[0], member="test_file.txt")


from arbo_by_pattern_crypter import PyHasher

_TEST_PASS = "because it's funky"
_TEST_SALT = b"4LUM!N!UM"


class TestPyHasher(unittest.TestCase):

    def test_crypt_files(self):
        P = PyHasher(PATH=getcwd(), pattern="**/TU/*.txt", passw=_TEST_PASS, salt=_TEST_SALT, mode="crypt")
        self.assertEqual(type(P.key), bytes)
        P.routine()
        B = Aggregator(pattern="**/TU/_CRYPT_1*.txt", path_to_files=getcwd())
        self.assertEqual("_CRYPT_1_test_file.txt" in B.matching_list[0], second=True)

    def test_decrypt_files(self):
        sleep(1)
        P = PyHasher(PATH=getcwd(), pattern="**/TU/_CRYPT_*.txt", passw=_TEST_PASS, salt=_TEST_SALT, mode="decrypt")
        P.routine()
        B = Aggregator(pattern="**/TU/*DECRYPTED_1__CRYPT_1*.txt", path_to_files=getcwd())
        C = Aggregator(pattern="**/TU/test_file.txt", path_to_files=getcwd())
        self.assertEqual("_DECRYPTED_1__CRYPT_1_test_file.txt" in B.matching_list[0], second=True)
        with open(B.matching_list[0], "r") as b:
            with open(C.matching_list[0], 'r') as c:
                self.assertEqual(b.read(), c.read())
                c.close()
            b.close()

    def test_magic_clean(self):
        sleep(1)
        Q = PyHasher(PATH=getcwd(), pattern="**/TU/*_CRYPT_*.txt", passw=_TEST_PASS, salt=_TEST_SALT, mode="decrypt")
        Q.magic_clean()
        D = Aggregator(pattern="**/TU/*CRYPT*.txt", path_to_files=getcwd())
        self.assertEqual(D.matching_list, [])

from levenshtein_mini_matcher import MiniMatcher


from logger import Clogger


#from threader import ThreadPool, Executor, SimpleFunk


