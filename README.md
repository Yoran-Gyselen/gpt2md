# gpt2md

A simple tool to convert your ChatGPT conversation to Markdown files.

gpt2md allows you to convert your conversations on ChatGPT to local Markdown files. This is done by extracting the conversation data from the `conversations.json` file when you download your profile data from OpenAI's website. gpt2md converts the data from this file into readable files you can easily store locally. This gives you the ability to store your data in a manner like it's presented to you on the ChatGPT website.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gpt2md.

```bash
pip install gpt2md
```

## Usage

You can use gpt2md as a library in Python or as a command-line tool.

In order for gpt2md to convert your data into Markdown files, you need to provide a file with your conversation history with ChatGPT. This file (among some others) can be downloaded from the ChatGPT website

1. Log in to the ChatGPT website.
2. Click on your profile avatar.
3. Click on `Settings` > `Data controls`.
4. Under the `Export data` section, click on `Export`.
5. In the info box, click `Confirm export`.
6. You should receive an e-mail containing a link to your archive (in ZIP-format).
7. Once extracted, look for the `conversations.json` file. This is the input file you need to provide to gpt2md.


### Usage in Python

```python
from gpt2md import Gpt2md

parser = Gpt2md(input_file="conversations.json", output="conversations", verbose=True)
parser.parse()
```

### Usage via the CLI

```bash
gpt2md -v conversations.json -o conversations
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

gpt2md is licensed under the [MIT license](https://choosealicense.com/licenses/mit/).