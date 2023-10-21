from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

# Function to read and parse the README.md file
def get_readme_content():
    with open('README.md', 'r', encoding='utf-8') as readme_file:
        readme_content = readme_file.read()
        return markdown.markdown(readme_content)

@app.route('/')
def index():
    readme_content = get_readme_content()
    return render_template('index.html', readme_content=readme_content)

if __name__ == '__main__':
    app.run(debug=True)
