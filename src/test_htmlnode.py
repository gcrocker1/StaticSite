import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", 'random paragraph text', props={"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("p", 'random paragraph text', props={"href": "https://www.google.com","target": "_blank",})
        node_str = node.props_to_html()
        node2_str = node2.props_to_html()
        print(node)
        print(node_str)
        self.assertEqual(node_str, node2_str)

    def test_eq_2(self):
        node = HTMLNode("p", 'random paragraph text')
        node2 = HTMLNode("p", 'random paragraph text')
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_not_eq(self):
        node = HTMLNode("p", 'random paragraph text', props={"href": "https://www.youtube.com","target": "_blank",})
        node2 = HTMLNode("p", 'random paragraph text', props={"href": "https://www.google.com","target": "_blank",})
        node_str = node.props_to_html()
        node2_str = node2.props_to_html()
        print(node)
        print(node_str)
        self.assertNotEqual(node_str, node2_str)


if __name__ == "__main__":
    unittest.main()