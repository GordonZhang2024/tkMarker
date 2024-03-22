#!/usr/bin/python
import converter
import click


@click.command()
@click.argument('file')
@click.argument('output_file')
def convert(file, output_file):
    '''\
    Convert Markdown to HTML
    '''
    with open(file) as f:
        markdown = f.read()

    html = converter.convert(markdown)
    with open(output_file, 'w+') as o:
        o.write(html)
        
if __name__ == '__main__':
    convert()
