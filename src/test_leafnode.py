import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Bold Text")
        self.assertEqual(node.to_html(), '<b>Bold Text</b>')

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "random text")
        self.assertEqual(node.to_html(), 'random text')


if __name__ == "__main__":
    unittest.main()