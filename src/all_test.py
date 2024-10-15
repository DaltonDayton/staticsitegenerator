import pytest

from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode


def test_to_html_props():
    node = HTMLNode(
        "div",
        "Hello, world!",
        None,
        {"class": "greeting", "href": "https://boot.dev"},
    )
    assert node.props_to_html() == 'class="greeting" href="https://boot.dev"'


def test_values():
    node = HTMLNode(
        "div",
        "I wish I could read",
    )
    assert node.tag == "div"
    assert node.value == "I wish I could read"
    assert node.children is None
    assert node.props is None


def test_repr():
    node = HTMLNode(
        "p",
        "What a strange world",
        None,
        {"class": "primary"},
    )
    assert (
        node.__repr__()
        == "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})"
    )


def test_to_html_no_children():
    node = LeafNode("p", "Hello, world!")
    assert node.to_html() == "<p>Hello, world!</p>"


def test_to_html_no_tag():
    node = LeafNode(None, "Hello, world!")
    assert node.to_html() == "Hello, world!"


def test_to_html_with_children():
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() == "<div><span>child</span></div>"


def test_to_html_with_grandchildren():
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() == "<div><span><b>grandchild</b></span></div>"


def test_to_html_many_children():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    assert (
        node.to_html()
        == "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    )


def test_headings():
    node = ParentNode(
        "h2",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    assert (
        node.to_html()
        == "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>"
    )
