import os

import click
from PIL import Image


@click.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "--format",
    "-f",
    "output_format",
    required=True,
    help="The desired output format (e.g., jpg, pdf).",
    type=click.Choice(["png", "jpg", 'jpeg'], case_sensitive=False)
)
@click.option('--output-path','-o', 'output_path', type=click.STRING, required=False, help='Filename to save the converted image (give option without extension)')
def convert_image(file_path, output_format, output_path):
    """
    Convert one jpg or png image to another format.
    
    FILE_PATH: The path of the input image to convert.
    """
    # Open the image
    try:
        with Image.open(file_path) as img:
            # Determine the output file path
            if output_path is None:
                output_path = os.path.splitext(file_path)[0] + '.' + output_format
            else:
                output_path = output_path + '.' + output_format

            # Convert to RGB if output is JPG/JPEG to avoid issues with transparency
            if output_format.lower() == 'jpg' or output_format.lower() == 'jpeg':
                output_format = 'jpeg'
                img = img.convert('RGB')

            # Save the image in the desired format
            img.save(output_path, output_format.upper())
            click.echo(f"Image converted to {output_format.upper()} and saved as {output_path}")
    except Exception as e:
        click.echo(f'Something wrong has occured with this error: {e}')


@click.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option('--output-path','-o', 'output_path', type=click.STRING, required=False, help='Filename to save the converted image (if a file exists it will overwrite it)')
@click.option('--compression-level', '-c', type=click.INT, help='Compression level that the image you want to compression takes value from 1 to 3')
def compress_image(file_path, output_path, compression_level):
    # TODO: make this function more apptroachable
    try: 
        with Image.open(file_path) as img:
            if output_path is None:
                filename_with_format = os.path.splitext(file_path)
                output_path = filename_with_format[0] + f'-{compression_level}-compressed'  + '.png'
            img.save(output_path, 'PNG', compress_level=compression_level)
    except Exception as e:
        click.echo('something wrong happend: ')
        print(e)
                




@click.group()
def cli():
    pass

cli.add_command(convert_image, 'img')
cli.add_command(compress_image, 'com')
