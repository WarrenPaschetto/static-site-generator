from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    test_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_node)


main()


