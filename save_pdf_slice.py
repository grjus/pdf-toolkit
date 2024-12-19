from argparse import ArgumentParser
from PyPDF4 import PdfFileReader, PdfFileWriter


def command_parser():
    parser = ArgumentParser(description="Slice PDF file")
    parser.add_argument("--input_path", type=str, help="Pdf file input location")
    parser.add_argument("--output_path", type=str, help="Output file location")
    parser.add_argument("--page_range", type=str, help="Page range to slice")
    args = parser.parse_args()
    return [args.input_path, args.output_path, args.page_range]


if __name__ == "__main__":
    input_path, output_path, page_range = command_parser()
    pdf = PdfFileReader(input_path)
    pdf_writer = PdfFileWriter()
    start, end = map(int, page_range.split("-"))
    for page_num in range(start, end + 1):
        pdf_writer.addPage(pdf.getPage(page_num))
    with open(output_path, "wb") as out:
        pdf_writer.write(out)
