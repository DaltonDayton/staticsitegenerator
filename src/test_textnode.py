import pytest

from src.textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)


# Initialization Tests
def test_init():
    node = TextNode("Sample text", text_type_text)
    assert node.text == "Sample text"
    assert node.text_type == text_type_text
    assert node.url is None

    node_with_url = TextNode("Sample link", text_type_link, "http://example.com")
    assert node_with_url.text == "Sample link"
    assert node_with_url.text_type == text_type_link
    assert node_with_url.url == "http://example.com"


# Equality Tests
def test_eq():
    node = TextNode("This is a text node", text_type_bold)
    node2 = TextNode("This is a text node", text_type_bold)
    assert node == node2


def test_eq_different_text():
    node = TextNode("Text A", text_type_text)
    node2 = TextNode("Text B", text_type_text)
    assert node != node2


def test_eq_different_type():
    node = TextNode("Same text", text_type_text)
    node2 = TextNode("Same text", text_type_bold)
    assert node != node2


def test_eq_different_url():
    node = TextNode("Same text", text_type_link, "http://example.com")
    node2 = TextNode("Same text", text_type_link, "http://example.org")
    assert node != node2


def test_eq_no_url():
    node = TextNode("Same text", text_type_link, "http://example.com")
    node2 = TextNode("Same text", text_type_link)
    assert node != node2


def test_eq_url():
    node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
    node2 = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
    assert node == node2


def test_eq_non_textnode():
    node = TextNode("This is a text node", text_type_bold)
    integer = 5
    with pytest.raises(TypeError):
        assert node == integer


# Representation Tests
def test_repr():
    node = TextNode("This is a text node", text_type_bold)
    assert repr(node) == "TextNode(This is a text node, bold, None)"


def test_repr_with_url():
    node = TextNode("Sample link", text_type_link, "http://example.com")
    assert repr(node) == "TextNode(Sample link, link, http://example.com)"


def test_repr_different_types():
    node_bold = TextNode("Bold text", text_type_bold)
    node_italic = TextNode("Italic text", text_type_italic)
    node_code = TextNode("Code text", text_type_code)
    assert repr(node_bold) == "TextNode(Bold text, bold, None)"
    assert repr(node_italic) == "TextNode(Italic text, italic, None)"
    assert repr(node_code) == "TextNode(Code text, code, None)"


def test_repr_with_url_text_type():
    node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
    assert repr(node) == "TextNode(This is a text node, text, https://www.boot.dev)"
