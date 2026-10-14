
import tkinter as tk
import webbrowser
from urllib.parse import urlparse

def open_scanned_code(event=None):
    code = scanner_input.get().strip()
    parsed = urlparse(code)

    if parsed.scheme in ("http", "https") and parsed.netloc:
        webbrowser.open(code)
        status.config(text="Opening website...")
    else:
        status.config(text="Invalid URL. Scan a website QR code.")

    scanner_input.delete(0, tk.END)
    scanner_input.focus_set()

root = tk.Tk()
root.title("QR Code Auto Opener")
root.geometry("420x200")

tk.Label(
    root, text="Scan a QR code",
    font=("Arial", 16)
).pack(pady=15)

scanner_input = tk.Entry(root, width=45)
scanner_input.pack(pady=5)
scanner_input.focus_set()
scanner_input.bind("<Return>", open_scanned_code)

status = tk.Label(root, text="Ready to scan")
status.pack(pady=10)

root.mainloop()