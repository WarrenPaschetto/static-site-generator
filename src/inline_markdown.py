import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        node_list.extend(split_nodes)
    return node_list
      
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)                   

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    markdown_text = old_nodes.text
    new_nodes = []
    markdown_images = extract_markdown_images(old_nodes.text)
    if len(markdown_images) == 0:
        new_nodes.append(TextNode(markdown_text, TextType.TEXT))
        return new_nodes
    for each in markdown_images:
        text = each[0]
        image = each[1]
        message = markdown_text.split(f"![{each[0]}]({each[1]})", 1)
        new_nodes.append(TextNode(message[0], TextType.TEXT))
        new_nodes.append(TextNode(text, TextType.IMAGE, image))
        markdown_text = markdown_text.replace(message[0] + f"![{each[0]}]({each[1]})" , "")

        
    return new_nodes

def split_nodes_link(old_nodes):
    markdown_text = old_nodes.text
    new_nodes = []
    markdown_links = extract_markdown_links(old_nodes.text)
    if len(markdown_links) == 0:
        new_nodes.append(TextNode(markdown_text, TextType.TEXT))
        return new_nodes
    for each in markdown_links:
        text = each[0]
        link = each[1]
        message = markdown_text.split(f"[{each[0]}]({each[1]})", 1)
        new_nodes.append(TextNode(message[0], TextType.TEXT))
        new_nodes.append(TextNode(text, TextType.LINK, link))
        markdown_text = markdown_text.replace(message[0] + f"[{each[0]}]({each[1]})" , "")

        
    return new_nodes

def text_to_textnodes(text):
    
    
    return 