import pytest

from src.htmlnode import HTMLNode


# Initialization Tests
def test_init():
    node = HTMLNode("p", "Sample paragraph", [], {})
    assert node.tag == "p"
    assert node.value == "Sample paragraph"
    assert node.children == []
    assert node.props == {}


def test_init_none():
    node = HTMLNode()
    assert node.tag is None
    assert node.value is None
    assert node.children is None
    assert node.props is None


# Property Tests
def test_to_html_props():
    node = HTMLNode(
        "div",
        "Hello, world!",
        None,
        {"class": "greeting", "href": "https://boot.dev"},
    )
    assert node.props_to_html() == 'class="greeting" href="https://boot.dev"'


def test_props_to_html():
    node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    assert node.props_to_html() == 'href="https://www.google.com" target="_blank"'


# Value Tests
def test_values():
    node = HTMLNode(
        "div",
        "I wish I could read",
    )
    assert node.tag == "div"
    assert node.value == "I wish I could read"
    assert node.children is None
    assert node.props is None


def test_empty_values():
    node = HTMLNode("", "", None, {})
    assert node.tag == ""
    assert node.value == ""
    assert node.children is None
    assert node.props == {}


def test_special_characters():
    node = HTMLNode("div", "<>&\"'", None, {"class": "special"})
    assert node.value == "<>&\"'"
    if node.props is not None:
        assert node.props.get("class") == "special"


# Children Tests
def test_children():
    child = HTMLNode("span", "child", None, {})
    parent = HTMLNode("div", "parent", [child], {})
    if parent.children is not None:
        assert parent.children[0].tag == "span"
        assert parent.children[0].value == "child"


# Error Handling Tests
def test_error_handling():
    with pytest.raises(TypeError):
        HTMLNode("div", "value", "not a list", {})  # type: ignore


def test_to_html():
    node = HTMLNode("p", "Sample paragraph", [], {})
    with pytest.raises(NotImplementedError):
        node.to_html()


# Representation Tests
def test_repr():
    node = HTMLNode(
        "a",
        "Sample link",
        props={"href": "https://www.google.com", "target": "_blank"},
    )
    assert (
        repr(node)
        == "HTMLNode(a, Sample link, children: None, {'href': 'https://www.google.com', 'target': '_blank'})"
    )
