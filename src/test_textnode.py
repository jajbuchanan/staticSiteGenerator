import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", "bold", url="https://example.com")
        node2 = TextNode("This is a text node", "bold", url="https://example.com")
        self.assertEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("This is a text node", "bold", url="https://example.com")
        node2 = TextNode("This is a text node", "bold", url="https://different.")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
