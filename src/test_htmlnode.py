import unittest

from .htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    # Initialization Tests
    def test_init(self):
        node = HTMLNode("p", "Sample paragraph", [], {})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Sample paragraph")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_init_none(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    # Property Tests
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            'class="greeting" href="https://boot.dev"',
        )

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(), 'href="https://www.google.com" target="_blank"'
        )

    # Value Tests
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_empty_values(self):
        node = HTMLNode("", "", None, {})
        self.assertEqual(node.tag, "")
        self.assertEqual(node.value, "")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {})

    def test_special_characters(self):
        node = HTMLNode("div", "<>&\"'", None, {"class": "special"})
        self.assertEqual(node.value, "<>&\"'")
        if node.props is not None:
            self.assertEqual(node.props.get("class"), "special")

    # Children Tests
    def test_children(self):
        child = HTMLNode("span", "child", None, {})
        parent = HTMLNode("div", "parent", [child], {})
        if parent.children is not None:
            self.assertEqual(parent.children[0].tag, "span")
            self.assertEqual(parent.children[0].value, "child")

    # Error Handling Tests
    def test_error_handling(self):
        with self.assertRaises(TypeError):
            HTMLNode("div", "value", "not a list", {})  # type: ignore

    def test_to_html(self):
        node = HTMLNode("p", "Sample paragraph", [], {})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    # Representation Tests
    def test_repr(self):
        node = HTMLNode(
            "a",
            "Sample link",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            repr(node),
            "Tag: a, Value: Sample link, Children: None, Props: {'href': 'https://www.google.com', 'target': '_blank'}",
        )


if __name__ == "__main__":
    unittest.main()
