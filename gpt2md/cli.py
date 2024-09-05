from argparse import ArgumentParser, BooleanOptionalAction
from .main import Gpt2md
from pathlib import Path

def cli():
    parser = ArgumentParser(prog="gpt2md", description="A simple tool to convert your ChatGPT conversation to Markdown files.")
    parser.add_argument("input_file", metavar="INPUT_FILE", type=str, help="The input file in JSON-format.")
    parser.add_argument('-v', '--verbose', help="Show verbose output.", action=BooleanOptionalAction, default=False)
    parser.add_argument('-o', '--output_folder', metavar="OUTPUT_FOLDER", type=str, help="Specify the output folder.", default=".")
    
    args = parser.parse_args()

    assert args.input_file[-5:] == ".json", "INPUT_FILE should be in the JSON-format."

    Path(args.output_folder).mkdir(parents=True, exist_ok=True)

    converter = Gpt2md(input_file=args.input_file, output_folder=args.output_folder, verbose=args.verbose)
    converter.parse()

if __name__ == "__main__":
    cli()