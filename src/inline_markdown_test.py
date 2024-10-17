import pytest

from src.inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
)
from src.textnode import TextNode, TextType


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


def test_split_nodes_delimiter_bold_multiword():
    node = TextNode(
        "This is text with a **bolded word** and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    assert new_nodes == [
        TextNode("This is text with a ", TextType.TEXT, None),
        TextNode("bolded word", TextType.BOLD, None),
        TextNode(" and ", TextType.TEXT, None),
        TextNode("another", TextType.BOLD, None),
    ]


def test_split_nodes_delimiter_bold_and_italic():
    node = TextNode("**bold** and *italic*", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    assert new_nodes == [
        TextNode("bold", TextType.BOLD, None),
        TextNode(" and ", TextType.TEXT, None),
        TextNode("italic", TextType.ITALIC, None),
    ]


def test_split_nodes_missing_delimiter():
    node = TextNode("This is text with a `code block word", TextType.TEXT)
    with pytest.raises(Exception):
        split_nodes_delimiter([node], "`", TextType.CODE)


def test_extract_markdown_images_one():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
    assert extract_markdown_images(text) == [
        ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
    ]


def test_extract_markdown_images_two():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    assert extract_markdown_images(text) == [
        ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
        ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
    ]


def test_extract_markdown_links_one():
    text = "This is text with a link [to boot dev](https://www.boot.dev)"
    assert extract_markdown_links(text) == [("to boot dev", "https://www.boot.dev")]


def test_extract_markdown_links_two():
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    assert extract_markdown_links(text) == [
        ("to boot dev", "https://www.boot.dev"),
        ("to youtube", "https://www.youtube.com/@bootdotdev"),
    ]
