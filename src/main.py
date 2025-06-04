from textnode import TextType, TextNode
from htmlnode import HTMLNode


def main():
    text_node = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(text_node)
    HTML_node = HTMLNode('a', 'text')
    print(HTML_node)

if __name__ == "__main__":
    main()