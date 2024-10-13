import unittest

from .leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    # Initialization Tests
    def test_init(self):
        node = LeafNode("p", "Sample paragraph", {})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Sample paragraph")
        self.assertEqual(node.props, {})

    def test_init_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None, {})

    # Property Tests
    def test_to_html(self):
        node = LeafNode("p", "Sample paragraph", {})
        self.assertEqual(node.to_html(), "<p>Sample paragraph</p>")

    def test_to_html_props(self):
        node = LeafNode(
            "a", "Click me!", {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank">Click me!</a>',
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "No Tag, raw text")
        self.assertEqual(node.to_html(), "No Tag, raw text")

    # Representation Tests
    def test_repr(self):
        node = LeafNode(
            "a",
            "Sample link",
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            repr(node),
            "Tag: a, Value: Sample link, Props: {'href': 'https://www.google.com', 'target': '_blank'}",
        )


if __name__ == "__main__":
    unittest.main()
