import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD, 'link.com')
        node2 = TextNode("This is a text node", TextType.BOLD, 'link.com')
        self.assertEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = TextNode("This is NOT a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_3(self):
        node = TextNode("This is a text node", TextType.BOLD, 'link.com')
        node2 = TextNode("This is a text node", TextType.BOLD, 'link2.com')
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()