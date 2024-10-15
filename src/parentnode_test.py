import pytest

from src.leafnode import LeafNode
from src.parentnode import ParentNode


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
