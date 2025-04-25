from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown import Markdown
import yaml
from yaml.loader import UnsafeLoader
from bs4 import BeautifulSoup

from md_to_html import reformat_table

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)


md_text = (file := open("../FAQ.md")).read()
file.close()


toml, md = md_text.split("\n---")

table_html = Markdown(extensions=("tables", "nl2br", "admonition")).convert(md)

table_dict = yaml.load(toml, UnsafeLoader)

print(table_dict)

# hardcoded skipping of the p tag, should be comparing for not a div instead
content = BeautifulSoup(table_html, "html.parser").findAll('div')
names = [item['class'][1] for item in content]

print(names)

exit()

table = reformat_table(table_html)

generated_svg = env.get_template("partial.svg").render(AITable=table)

file = open("generatedFAQ.svg", "w")
file.write(generated_svg)
file.close()

# SVG Base
"""
<?xml version="1.0" standalone="yes"?>
<svg width="{{image.width}}" height="{{image.height}}" xmlns="http://www.w3.org/2000/svg">
    <rect width="{{image.width}}" height="{{image.height}}" fill="#{{image.color}}"/>
    {% for block in image.blocks &}
    {{block|safe}}
    {% endfor %}
</svg>
"""

# Text Block
"""
# Insert splitting text.content into lines here
{% if len(text.lines) > 1 %}
<text x="{{text.x}}" y="{{text.y}}" fill="#{{text.fill}}" font-size="{{text.font_size}}">{{text.line}}</text>
{% else %}
<text x="{{text.x}}" y="{{text.y}}" fill="#{{text.fill}}" font-size="{{text.font_size}}">
    # insert for line in lines
    <tspan> x="{{text.x}}" dy="1.2em">{{text.line}}</tspan}
</text>
{% endif %}
"""

# HTML BLock
"""
<foreignObject x="{{html.x}}" y="{{html.y}}" width="{{html.w}}" height="{{html.h}}">
    <style>
        {{html.styling|safe}}
    </style>
    <body class={{html.name}} xmlns="http://w3.org/1999/xhtml">
        {{html.content|safe}}
    </body>
<foreignObject>
"""
