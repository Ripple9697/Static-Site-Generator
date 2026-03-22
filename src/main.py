import os
import shutil
import sys
from copystatic import copy_files_recursive
from gencontent import generate_page,generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
dir_docs = "./docs"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[-1]
    else:
        basepath = "/"

    print("Deleting public directory...")
    if os.path.exists(dir_docs):
        shutil.rmtree(dir_docs)
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_docs)
    
    generate_pages_recursive(
    dir_path_content,
    template_path,
    dir_docs,
    basepath,
    )

main()

