#!/usr/bin/env python3
import os

# Directory where your blog posts are stored
post_dir = "posts/"

# Get a list of all the files in the post directory
post_files = os.listdir(post_dir)

# Create a list of links to each blog post
post_links = ""
for post_file in post_files:
    if post_file.endswith(".html"):
        post_links += f"<li><a href='posts/{post_file}'>{post_file}</a></li>"

# Generate the HTML code for the blog page
html = f"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My Blog</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <header>
      <img src="prof_prof.jpg" alt="Picture of Me">
      <h1>Joe Howie</h1>
      <script src="navigation.js"></script>
    </header>

<main>
    <h1>My Blog</h1>
    {post_links}

</main>
<footer>
  <p>&copy; 2023 Joe Howie</p>
  </footer>
</body>
</html>
"""

# Write the HTML code to a file
with open("blog.html", "w") as f:
    f.write(html)
