# Tiller
Tiller is a command line interface for transforming text and markdown files into HTML files. 
[Samples can be found here!](https://namatuzio.github.io/tiller/).
The project can be found on PyPI [here](https://test.pypi.org/project/namatuzio-tiller/#description).

## Features

- Transform text files into HTML files
- Transform markdown files into HTML files (Markdown heading1 will be transformed into html \<h1\>)
- Easily transform multiple files at once
- Customizable output directory
- Language support for generated HTML file
- TOML config file support

## Installation

Please note that Tiller requires Python 3.11 or higher to run due to the use of TOMLib.

```cmd
pip install -i https://test.pypi.org/simple/ namatuzio-tiller
``` 

## Options:

    --version, -v  Print the current version of Tiller.
    --help, -h     Print the help message.
    --config, -c   Specify the path to a TOML config file to be used.
    --output, -o   Change the output directory of the .html files.
    --lang, -l    Specify the language of the generated HTML file.

## Package Usage:

    tiller [OPTIONS] DIR

## Local Usage:

    .\main.py [OPTIONS] DIR
    > note this must be ran from src/namatuzio_tiller_package

## Local Examples:

### Transform a file through a relative path:

```
.\main.py .\example.txt
Converted example.txt to example.html
```

```
.\example.txt

Hello

World\\

How are you?
```

```html
.\til\example.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hello</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <h1>Hello</h1>
    <body>
        <p>Hello</p>
		<p>World</p>
		<p>How are you?</p>
    </body>
</html>
```

### Transform all files in the current directory and output them to the `output` directory:

    .\main.py --output output .
    Converted example.txt to example.html
    Converted example2.txt to example2.html


```
.\example.txt

Hello

World

How are you?
```

```
.\example2.txt

Hi

* How
* Are
* You
* ?
```

```html
.\output\example.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>example</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <h1>example</h1>
    <body>
        <p>Hello</p>
		<p>World</p>
		<p>How are you?</p>
    </body>
</html>
```

```html
.\output\example2.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>example2</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <h1>example2</h1>
    <body>
        <p>Hi</p>
		<ul>
		<li>How</li>
		<li>Are</li>
		<li>You</li>
		<li>?</li>
		</ul>
    </body>
</html>
```
### Transform a markdown file:
```md
.\main.py .\example3.md
# Heading



Lorem ipsum dolor sit amet. Aut unde eligendi ut labore laboriosam et nihil commodi ut dolorem dolor qui tempora exercitationem qui quis error eum unde quaerat! Eum autem quam ut quae voluptates quo veritatis porro.

---

Ut nihil impedit in galisum assumenda cum incidunt nihil rem dolorem distinctio et doloremque maiores id labore ipsum quo suscipit saepe. Sed veniam debitis in natus repudiandae rem excepturi accusamus sit dolorem quia aut magni voluptatem id incidunt Quis aut voluptatibus quibusdam.

---

Eum quos harum est rerum necessitatibus aut quae architecto. Non deleniti tempore aut consectetur maiores in corrupti inventore eum veniam aliquam.

```
```html
<!DOCTYPE html>
<html lang="en-CA">
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
        <title>example3</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <h1>Heading</h1>
    <body>
        <p>Lorem ipsum dolor sit amet. Aut unde eligendi ut labore laboriosam et nihil commodi ut dolorem dolor qui tempora exercitationem qui quis error eum unde quaerat! Eum autem quam ut quae voluptates quo veritatis porro.</p>
		<hr />
		
		<p>Ut nihil impedit in galisum assumenda cum incidunt nihil rem dolorem distinctio et doloremque maiores id labore ipsum quo suscipit saepe. Sed veniam debitis in natus repudiandae rem excepturi accusamus sit dolorem quia aut magni voluptatem id incidunt Quis aut voluptatibus quibusdam.</p>
		<hr />
		
		<p>Eum quos harum est rerum necessitatibus aut quae architecto. Non deleniti tempore aut consectetur maiores in corrupti inventore eum veniam aliquam.</p>
    </body>
</html>
```

### Generate HTML file with a different language:
```
.\main.py --lang fr .\example.txt

Converted example.txt to example.html
```
```html
.\example.txt

Hello

World

How are you?
```
```html
.\til\example.html
<!DOCTYPE html>
<html lang="fr">
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
        <title>example</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <h1>example</h1>
    <body>
        <p>Hello</p>
		<p>World</p>
		<p>How are you?</p>
    </body>
</html>
```
### Transform file(s) using a TOML config file
```
.\main.py --config (or -c) .\examples\TOMLExample.toml .\examples

Converted example.txt to example.html
Converted example2.txt to example2.html
Converted example3.md to example3.html
example4.html is not a .txt file or a .md file. Skipping...

TOMLExample.toml is not a .txt file or a .md file. Skipping...
```

### Display the help message:
```
.\main.py --help (or -h)

Usage: main.py [OPTIONS] DIR 
  Convert .txt or .md files to .html files.
Arguments:
  DIR  [required]\n
Options:
  --version, -v  Print the current version of Tiller.
  --help, -h     Show this message and exit.
  --output, -o   Change the output directory of the .html files.
```

### Display the current version of Tiller:
  
```
.\main.py --version (or -v)

Tiller Version: 1.1.0 
```

