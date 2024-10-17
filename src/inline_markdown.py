import re

from src.textnode import TextNode, TextType


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


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
