import unittest
from lab3 import DoublyLinked, Sentinel

class TestDoublyLinked(unittest.TestCase):

    def test_push_front(self):
        dll = DoublyLinked()
        dll.push_front(10)
        self.assertEqual(dll.get_front().get_data(), 10)
        dll.push_front(20)
        self.assertEqual(dll.get_front().get_data(), 20)
        self.assertEqual(dll.get_back().get_data(), 10)

    def test_push_back(self):
        dll = DoublyLinked()
        dll.push_back(30)
        self.assertEqual(dll.get_back().get_data(), 30)
        dll.push_back(40)
        self.assertEqual(dll.get_back().get_data(), 40)
        self.assertEqual(dll.get_front().get_data(), 30)

    def test_pop_front(self):
        dll = DoublyLinked()
        dll.push_back(50)
        dll.push_back(60)
        val = dll.pop_front()
        self.assertEqual(val, 50)
        self.assertEqual(dll.get_front().get_data(), 60)

    def test_pop_back(self):
        dll = DoublyLinked()
        dll.push_front(70)
        dll.push_front(80)
        val = dll.pop_back()
        self.assertEqual(val, 70)
        self.assertEqual(dll.get_back().get_data(), 80)

    def test_pop_front_empty(self):
        dll = DoublyLinked()
        with self.assertRaises(IndexError):
            dll.pop_front()

    def test_pop_back_empty(self):
        dll = DoublyLinked()
        with self.assertRaises(IndexError):
            dll.pop_back()

class TestSentinel(unittest.TestCase):

    def test_push_front(self):
        sll = Sentinel()
        sll.push_front(100)
        self.assertEqual(sll.get_front().get_data(), 100)
        sll.push_front(110)
        self.assertEqual(sll.get_front().get_data(), 110)
        self.assertEqual(sll.get_back().get_data(), 100)

    def test_push_back(self):
        sll = Sentinel()
        sll.push_back(200)
        self.assertEqual(sll.get_back().get_data(), 200)
        sll.push_back(210)
        self.assertEqual(sll.get_back().get_data(), 210)
        self.assertEqual(sll.get_front().get_data(), 200)

    def test_pop_front(self):
        sll = Sentinel()
        sll.push_back(300)
        sll.push_back(310)
        val = sll.pop_front()
        self.assertEqual(val, 300)
        self.assertEqual(sll.get_front().get_data(), 310)

    def test_pop_back(self):
        sll = Sentinel()
        sll.push_front(400)
        sll.push_front(410)
        val = sll.pop_back()
        self.assertEqual(val, 400)
        self.assertEqual(sll.get_back().get_data(), 410)

    def test_pop_front_empty(self):
        sll = Sentinel()
        with self.assertRaises(IndexError):
            sll.pop_front()

    def test_pop_back_empty(self):
        sll = Sentinel()
        with self.assertRaises(IndexError):
            sll.pop_back()

if __name__ == '__main__':
    unittest.main()
