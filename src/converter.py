#!/usr/bin/python3

"""
Module converter
Convert Markdown to HTML
"""

import re

def convert(markdown: str, preview=False, file_path='./') -> str:
    """
    Function convert()
    Convert Markdown to HTML
    """
    global path
    path = file_path
    markdown = markdown.splitlines()
    html = convert_str(markdown, preview=preview)
    return html

def convert_str(markdown: list, preview=False, file_path='./') -> str:
    """
    Function convert_str()
    Convert Markdown to HTML
    """

    html = ''

    for line in markdown:
        line = convert_single_line(line) + '<br/>'
        html = html + line

    if preview:
        html = '''\
<html>
    <style>
    p {
        background: lightgrey;
    }
    q {
        background: lightgrey;
     }
    </style>
</html>
'''\
        + html\
        + '</html>'
    else:
        html = '''\
<html>
    <style>
    p {
        background: lightgrey;
    }
    q {
        background: lightgrey;
     }
    </style>
    <title>Preview</title>
</html>
'''\
        + html\
        + '</html>'

    quoted_code  = re.findall(r'```[\w\W]+?```', html)
    if quoted_code:
        for i in quoted_code:
            quoted_code = '<code>' + i[3:-3] + '</code>'
            html = html.replace(i, quoted_code)

    return html

def convert_single_line(line: str) -> str:
    """
    Function convert_single_line()
    Convert single-line Markdown to HTML
    """
    head = re.match(r'#+\s', line)
    if head:
        head = str(head.group(0))
        lenth = len(head) - 1
        if lenth <= 6:
            line = line.replace(head, f'<h{lenth}>')
            line = line + f'</h{lenth}><hr/>'

    bold = re.findall(r'[\*_]{2}[\w\s]+?[\*_]{2}', line)
    if bold:
        for i in bold:
            strong = '<strong>' + i[2:-2] + '</strong>'
            line = line.replace(i, strong)

    italic = re.findall(r'[\*_][\w\s</>]+?[\*_]', line)
    if italic:
        for i in italic:
            em = '<em>' + i[1:-1] + '</em>'
            line = line.replace(i, em)

    quote = re.match(r'[>\s]+\s', line)
    if quote:
        quote = str(quote.group(0))
        lenth = len(quote) - 1
        line = line.replace(quote, lenth * '<blockquote>')
        line = line + lenth * '</blockquote>'

    code = re.findall(r'`[\w\s</>]+?`', line)
    if code:
        for i in code:
            c = '<q><code>' + i[1:-1] + '</code></q>'
            line = line.replace(i, c)

    strikethrough = re.findall(r'~{2}[\w\s]+?~{2}', line)
    if strikethrough:
        for i in strikethrough:
            s = '<s>' + i[2:-2] + '</s>'
            line = line.replace(i, s)

    link = re.match(r'\[[\w\s]+?\]\([\w\s]+?\)', line)
    if link:
        link = str(link.group(0))
        text = re.match(r'\[[\w\s]+?\]', link).group(0)
        text = text.replace('(', '')
        text = text.replace(')', '')
        href = re.match(r'\([\w\s]+?\)', link).group(0)
        href = href.replace('(', '')
        href = href.replace(')', '')
        l = f'<a href={href}>{text}</a>'
        line = line.replace(link, l)

    img = re.match(r'!\[\]\([\w\W]+?\)', line)
    if img:
        img = str(img.group(0))
        src = img.replace('![]', '')\
                 .replace('(', '')\
                 .replace(')', '')
        image = f'<img src={file_path}{src}/>'
        line = line.replace(img, image)

    hr = line == '---'
    if hr:
        line = '<hr/>'

    return line
