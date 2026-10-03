# BookBot

BookBot is a small Python command-line project that analyzes a text file and reports basic writing statistics. It was built as a learning project to practice reading files, counting words, and summarizing character frequency in a book or other text corpus.

## What it does

Given a path to a text file, BookBot:

- Reads the file contents
- Counts total words
- Counts how often each character appears
- Ignores non-letter characters in the final character report
- Prints a simple formatted summary to the terminal

This makes it useful for quick text analysis, especially with long works like novels, essays, or other plain-text documents.

## Example usage

```bash
python3 main.py books/frankenstein.txt
```

This will output a report similar to:

- total word count
- character frequency breakdown for alphabetic characters
- a header and summary section for the analyzed text

## Repository structure

- `main.py` — CLI entry point that reads the input file and prints the report
- `stats.py` — helper functions for word and character counting
- `books/` — sample text files used for testing and demonstration
- `README.md` — project overview and usage notes

## Sample data

The repository includes public-domain book texts such as:

- Frankenstein
- Moby-Dick
- Pride and Prejudice

These sample files let you run BookBot immediately without needing to add your own text files.

## Why this project exists

BookBot is a simple educational project designed to practice:

- Python file I/O
- string processing
- dictionaries and sorting
- command-line arguments
- writing readable command-line output

It is a good example of a lightweight data-processing script that turns raw text into useful insights.
