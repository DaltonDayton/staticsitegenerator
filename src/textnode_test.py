import pytest

from src.textnode import TextNode, TextType


# Initialization Tests
def test_init():
    node = TextNode("Sample text", TextType.TEXT)
    assert node.text == "Sample text"
    assert node.text_type == TextType.TEXT
    assert node.url is None

    node_with_url = TextNode("Sample link", TextType.LINK, "http://example.com")
    assert node_with_url.text == "Sample link"
    assert node_with_url.text_type == TextType.LINK
    assert node_with_url.url == "http://example.com"


# Equality Tests
def test_eq():
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    assert node == node2


def test_eq_different_text():
    node = TextNode("Text A", TextType.TEXT)
    node2 = TextNode("Text B", TextType.TEXT)
    assert node != node2


def test_eq_different_type():
    node = TextNode("Same text", TextType.TEXT)
    node2 = TextNode("Same text", TextType.BOLD)
    assert node != node2


def test_eq_different_url():
    node = TextNode("Same text", TextType.LINK, "http://example.com")
    node2 = TextNode("Same text", TextType.LINK, "http://example.org")
    assert node != node2


def test_eq_no_url():
    node = TextNode("Same text", TextType.LINK, "http://example.com")
    node2 = TextNode("Same text", TextType.LINK)
    assert node != node2


def test_eq_url():
    node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
    node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
    assert node == node2


def test_eq_non_textnode():
    node = TextNode("This is a text node", TextType.BOLD)
    integer = 5
    with pytest.raises(TypeError):
        assert node == integer


# Representation Tests
def test_repr():
    node = TextNode("This is a text node", TextType.BOLD)
    assert repr(node) == "TextNode(This is a text node, TextType.BOLD, None)"


def test_repr_with_url():
    node = TextNode("Sample link", TextType.LINK, "http://example.com")
    assert repr(node) == "TextNode(Sample link, TextType.LINK, http://example.com)"


def test_repr_different_types():
    node_bold = TextNode("Bold text", TextType.BOLD)
    node_italic = TextNode("Italic text", TextType.ITALIC)
    node_code = TextNode("Code text", TextType.CODE)
    assert repr(node_bold) == "TextNode(Bold text, TextType.BOLD, None)"
    assert repr(node_italic) == "TextNode(Italic text, TextType.ITALIC, None)"
    assert repr(node_code) == "TextNode(Code text, TextType.CODE, None)"


def test_repr_with_url_text_type():
    node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
    assert (
        repr(node)
        == "TextNode(This is a text node, TextType.TEXT, https://www.boot.dev)"
    )
