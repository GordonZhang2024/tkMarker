#!/usr/bin/env python3

"""
Module converter
Convert Markdown to HTML
"""

import re

"""
tkMarker
    A Markdown editor using tkinter
Copyright (C) 2024 Gordon Zhang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


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
        line = convert_single_line(line)
        html = html + line

    script = ''
    if preview:
        # reload automatically
        script = '''\
        <script>
        function AutoRefresh(time) {
            setTimeout("location.reload(true);", time);
        }
        </script>
        '''

    html = '''\
    <html>
        <title>
            Preview
        </title>
        <!This is the preview.>
        <style>
            html {
                font-family: 'Sans Mono';
            }
        </style>
    '''\
        + script\
        + '''\
            <body onload = "JavaScript:AutoRefresh(5000);">
        '''\
        + html\
        + '''\
            </body>
            </html>
        '''

    # Convert quoted code
    html = convert_code(html)

    return html


def convert_gfm(line: str) -> str:
    # GitHub flavored Markdown support
    gfm_alerts = {
        '[!NOTE]': 'NOTE',
        '[!TIP]': 'TIP',
        '[!IMPORTANT]': 'IMPORTANT',
        '[!WARNING]': 'WARNING',
        '[!CAUTION]': 'CAUTION'
    }

    for origin, html in gfm_alerts.items():
        line = line.replace(origin, html)

    line = line.replace('[ ]', '<input type="checkbox">')\
               .replace('[x]', '<input type="checkbox" checked>')

    return line


def replace_script_tag(line: str) -> str:
    line = line.replace('<script>', '')\
               .replace('</script>', '')

    return line


def convert_list(line: str) -> str:
    li = re.match(r'-\s[\w\W]+', line)
    if li:
        line = str(li.group(0))
        line = line.replace('-', '<ul><li>') + '</li></ul>'

    return line


def convert_code(text: str) -> str:
    # Convert code
    code = re.findall(r'`[\w\s</>]+?`', text)
    if code:
        for i in code:
            c = '<q><code>' + i[1:-1] + '</code></q>'
            text = text.replace(i, c)

    return text


def convert_single_line(line: str) -> str:
    """
    Function convert_single_line()
    Convert single-line Markdown to HTML
    """

    global need_br_tag
    need_br_tag = True  # if the line need a '<br>' tag at the end.
    have_style = True  # if there is a style.

    while have_style:  # loop(because there will possibly be nested styles)
        # find a style and convert it to html
        have_style = False
        head = re.match(r'#+\s', line)
        if head:
            head = str(head.group(0))
            lenth = len(head) - 1
            if lenth <= 6:
                line = line.replace(head, f'<h{lenth}>')
                line = line + f'</h{lenth}><hr/>'
                need_br_tag = False
                have_style = True

        bold = re.findall(r'[\*_]{2}[\w\W]+?[\*_]{2}', line)
        if bold:
            for i in bold:
                strong = '<strong>' + i[2:-2] + '</strong>'
                line = line.replace(i, strong)
                have_style = True

        italic = re.findall(r'[\*_][\w\s</>]+?[\*_]', line)
        if italic:
            for i in italic:
                em = '<em>' + i[1:-1] + '</em>'
                line = line.replace(i, em)
                have_style = True

        quote = re.match(r'[>\s]+\s', line)
        if quote:
            quote = str(quote.group(0))
            lenth = len(quote) - 1
            line = line.replace(quote, lenth * '<blockquote>')
            line = line + lenth * '</blockquote>'
            have_style = True

        strikethrough = re.findall(r'~{2}[\w\s]+?~{2}', line)
        if strikethrough:
            for i in strikethrough:
                s = '<s>' + i[2:-2] + '</s>'
                line = line.replace(i, s)
                have_style = True

        link = re.search(r'\[[\w\W\s]+?\]\([\w\s]+?\)', line)
        if link:
            link = str(link.group(0))
            text = re.match(r'\[[\w\s]+?\]', link).group(0)
            text = text.replace('(', '')
            text = text.replace(')', '')
            href = re.match(r'\([\w\s]+?\)', link).group(0)
            href = href.replace('(', '')
            href = href.replace(')', '')
            html_link = f'<a href={href}>{text}</a>'
            line = line.replace(link, html_link)
            have_style = True

        img = re.search(r'!\[[\w\W\s]+?\]\([\w\W]+?\)', line)
        if img:
            img = str(img.group(0))
            description = re.search(r'!\[[\w\s]+?\]', img)
            if description:
                description = description.group(0)
            else:
                description = ''

            src = img.replace(description, '')\
                     .replace('(', '')\
                     .replace(')', '')
            
            description = description.replace('![', '')\
                                     .replace(']', '')
            image = f'<img src={src} alt={description}/>'
            line = line.replace(img, image)
            need_br_tag = False
            have_style = True

        hr = line == '---'
        if hr:
            line = '<hr/>'
            need_br_tag = False
            have_style = True

        line = convert_list(line)

        # GitHub flavored Markdown support
        line = convert_gfm(line)

        line = replace_script_tag(line)

    if need_br_tag:
        line = line + '<br/>'

    return line
