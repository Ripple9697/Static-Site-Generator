import os
from markdown_blocks import markdown_to_html_node
####
def extract_title(markdown):
    title = ""
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    if not title:
        raise ValueError("")
    return title
###

def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        md = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",html)
    directory = os.path.dirname(dest_path)
    os.makedirs(directory,exist_ok=True)
    with open(dest_path,"w") as file:
        file.write(template)
