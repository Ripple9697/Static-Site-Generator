import os
from markdown_blocks import markdown_to_html_node
from pathlib import Path
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

def generate_pages_recursive(dir_path_content,template_path,dest_dir_path):
    for x in os.listdir(dir_path_content):
        source = os.path.join(dir_path_content,x)
        destination = os.path.join(dest_dir_path,x)
        if os.path.isfile(source):
            if source.endswith(".md"):

                destination = Path(destination).with_suffix(".html")
                generate_page(source,template_path,destination)
        else:
            generate_pages_recursive(source,template_path,destination)
