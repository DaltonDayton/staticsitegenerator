from enum import Enum

from src.leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    text: str
    text_type: TextType
    url: str | None

    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            raise TypeError("Can only compare TextNode instances")
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("Link text node must have a URL")
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("Image text node must have a URL")
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid text type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            split_node = node.text.split(delimiter)
            if len(split_node) is not 3:
                raise Exception("Missing delimiter")
            new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            match text_type:
                case TextType.BOLD:
                    new_nodes.append(TextNode(split_node[1], TextType.BOLD))
                case TextType.CODE:
                    new_nodes.append(TextNode(split_node[1], TextType.CODE))
                case TextType.ITALIC:
                    new_nodes.append(TextNode(split_node[1], TextType.ITALIC))
                case TextType.ITALIC:
                    new_nodes.append(TextNode(split_node[1], TextType.ITALIC))
            new_nodes.append(TextNode(split_node[2], TextType.TEXT))
    return new_nodes
