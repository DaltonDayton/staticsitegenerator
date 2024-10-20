import pytest

from src.leafnode import LeafNode


# Initialization Tests
def test_init():
    node = LeafNode("p", "Sample paragraph", {})
    assert node.tag == "p"
    assert node.value == "Sample paragraph"
    assert node.props == {}


# Property Tests
def test_to_html():
    node = LeafNode("p", "Sample paragraph", {})
    assert node.to_html() == "<p>Sample paragraph</p>"


def test_to_html_no_value():
    node = LeafNode("p", None, {})
    with pytest.raises(ValueError):
        node.to_html()


def test_to_html_props():
    node = LeafNode(
        "a", "Click me!", {"href": "https://www.google.com", "target": "_blank"}
    )
    assert (
        node.to_html()
        == '<a href="https://www.google.com" target="_blank">Click me!</a>'
    )


def test_to_html_no_tag():
    node = LeafNode(None, "No Tag, raw text")
    assert node.to_html() == "No Tag, raw text"


# Representation Tests
def test_repr():
    node = LeafNode(
        "a", "Sample link", {"href": "https://www.google.com", "target": "_blank"}
    )
    assert (
        repr(node)
        == "LeafNode(a, Sample link, {'href': 'https://www.google.com', 'target': '_blank'})"
    )
