import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog

def merge_pdfs(pdf_list, output_path):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        if os.path.exists(pdf):
            pdf_merger.append(pdf)
        else:
            print(f"File {pdf} does not exist and will be skipped.")

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select PDF files
    pdf_files = filedialog.askopenfilenames(title="Select PDF files to merge", filetypes=[("PDF files", "*.pdf")])

    if pdf_files:
        # Open file dialog to select the output file path
        output_pdf = filedialog.asksaveasfilename(title="Save merged PDF as", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if output_pdf:
            merge_pdfs(pdf_files, output_pdf)
            print(f"Merged PDF saved as {output_pdf}")
        else:
            print("No output file selected.")
    else:
        print("No PDF files selected.")