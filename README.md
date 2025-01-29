# BibTeX Generator
This repository contains a script for crawling BibTeX entries, given a list of titles of academic papers.  
I used [title2bib](https://github.com/bibcure/title2bib) for the search part.

# Requirements
Python:
- [title2bib](https://github.com/bibcure/title2bib)
- argparse
- tqdm

The default input and output are `input.txt` and `output.txt`. Refer to the provided example files for the required format.

# Notice
- The results are NOT guaranteed to be correct. Please double-check for important use cases.
    - TODO: Add a simple similarity check
- For papers that do not have a match, you'll need to MANUALLY update their BibTeX entries.
    - These papers will be highlighted with `=== Failed ===` in the output file.

Enjoy researching and writing papers!