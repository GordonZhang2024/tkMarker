#!/usr/bin/python
import re

def convert(markdown: str):
    '''
    function convert(): convert Markdown to HTML
    '''
    markdown = markdown.splitlines()
    html = ''    
    for index, line in enumerate(markdown):
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
            image = f'<img src={src}/>'
            line = line.replace(img, image)
       
        hr = line == '---'
        if hr:
            line = '<hr/>'

        line = line + '<br/>'
        html = html + line
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
    <title>
        Preview
    </title>
</html>
'''\
    + html\
    + '</html>'
    html = html.replace('<script>', '')\
               .replace('</script>', '')
    
    quoted_code  = re.findall(r'```[\w\W]+?```', html)
    if quoted_code:
        for i in quoted_code:
            quoted_code = '<code>' + i[3:-3] + '</code>'
            html = html.replace(i, quoted_code)

    return html
