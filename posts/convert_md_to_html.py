#!/usr/bin/env python3

import sys
import os
import pandas as pd
import re
from markdown_it import MarkdownIt
from io import StringIO

def convert_markdown_to_html(input_file, output_file):
    # Read the input Markdown file
    with open(input_file, 'r') as f:
        markdown_content = f.read()

    # Configure Markdown-it with code block rendering
    md = MarkdownIt()
    md.renderer.rules["code_block"] = lambda tokens, idx, options, env, self: \
        f'<pre><code class="language-{tokens[idx].info.strip()}">{md.utils.escape_html(tokens[idx].content)}</code></pre>'

    # Convert Markdown to HTML
    html_content = md.render(markdown_content)

    # Convert the table to HTML
    html_content = convert_table_to_html(html_content)

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)

def convert_table_to_html(html_content):
    # Find the table markdown syntax using regular expressions
    table_pattern = r'\|.*\|\n\|(?:[-:]+\|)+\n(?:.*\|\n)+?\|.*\|'
    table_markdown = re.search(table_pattern, html_content, re.MULTILINE | re.DOTALL)

    if table_markdown:
        table_markdown = table_markdown.group()

        # Parse the table using pandas
        table_rows = table_markdown.strip().split('\n')
        headers = [header.strip() for header in table_rows[0].split('|')[1:-1]]
        data_rows = [row.strip().split('|')[1:-1] for row in table_rows[2:]]
        df = pd.DataFrame(data_rows, columns=headers)

        # Convert the table to HTML
        html_table = df.to_html(index=False)

        # Replace the table markdown with the HTML table
        html_content = html_content.replace(table_markdown, html_table)

    return html_content


# Provide the input and output file paths
input_file = sys.argv[1]
temp_file = "temp.html"
output_file = input_file.split(".")[0]+".html"
# Convert Markdown to HTML with code block and table rendering
convert_markdown_to_html(input_file, temp_file)


# Read the contents of input.html
with open(temp_file, 'r') as file:
    input_html = file.read()

# Read the contents of template.html
with open('template.html', 'r') as file:
    template_html = file.read()

# Insert the input.html content into the template
output_html = template_html.replace('{CONTENT}', input_html)

# Write the final HTML to a new file
with open(output_file, 'w') as file:
    file.write(output_html)

os.system("rm temp.html")
