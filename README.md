# 📦 Universal File Compressor

**A lightweight, GUI-based Python tool to compress various file types — including PDF, images, and text — using both lossless and lossy techniques.**

---

![Screenshot](https://github.com/yourusername/universal-file-compressor/assets/screenshot.png)

## 🚀 Features

- ✅ Compress **PDFs** using Ghostscript (Lossless & Lossy)
- ✅ Compress **JPG / PNG images** (Lossless & Quality-adjusted)
- ✅ Compress **TXT files** using `zlib` (Lossless)
- 🎨 Simple **Tkinter GUI**
- 🔧 Adjustable **PDF quality levels**: `Extreme`, `Recommended`, `Less`
- 📂 Multi-file selection & batch compression
- 🪄 Easy to use — no coding knowledge required!

---

## 📁 Supported File Types

| File Type | Mode       | Technique        |
|-----------|------------|------------------|
| `.pdf`    | Lossless   | Linearized with PikePDF |
| `.pdf`    | Lossy      | Ghostscript PDFSETTINGS |
| `.jpg`, `.png` | Lossless   | PIL Optimize         |
| `.jpg`, `.png` | Lossy      | PIL with Quality      |
| `.txt`    | Lossless   | zlib Compression  |

---

## 🖼 GUI Preview

> ![UI Preview](https://github.com/yourusername/universal-file-compressor/assets/ui_preview.png)

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/universal-file-compressor.git
cd universal-file-compressor
````

### 2. Install Python Libraries

Make sure Python 3.8+ is installed.

```bash
pip install pillow pikepdf
```

### 3. Install Ghostscript

* Download from: [https://www.ghostscript.com/download/gsdnld.html](https://www.ghostscript.com/download/gsdnld.html)
* Locate the path of `gswin64c.exe` and update it in the script:

```python
gs_path = r"C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe"
```

### 4. Run the App

```bash
python universal_file_compressor.py
```

---

## 🧪 Example Output

| Original File | Size   | Compressed Size | Mode     |
| ------------- | ------ | --------------- | -------- |
| report.pdf    | 2.1 MB | 880 KB          | Lossy    |
| image.png     | 800 KB | 520 KB          | Lossless |
| notes.txt     | 130 KB | 14 KB           | Lossless |

---

## 💡 Future Enhancements

* 🧠 AI-based compression suggestion
* 🗜 Support for `.docx`, `.pptx`, `.zip`, `.mp4`
* ☁️ Cloud upload (Google Drive)

---

## 🙋‍♂️ Author

**Prathamesh Sitaram Warak**
💻 Cyber & Tech Enthusiast | BE-IT Student
📧 [prathameshwarak@protonmail.com](mailto:prathameshwarak@protonmail.com)

---

> ⭐ If you found this useful, please give it a star and share with others!

