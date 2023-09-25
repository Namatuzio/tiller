# main.py

# running your tool at the command-line with the --version or -v flag should print the tool's name and current version.
# running your tool at the command-line with the --help or -h flag should print a standard help/usage message showing how to run the tool, which command line flags and arguments can be used, etc.
# your tool should allow the user to specify either a file or folder of files as input:
    ## If the input is a .txt file, it should process that file; if it's a directory, your tool should look for and find all .txt files within that folder, processing each one.
# your tool should generate one .html output file for each input file. For example, if I run the tool on doc.txt a new doc.html file will be generated.
# you need to deal with marking-up paragraphs: every blank line should be considered a paragraph limit and the text transformed into <p>...</p>. For example, given the following input file:
# your tool write output file(s) to a ./til folder by default. That is, if I run the tool, I should end-up with a new folder called til in the current directory, and it should contain one or more .html files. Each time the tool is run, an existing til folder should first be removed so that til always contains the latest output.

from typing import Optional

import typer
from typing_extensions import Annotated
import os
import markdown

__version__ = "0.1.0"
__help__ = """Usage: main.py [OPTIONS] DIR \n
  Convert .txt or .md files to .html files.\n
Arguments:
  DIR  [required]\n
Options:
  --version, -v  Print the current version of Tiller.
  --help, -h     Show this message and exit.
  --output, -o   Specify the name of the folder which the generated files will appear.
  --lang, -l    Specify the language of the generated HTML file.\n"""

app = typer.Typer(add_completion=False)


def version_callback(value: bool):
    if value:
        print(f"Tiller Version: {__version__}")
        raise typer.Exit()
    
def help_callback(value: bool):
    if value:
        print(f"Help: {__help__}")
        raise typer.Exit(
            code=0
        )

@app.command()
def main(dir: str, version: Optional[bool] = typer.Option(None, "--version", "-v", callback=version_callback, help="Print the current version of Tiller."), 
         help: Optional[bool] = typer.Option(None, "--help", "-h", callback=help_callback, help="Print the help message."), output: Optional[str] = typer.Option(None, "--output", "-o", help="Change the output directory of the .html files."),
         lang: Optional[str] = typer.Option(None, "--lang", "-l", help="Specify the language of the generated HTML file.")):
    """Convert .txt or .md files to .html files."""
    if(output == None):
        output = "til"
    if(lang == None):
        lang = "en-CA"
    try:
        os.makedirs(output, exist_ok=True)
    except OSError as error:
        print(error)
        exit(-1)

    if(os.path.isdir(dir)):
        for file in os.listdir(dir):
            # Added a condition to check for markdown file
            if(file.split(".")[-1] == ".txt" or file.split(".")[-1] == ".md"):
                with open(dir + "/" + file, "r") as text_file:
                    text_file = text_file.read()
                    WriteHTML(text_file, file.split(".")[0], output, lang)
            else:
                # Added an output to indicate if a file was not .md in addition to not being a .txt file
                print(f"{file} is not a .txt file or a .md file. Skipping... \n")
    elif(os.path.isfile(dir)):
        with open(dir, "r") as text_file:
            if (os.path.splitext(dir)[1] == ".txt" or os.path.splitext(dir)[1] == ".md"):
                text_file = text_file.read()
                if dir.find("\\") != -1:
                    title = dir.split("\\")[-1]
                    title = title.split(".")[-2]
                    WriteHTML(text_file, title, output, lang)
                else:
                    WriteHTML(text_file, dir.split(".")[0], output, lang)
            else:
                # Added an output to indicate if a file was not .md in addition to not being a .txt file
                print(f"{dir} is not a .txt file or .md file. Skipping... \n")



def WriteHTML(text:str, title:str, output:str = "til", lang:str = "en-CA"):
    # Check for markdown heading syntax before converting to html
    h1_content = title
    h1_start_index = text.find("#")
    h1_end_index = text.find("\n", h1_start_index + 1)
    markdown_heading1 = text[h1_start_index + 1:h1_end_index].strip()
    new_text_content = text
    if(h1_start_index >= 0):
        h1_content = markdown_heading1
        new_text_content = text[h1_end_index:]
    html = markdown.markdown(new_text_content)

    with open(f"{output}/{title}.html", "w") as html_file:
        html_content = """<!DOCTYPE html>
<html lang=\"""" + lang + """\">
    <style>
    body {
        background-color: rgb(0, 116, 145);
        text-align: center;
        color: white;
        font-family: Arial, Helvetica, sans-serif;
        font-size: xx-large;
    }
    </style>
    <head>
        <meta charset="UTF-8">
        <title>""" + title + """</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <h1>""" + h1_content + """</h1>
    <body>
        """ + html.replace("\n", "\n\t\t")  + """
    </body>
</html>"""
        if(html_content.find("<li>") != -1):
            html_content = html_content.replace("<li>", "\t<li>")
        html_file.write(html_content)
    if(h1_start_index >= 0):
        print(f"Converted {title}.md to {title}.html")
    else:
        print(f"Converted {title}.txt to {title}.html")
    
    

if __name__ == "__main__":
    app()