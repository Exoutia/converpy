import os
from PIL import Image
import pypandoc
import click

def convert_image(input_path, output_format):
    """
    Convert an image to the specified format.

    Args:
        input_path (str): The path of the input image file.
        output_format (str): The desired output image format (e.g., 'jpg', 'png').

    Returns:
        str: The path to the converted image file.
    """
    try:
        with Image.open(input_path) as img:
            output_path = os.path.splitext(input_path)[0] + '.' + output_format
            img.convert('RGB').save(output_path, output_format.upper())
            click.echo(f"Image converted to {output_format} and saved as {output_path}")
            return output_path
    except Exception as e:
        click.echo(f"Error converting image: {e}", err=True)

def convert_document(input_path, output_format):
    """
    Convert a document to the specified format.

    Args:
        input_path (str): The path of the input document file.
        output_format (str): The desired output document format (e.g., 'pdf').

    Returns:
        str: The path to the converted document file.
    """
    try:
        output_path = os.path.splitext(input_path)[0] + '.' + output_format
        pypandoc.convert_file(input_path, output_format, outputfile=output_path)
        click.echo(f"Document converted to {output_format} and saved as {output_path}")
        return output_path
    except Exception as e:
        click.echo(f"Error converting document: {e}", err=True)

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.argument('output_format', type=str)
def convert(file_path, output_format):
    """
    Convert a file to a specified format.
    
    FILE_PATH: The path of the input file to convert.
    OUTPUT_FORMAT: The desired output format (e.g., 'jpg', 'pdf').
    """
    output_format = output_format.lower()

    # Determine the file type and call the appropriate conversion function
    if file_path.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff')):
        convert_image(file_path, output_format)
    elif file_path.lower().endswith(('docx', 'md', 'html', 'odt', 'txt')):
        convert_document(file_path, output_format)
    else:
        click.echo("Unsupported file format for conversion.", err=True)

if __name__ == '__main__':
    convert()
