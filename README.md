# Tiller
Tiller is a command line interface for transforming text files into HTML files. 
[The repo can be found here](https://github.com/Namatuzio/tiller) and [samples can be found here!](https://namatuzio.github.io/tiller/)

## Features

- Transform text files into HTML files
- Easily transform multiple files at once
- Customizable output directory

## Installation

Ensure Python is installed

`python --version`

Install the required libraries

```
pip install "typer[all]"
pip install Markdown
```

## Options:

    --version, -v  Print the current version of Tiller.
    --help, -h     Print the help message.
    --output, -o   Change the output directory of the .html files.

## Usage:

    .\main.py [OPTIONS] DIR

## Examples:

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

### Display the help message:
```
.\main.py --help (or -h)

Usage: main.py [OPTIONS] DIR 
  Convert .txt files to .html files.
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

Tiller Version: 0.1.0 
```

