import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        test_node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(test_node.props_to_html(),' href="https://www.google.com" target="_blank"')
        
    def test_error(self):
        err = HTMLNode()
        err.to_html
        self.assertRaises(NotImplementedError)
        
    def test__tag_none(self):
        FirstNode = HTMLNode()
        SecondNode = HTMLNode()
        test_node = HTMLNode(value="Text inside paragraph", children=[FirstNode, SecondNode], props={"href": "https://www.google.com", "target": "_blank",})
        self.assertIsNone(test_node.tag)
    
    def test__value_none(self):
        FirstNode = HTMLNode()
        SecondNode = HTMLNode()
        test_node = HTMLNode(tag="p", children=[FirstNode, SecondNode], props={"href": "https://www.google.com", "target": "_blank",})
        self.assertIsNone(test_node.value)
        
    def test_repr(self):
        test_node = HTMLNode(tag="p", value="Text inside paragraph", children=[], props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(test_node.__repr__(), "HTMLNode(p, Text inside paragraph, children: [], {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_to_html_leafnode(self):
        test_node = LeafNode("a", "Click here to visit Google", {"href": "https://www.google.com"})
        self.assertEqual(test_node.to_html(),'<a href="https://www.google.com">Click here to visit Google</a>')
        
    def test_missing_value_leafnode(self):
        err = LeafNode("a", {"href": "https://www.google.com"})
        err.to_html
        self.assertRaises(ValueError)
        
    def test__tag_none_to_html(self):
        test_node = LeafNode(None, "Click here to visit Google", {"href": "https://www.google.com"})
        self.assertEqual(test_node.to_html(), "Click here to visit Google")
    
    def test__tag_none_leafnode(self):
        test_node = LeafNode(None, "Click here to visit Google", {"href": "https://www.google.com"})
        self.assertEqual(test_node.tag, None)
        
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        
    def test_repr_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
            )
        self.assertEqual(node.__repr__(), "ParentNode(p, children: [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None)], None)")
        
    def test_parent_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        node.to_html
        self.assertRaises(ValueError)
        
    def test_parent_no_children(self):
        node = ParentNode("p", None, {"href": "https://www.google.com"})
        node.to_html
        self.assertRaises(ValueError)
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
if __name__ == "__main__":
    unittest.main()

