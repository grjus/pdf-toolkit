from PyPDF4 import PdfFileMerger
import os
from argparse import ArgumentParser


def get_pdf_files_from_path(path: str) -> list[str]:
    files = []
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            if f.endswith(".pdf"):
                files.append(os.path.abspath(os.path.join(dirpath, f)))
    return files


def command_parser():
    parser = ArgumentParser(description="Merge PDF files")
    parser.add_argument("--dir_path", type=str, help="Pdf files directory path")
    parser.add_argument("-o", "--output", help="Output file name")
    return [parser.parse_args().dir_path, parser.parse_args().output]


if __name__ == "__main__":
    dir_path, output = command_parser()
    pdf_files: list[str] = get_pdf_files_from_path(dir_path)
    merger = PdfFileMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output)
    merger.close()
