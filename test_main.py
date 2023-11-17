import os
from typer.testing import CliRunner
from main import CheckFileExtension
from main import WriteHTML
from main import app
import shutil

runner = CliRunner()

# Test all main arguments

## Test Version Flag
def test_main_version_arg():
    result = runner.invoke(app, ["-v"])
    assert "Tiller Version: 0.1.0" in result.output

## Test Help Flag
def test_main_help_arg():
    result = runner.invoke(app, ["-h"])
    assert "Usage: main.py [OPTIONS] DIR" in result.output

## Test Output Flag
def test_main_output_arg():
    with runner.isolated_filesystem():
        examples_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
        shutil.copytree(examples_dir, "examples")
        runner.invoke(app, ["-o", "output", "examples"])
        assert os.path.isdir("output") is True
        assert len(os.listdir("output")) > 0

## Test Lang Flag
def test_main_lang_arg():
    with runner.isolated_filesystem():
        runner.invoke(app, ["-l", "en", "examples"])
        if(os.path.isfile("til/example.html")):
            with open("til/example.html") as file:
                assert "lang=en" in file.read()

## Test Config Flag
def test_main_config_arg():
    with runner.isolated_filesystem():
        runner.invoke(app, ["-c", "examples/TOMLExample.toml", "examples"])
        if(os.path.isfile("til/example.html")):
            with open("til/example.html") as file:
                assert "lang=fr-CA" in file.read()

## Test Invalid Config File
def test_main_invalid_config_arg():
    with runner.isolated_filesystem():
        result = runner.invoke(app, ["-c", "examples/InvalidTOMLExample.toml", "examples"])
        assert result.exit_code == 1

## Test -o and -l in unison
def test_main_output_lang_arg():
    with runner.isolated_filesystem():
        examples_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
        shutil.copytree(examples_dir, "examples")
        runner.invoke(app, ["-l", "en", "-o", "output", "examples"])
        assert os.path.isdir("output") is True
        assert len(os.listdir("output")) > 0
        if(os.path.isfile("output/example.html")):
            with open("output/example.html") as file:
                assert 'lang="en"' in file.read()

# Test default arguments

## Test default output
def test_main_dir_def():
    with runner.isolated_filesystem():
        examples_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
        shutil.copytree(examples_dir, "examples")
        runner.invoke(app, ["examples"])
        assert os.path.isdir("til") is True
        assert len(os.listdir("til")) > 0

## Test dir not exist
def test_main_dir_not_exist_def():
    result = runner.invoke(app, ["notexist"])
    assert "Error: Invalid value for 'DIR': Path 'notexist' does not exist." in result.output

## Test dir is file
def test_main_dir_file_def():
    with runner.isolated_filesystem():
        examples_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
        shutil.copytree(examples_dir, "examples")
        runner.invoke(app, ["examples/example.txt"])
        assert os.path.isdir("til") is True
        assert len(os.listdir("til")) > 0

## Test file extension checks in main app
def test_main_file_extension_def():
    with runner.isolated_filesystem():
        examples_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
        shutil.copytree(examples_dir, "examples")
        result = runner.invoke(app, ["examples/example.txt"])
        assert os.path.isfile("til/example.html") is True
        assert "Converted example.txt to example.html" in result.output
        result = runner.invoke(app, ["examples/example4.html"])
        assert os.path.isfile("til/example4.html") is False
        assert "example4.html is not a .txt file or .md file. Skipping..." in result.output

# Test the CheckFileExtension function

## Test supported file extension
def test_file_extension_true_fe():
    assert CheckFileExtension("test.txt") is True
    assert CheckFileExtension("test.md") is True

## Test unsupported file extension
def test_file_extension_false_fe():
    assert CheckFileExtension("test.php") is False

## Test file extension with path
def test_file_extension_path_fe():
    assert CheckFileExtension("test/test.txt") is True
    assert CheckFileExtension("test/test.md") is True
    assert CheckFileExtension("test/test.php") is False

# Test the WriteHTML function

## Test text file conversion
def test_txt_conversion_conv():
    with runner.isolated_filesystem():
        examples_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
        shutil.copytree(examples_dir, "examples")
        with open("examples/example.txt", "r") as text_file:
            text_file = text_file.read()
            WriteHTML(text_file, "example", "examples")
            assert os.path.isfile("examples/example.html") is True
            with open("examples/example.html") as file:
                assert "<p>Hello</p>" in file.read()

## Test markdown file conversion
def test_md_conversion_conv():
    with runner.isolated_filesystem():
        examples_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
        shutil.copytree(examples_dir, "examples")
        with open("examples/example3.md", "r") as text_file:
            text_file = text_file.read()
            WriteHTML(text_file, "example3", "examples")
            assert os.path.isfile("examples/example3.html") is True
            with open("examples/example3.html") as file:
                assert "<hr />" in file.read()

## Test conversion by passing test into WriteHTML
def test_plain_text_conversion_conv():
    with runner.isolated_filesystem():
        examples_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
        shutil.copytree(examples_dir, "examples")
        WriteHTML("Hello World", "example", "examples")
        assert os.path.isfile("examples/example.html") is True
        with open("examples/example.html") as file:
            assert "<p>Hello World</p>" in file.read()

def test_plain_md_conversion_conv():
    with runner.isolated_filesystem():
        examples_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
        shutil.copytree(examples_dir, "examples")
        WriteHTML("# Hello World ", "example", "examples")
        assert os.path.isfile("examples/example.html") is True
        with open("examples/example.html") as file:
            assert "<h1>Hello World</h1>" in file.read()