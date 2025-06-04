import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", 'random paragraph text', props={"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("p", 'random paragraph text', props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_eq_2(self):
        node = HTMLNode("p", 'random paragraph text')
        node2 = HTMLNode("p", 'random paragraph text')
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_eq_3(self):
        node = HTMLNode("p", 'random paragraph text', props={"href": "https://www.google.com","target": "_blank",})
        node_str = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), node_str)

    def test_eq_4(self):
        node = HTMLNode("p", 'random paragraph text', props={"href": "https://www.google.com","target": "_blank",})
        node_repr = "HTMLNode(p, random paragraph text, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(node.__repr__(), node_repr)

    def test_not_eq(self):
        node = HTMLNode("p", 'random paragraph text', props={"href": "https://www.youtube.com","target": "_blank",})
        node2 = HTMLNode("p", 'random paragraph text', props={"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())


if __name__ == "__main__":
    unittest.main()