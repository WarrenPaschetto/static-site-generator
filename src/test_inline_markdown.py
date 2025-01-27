import unittest
from inline_markdown import (split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes)

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_split_node_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),])
        
    def test_split_node_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT),])
        
    def test_split_node_delimiter_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT),])
        
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )
        
    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
        
    def test_extract_markdown_images_return_tuple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        img_list = extract_markdown_images(text)
        self.assertEqual(img_list, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
    def test_extract_markdown_images_return_empty(self):
        text = "This is text with a rick roll and obi wan https://i.imgur.com/fJRm4Vk.jpeg"
        img_list = extract_markdown_images(text)
        self.assertEqual(img_list, [])
        
    def test_extract_markdown_links_return_tuple(self):
        text = text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        link_list = extract_markdown_links(text)
        self.assertEqual(link_list, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
        
    def test_extract_markdown_links_return_empty(self):
        text = "This is text with a link to boot dev https://www.boot.dev and to youtube https://www.youtube.com/@bootdotdev"
        link_list = extract_markdown_links(text)
        self.assertEqual(link_list, [])
        
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image(node)
        self.assertEqual(new_nodes, [TextNode("This is text with a " , TextType.TEXT, None), TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), TextNode( " and " , TextType.TEXT, None), TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_split_nodes_same_image(self):
        node = TextNode(
            "This is text with a ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image(node)
        self.assertEqual(new_nodes, [TextNode("This is text with a " , TextType.TEXT, None), TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode( " and " , TextType.TEXT, None), TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")])
    
    def test_split_nodes_no_image(self):
        node = TextNode(
            "This is text with a (https://i.imgur.com/aKaOqIh.gif) and obi wan",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image(node)
        self.assertEqual(new_nodes, [TextNode("This is text with a (https://i.imgur.com/aKaOqIh.gif) and obi wan", TextType.TEXT, None)])
        
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link(node)
        self.assertEqual(new_nodes, [TextNode("This is text with a link " , TextType.TEXT, None), TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"), TextNode( " and " , TextType.TEXT, None), TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")])

    def test_split_nodes_same_links(self):
        node = TextNode(
            "This is text with a link [to youtube](https://www.youtube.com/@bootdotdev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link(node)
        self.assertEqual(new_nodes, [TextNode("This is text with a link " , TextType.TEXT, None), TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"), TextNode( " and " , TextType.TEXT, None), TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")])

    def test_split_nodes_no_link(self):
        node = TextNode(
            "This is text with a link to boot dev(https://www.boot.dev) and to youtube(https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link(node)
        self.assertEqual(new_nodes, [TextNode("This is text with a link to boot dev(https://www.boot.dev) and to youtube(https://www.youtube.com/@bootdotdev)", TextType.TEXT, None)])

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        print(nodes)
        
if __name__ == "__main__":
    unittest.main()