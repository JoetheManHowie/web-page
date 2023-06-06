#!/usr/bin/env python3
import markdown
import sys

def convert_markdown_to_html(input_file, output_file):
    # Read the input Markdown file
    with open(input_file, 'r') as f:
        markdown_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)

# Provide the input and output file paths
input_file = sys.argv[1]
output_file = sys.argv[2]

# Convert Markdown to HTML
convert_markdown_to_html(input_file, output_file)
