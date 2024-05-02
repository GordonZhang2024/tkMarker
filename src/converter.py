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

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
        script = '''\
        <script>
        function AutoRefresh(time) {
            setTimeout("location.reload(true);", time);
        }
        </script>
        '''

    html = '''\
    <html>
        <style>
            html {
                font-family: 'Sans-Serif';
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

    quoted_code = re.findall(r'```[\w\W]+?```', html)
    if quoted_code:
        for i in quoted_code:
            quoted_code = '<code>' + i[3:-3] + '</code>'
            html = html.replace(i, quoted_code)

    return html


def convert_gfm(line: str) -> str:
    # GitHub flavored alerts
    gfm_alerts = {
        '[!NOTE]': 'NOTE',
        '[!TIP]': 'TIP',
        '[!IMPORTANT]': 'IMPORTANT',
        '[!WARNING]': 'WARNING',
        '[!CAUTION]': 'CAUTION'
    }

    for origin, html in gfm_alerts.items():
        line = line.replace(origin, html)

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

    need_br_tag = False

    return line


def convert_code(line: str) -> str:
    code = re.findall(r'`[\w\s</>]+?`', line)
    if code:
        for i in code:
            c = '<q><code>' + i[1:-1] + '</code></q>'
            line = line.replace(i, c)


def convert_single_line(line: str) -> str:
    """
    Function convert_single_line()
    Convert single-line Markdown to HTML
    """
    
    global need_br_tag
    need_br_tag = True # if the line need a '<br>' tag at the end.
    

    head = re.match(r'#+\s', line)
    if head:
        head = str(head.group(0))
        lenth = len(head) - 1
        if lenth <= 6:
            line = line.replace(head, f'<h{lenth}>')
            line = line + f'</h{lenth}><hr/>'
            need_br_tag = False

    bold = re.findall(r'[\*_]{2}[\w\W]+?[\*_]{2}', line)
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
        html_link = f'<a href={href}>{text}</a>'
        line = line.replace(link, html_link)

    img = re.match(r'!\[[\w\s]+?\]\([\w\W]+?\)', line)
    if img:
        img = str(img.group(0))
        description = re.search(r'!\[[\w\s]+?\]', img)
        description = description.group(0)
        src = img.replace(description, '')\
                 .replace('(', '')\
                 .replace(')', '')
        description = description.replace('![', '')\
                                 .replace(']', '')
        image = f'<img src={src} alt={description}/>'
        line = line.replace(img, image)
        need_br_tag = False

    hr = line == '---'
    if hr:
        line = '<hr/>'
        need_br_tag = False

    line = convert_list(line)

    # GitHub flavored Markdown support
    line = convert_gfm(line)

    line = replace_script_tag(line)

    return line
