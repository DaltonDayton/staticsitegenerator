import re

from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            sections = node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception("Missing delimiter")

            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(sections[i], text_type))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        sections = re.split(r"(!\[[^\[\]]*\]\([^\(\)]*\))", node.text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                image = extract_markdown_images(sections[i])
                image_alt = image[0][0]
                image_link = image[0][1]
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        sections = re.split(r"(\[[^\[\]]*\]\([^\(\)]*\))", node.text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                image = extract_markdown_links(sections[i])
                image_alt = image[0][0]
                image_link = image[0][1]
                new_nodes.append(TextNode(image_alt, TextType.LINK, image_link))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
