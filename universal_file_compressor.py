# universal_file_compressor.py

import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PIL import Image
import pikepdf
import zlib
import subprocess

# ========== Ghostscript path (manual fix) ==========
gs_path = r"C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe"

# ========== Compression Functions ==========

def compress_pdf_lossless(input_path, output_path):
    try:
        pdf = pikepdf.open(input_path)
        pdf.save(output_path, linearize=True)
        pdf.close()
        print(f"[PDF:Lossless] {input_path} → {output_path}")
    except Exception as e:
        messagebox.showerror("PDF Compression Error", f"{input_path}\n{str(e)}")

def compress_pdf_lossy(input_path, output_path):
    try:
        subprocess.call([
            gs_path,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS={pdf_quality.get()}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_path}",
            input_path
        ])
        print(f"[PDF:Lossy] {input_path} → {output_path}")
    except Exception as e:
        messagebox.showerror("PDF Lossy Compression Error", f"{input_path}\n{str(e)}")

def compress_image_lossless(input_path, output_path):
    try:
        img = Image.open(input_path)
        img.save(output_path, optimize=True)
        print(f"[Image:Lossless] {input_path} → {output_path}")
    except Exception as e:
        messagebox.showerror("Image Compression Error", f"{input_path}\n{str(e)}")

def compress_image_lossy(input_path, output_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGB")
        img.save(output_path, optimize=True, quality=40)
        print(f"[Image:Lossy] {input_path} → {output_path}")
    except Exception as e:
        messagebox.showerror("Image Compression Error", f"{input_path}\n{str(e)}")

def compress_text_lossless(input_path, output_path):
    try:
        with open(input_path, 'rb') as f:
            content = f.read()
        compressed = zlib.compress(content)
        with open(output_path, 'wb') as f:
            f.write(compressed)
        print(f"[Text:Lossless] {input_path} → {output_path}")
    except Exception as e:
        messagebox.showerror("Text Compression Error", f"{input_path}\n{str(e)}")

# ========== GUI Functions ==========

selected_files = []

def browse_files():
    global selected_files
    files = filedialog.askopenfilenames(title="Select files to compress")
    selected_files = list(files)
    file_listbox.delete(0, tk.END)
    for file in selected_files:
        file_listbox.insert(tk.END, file)

def compress_selected_files():
    if not selected_files:
        messagebox.showwarning("No Files", "Please select files to compress.")
        return

    save_dir = filedialog.askdirectory(title="Select Folder to Save Compressed Files")
    if not save_dir:
        return

    mode = compression_mode.get()
    print(f"Compression mode selected: {mode}")

    for file_path in selected_files:
        ext = os.path.splitext(file_path)[1].lower()
        base_name = os.path.basename(file_path)
        name_only, _ = os.path.splitext(base_name)

        if ext == '.txt':
            output_path = os.path.join(save_dir, f"{name_only}_compressed.txt.zlib")
        else:
            output_path = os.path.join(save_dir, f"{name_only}_compressed{ext}")

        if ext == '.pdf':
            if mode == "lossless":
                compress_pdf_lossless(file_path, output_path)
            else:
                compress_pdf_lossy(file_path, output_path)

        elif ext in ['.jpg', '.jpeg', '.png']:
            if mode == "lossless":
                compress_image_lossless(file_path, output_path)
            else:
                compress_image_lossy(file_path, output_path)

        elif ext == '.txt':
            compress_text_lossless(file_path, output_path)

        else:
            messagebox.showinfo("Skipped", f"Compression for '{ext}' not supported yet.\nFile: {base_name}")

    messagebox.showinfo("Done", f"{mode.upper()} compression completed!")

# ========== GUI Layout ==========

root = tk.Tk()
root.title("Universal File Compressor")
root.geometry("650x550")
root.resizable(False, False)
root.configure(bg="yellow")  # 🌟 Set background to yellow

compression_mode = tk.StringVar(value="lossless")
pdf_quality = tk.StringVar(value="/ebook")  # Default = Recommended

tk.Label(root, text="Universal File Compressor", font=("Arial", 16, "bold"), bg="yellow", fg="black").pack(pady=10)
tk.Label(root, text="Supported: PDF (lossless/lossy), JPG, PNG, TXT", font=("Arial", 10, "bold"), bg="yellow", fg="black").pack(pady=5)

file_listbox = tk.Listbox(root, width=70, height=10)
file_listbox.pack(pady=10)

toggle_frame = tk.Frame(root, bg="yellow")
toggle_frame.pack(pady=5)
tk.Label(toggle_frame, text="Compression Mode:", font=("Arial", 10, "bold"), bg="yellow", fg="black").pack(side="left", padx=5)
tk.Radiobutton(toggle_frame, text="Lossless", variable=compression_mode, value="lossless", bg="yellow").pack(side="left")
tk.Radiobutton(toggle_frame, text="Lossy", variable=compression_mode, value="lossy", bg="yellow").pack(side="left")

quality_frame = tk.Frame(root, bg="yellow")
quality_frame.pack(pady=5)
tk.Label(quality_frame, text="PDF Quality Level:", font=("Arial", 10, "bold"), bg="yellow", fg="black").pack(side="left", padx=5)
tk.Radiobutton(quality_frame, text="Extreme", variable=pdf_quality, value="/screen", bg="yellow").pack(side="left")
tk.Radiobutton(quality_frame, text="Recommended", variable=pdf_quality, value="/ebook", bg="yellow").pack(side="left")
tk.Radiobutton(quality_frame, text="Less", variable=pdf_quality, value="/printer", bg="yellow").pack(side="left")

tk.Button(root, text="Browse Files", command=browse_files, width=20, bg="red", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
tk.Button(root, text="Compress Files", command=compress_selected_files, width=20, bg="green", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

tk.Label(root, text="More file types coming soon...", font=("Arial", 9, "italic"), bg="yellow", fg="black").pack(side="bottom", pady=5)

root.mainloop()
