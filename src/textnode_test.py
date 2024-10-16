import pytest

from src.textnode import (
    TextNode,
    TextType,
    split_nodes_delimiter,
    text_node_to_html_node,
)


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


# text_node_to_html_node Tests
def test_text():
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    if html_node is not None:
        assert html_node.tag == None
    if html_node is not None:
        assert html_node.value == "This is a text node"


def test_image():
    node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
    html_node = text_node_to_html_node(node)
    if html_node is not None:
        assert html_node.tag == "img"
    if html_node is not None:
        assert html_node.value == None
    if html_node is not None:
        assert html_node.props == {
            "src": "https://www.boot.dev",
            "alt": "This is an image",
        }


def test_bold():
    node = TextNode("This is bold", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    if html_node is not None:
        assert html_node.tag == "b"
    if html_node is not None:
        assert html_node.value == "This is bold"


def test_split_nodes_delimiter_code():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    assert new_nodes == [
        TextNode("This is text with a ", TextType.TEXT, None),
        TextNode("code block", TextType.CODE, None),
        TextNode(" word", TextType.TEXT, None),
    ]


def test_split_nodes_delimiter_bold():
    node = TextNode("This is text with a **bolded** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.CODE)
    assert new_nodes == [
        TextNode("This is text with a ", TextType.TEXT, None),
        TextNode("bolded", TextType.CODE, None),
        TextNode(" word", TextType.TEXT, None),
    ]


def test_split_nodes_delimiter_italic_underscore():
    node = TextNode("This is text with an _italicized_ word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.CODE)
    assert new_nodes == [
        TextNode("This is text with an ", TextType.TEXT, None),
        TextNode("italicized", TextType.CODE, None),
        TextNode(" word", TextType.TEXT, None),
    ]


def test_split_nodes_delimiter_italic_asterisk():
    node = TextNode("This is text with an *italicized* word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "*", TextType.CODE)
    assert new_nodes == [
        TextNode("This is text with an ", TextType.TEXT, None),
        TextNode("italicized", TextType.CODE, None),
        TextNode(" word", TextType.TEXT, None),
    ]


def test_split_nodes_delimiter_texttype_bold():
    node = TextNode("bolded text", TextType.BOLD)
    new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
    assert new_nodes == [
        TextNode("bolded text", TextType.BOLD, None),
    ]


def test_split_nodes_missing_delimiter():
    node = TextNode("This is text with a `code block word", TextType.TEXT)
    with pytest.raises(Exception):
        split_nodes_delimiter([node], "`", TextType.CODE)
