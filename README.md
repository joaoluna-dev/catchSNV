# 🧬 catchSNV 
catchSNV is a solution that finds SNVs in a FASTA file sent from the user by comparing it to a reference sequence available at GenBank. It generates a .csv report of the variant, its position, and the reference nucleotide available from GenBank.

## Highlights
- Easy to use.
- You just need Python and requests.
- Fast and convenient.
- It generates a report that can be used in other scripts, like R analysis pipelines.
- You can get the position, the reference, and the variant nucleotide.

## Overview

I'm a biomedical scientist, working in Data science, computational biology, and genomics. This tool is made for scientists who want to get SNVs from a sequenced sample in an easy and fast way, and use the data for downstream analysis.

## Authors
- João Gabriel: https://github.com/joaoluna-dev

## Usage

- Go to the file's folder, by command line or bash, and run the following:

```
python main.py
```
- So, the software will ask for some information, like your name, the gene name, the sequence, and the GenBank ID from the reference.

## Instalation

- Clone the repository to your system
- Requirements: Python 3.X and requests
```
pip install requests
```

## Feedback and Contributing
- Issues tab: https://github.com/joaoluna-dev/catchSNV/issues
- Feel comfortable suggesting any new features and corrections, every feedback is important ❤️
