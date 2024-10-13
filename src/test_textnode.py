import unittest

from .textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)


class TestTextNode(unittest.TestCase):

    # Initialization Tests
    def test_init(self):
        node = TextNode("Sample text", text_type_text)
        self.assertEqual(node.text, "Sample text")
        self.assertEqual(node.text_type, text_type_text)
        self.assertIsNone(node.url)

        node_with_url = TextNode("Sample link", text_type_link, "http://example.com")
        self.assertEqual(node_with_url.text, "Sample link")
        self.assertEqual(node_with_url.text_type, text_type_link)
        self.assertEqual(node_with_url.url, "http://example.com")

    # Equality Tests
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq_different_text(self):
        node = TextNode("Text A", text_type_text)
        node2 = TextNode("Text B", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_different_type(self):
        node = TextNode("Same text", text_type_text)
        node2 = TextNode("Same text", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_different_url(self):
        node = TextNode("Same text", text_type_link, "http://example.com")
        node2 = TextNode("Same text", text_type_link, "http://example.org")
        self.assertNotEqual(node, node2)

    def test_eq_no_url(self):
        node = TextNode("Same text", text_type_link, "http://example.com")
        node2 = TextNode("Same text", text_type_link)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_eq_non_textnode(self):
        node = TextNode("This is a text node", text_type_bold)
        integer = 5
        with self.assertRaises(TypeError):
            self.assertEqual(node, integer)

    # Representation Tests
    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_repr_with_url(self):
        node = TextNode("Sample link", text_type_link, "http://example.com")
        self.assertEqual(repr(node), "TextNode(Sample link, link, http://example.com)")

    def test_repr_different_types(self):
        node_bold = TextNode("Bold text", text_type_bold)
        node_italic = TextNode("Italic text", text_type_italic)
        node_code = TextNode("Code text", text_type_code)
        self.assertEqual(repr(node_bold), "TextNode(Bold text, bold, None)")
        self.assertEqual(repr(node_italic), "TextNode(Italic text, italic, None)")
        self.assertEqual(repr(node_code), "TextNode(Code text, code, None)")

    def test_repr_with_url_text_type(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            repr(node), "TextNode(This is a text node, text, https://www.boot.dev)"
        )


if __name__ == "__main__":
    unittest.main()
