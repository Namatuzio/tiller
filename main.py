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
  Convert .txt files to .html files.\n
Arguments:
  DIR  [required]\n
Options:
  --version, -v  Print the current version of Tiller.
  --help, -h     Show this message and exit.
  --output, -o   Change the output directory of the .html files.\n"""

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
         help: Optional[bool] = typer.Option(None, "--help", "-h", callback=help_callback, help="Print the help message."), output: Optional[str] = typer.Option(None, "--output", "-o", help="Change the output directory of the .html files.")):
    """Convert .txt files to .html files."""
    if(output == None):
        output = "til"
    if(not os.path.exists(output)):
        os.mkdir(output)
    elif(os.path.exists(output)):
        for file in os.listdir(output):
            os.remove(output + "/" + file)
        os.rmdir(output)
        os.mkdir("./" + output)
        
    if(os.path.isdir(dir)):
        for file in os.listdir(dir):
            if(file.split(".")[1] == "txt"):
                with open(dir + "/" + file, "r") as text_file:
                    text_file = text_file.read()
                    WriteHTML(text_file, file.split(".")[0], output)
            else:
                print(f"{file} is not a .txt file. Skipping... \n")
    elif(os.path.isfile(dir)):
        with open(dir, "r") as text_file:
            if dir.split(".")[1] == "txt":
                text_file = text_file.read()
                if dir.find("\\") != -1:
                    title = dir.split("\\")[-1]
                    title = title.split(".")[-2]
                    WriteHTML(text_file, title, output)
                else:
                    WriteHTML(text_file, dir.split(".")[0], output)
            else:
                print(f"{dir} is not a .txt file. Skipping... \n")



def WriteHTML(text:str, title:str, output:str = "til"):
    html = markdown.markdown(text)

    with open(f"{output}/{title}.html", "w") as html_file:
        html_content = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>""" + title + """</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <h1>""" + title + """</h1>
    <body>
        """ + html.replace("\n", "\n\t\t") + """
    </body>
</html>"""
        html_file.write(html_content)
    print(f"Converted {title}.txt to {title}.html")

    

if __name__ == "__main__":
    app()