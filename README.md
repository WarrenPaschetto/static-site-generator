# Static Site Generator

A lightweight **static site generator** that converts structured data into HTML pages. This project processes text, markdown-style content, and generates HTML with minimal dependencies.

## Features
- **HTML Node Representation:** Create and manipulate HTML elements programmatically.
- **Markdown Parsing:** Supports inline markdown transformations (bold, italic, links, and images).
- **Lightweight and Simple:** No heavy dependencies, making it easy to extend and use.
- **Automated Testing:** Unit tests are included for key components.
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example](#example)
- [Running Tests](#running-the-tests)
- [Contributing](#contributing)
- [License](#license)
## Installation
To get started, clone the repository and navigate into the project directory:
```sh
git clone https://github.com/yourusername/static-site-generator.git
cd static-site-generator
```
Ensure you have Python 3.x installed. You can check this by running:
```sh
python3 --version
```
## Usage
### Running the Static Site Generator
You can generate a static website by running:
```sh
./main.sh
```
from your root folder in your terminal. This will execute the main script and process HTML generation.

### Running the Tests
To validate the functionality, run:
```sh
./test.sh
```
from your root folder in your terminal. 

## Project Structure

```graphql
.
├── public/                    # Output directory (HTML & CSS files)
│   ├── index.html              # Example generated HTML
│   ├── styles.css              # Example CSS file
├── src/                        # Source code
│   ├── htmlnode.py             # HTML element representation
│   ├── inline_markdown.py      # Markdown parsing logic
│   ├── main.py                 # Entry point
│   ├── textnode.py             # Text processing utilities
├── tests/                      # Unit tests
│   ├── test_htmlnode.py        # Tests for HTML processing
│   ├── test_inline_markdown.py # Tests for markdown parsing
│   ├── test_textnode.py        # Tests for text processing
├── .gitignore                  # Ignore compiled files & output
├── main.sh                     # Shell script to run the generator
├── test.sh                     # Shell script to run tests
└── README.md                   # Project documentation

```

## Example
### Input (Markdown):
```markdown
This is **bold** text, and this is *italic* text.

Check out [Boot.dev](https://www.boot.dev).

Here's an image:
![Rick Roll](https://i.imgur.com/aKaOqIh.gif)

```
### Output (HTML):
```html
<p>
    This is <b>bold</b> text, and this is <i>italic</i> text.
</p>
<p>
    Check out <a href="https://www.boot.dev">Boot.dev</a>.
</p>
<p>
    Here's an image:
    <img src="https://i.imgur.com/aKaOqIh.gif" alt="Rick Roll">
</p>

```
## Contributing
Feel free to fork this repository and submit pull requests with improvements. Contributions are welcome!

## License
This project is licensed under the MIT License. See [License](LICENSE) for details.

