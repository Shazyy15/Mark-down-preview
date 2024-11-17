import tkinter as tk
from tkinter import ttk
from markdown import markdown
from tkinter import scrolledtext
import re

class MarkdownPreviewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Previewer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.config(bg="#f7f9fc")
        
        # Layout configuration
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)

        # Markdown input (left side)
        tk.Label(root, text="Markdown Input", font=("Helvetica", 14, "bold"), bg="#f7f9fc", fg="#0078d4").grid(row=0, column=0, pady=(10, 0), sticky="n")
        self.markdown_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), relief="sunken", bd=2)
        self.markdown_input.grid(row=1, column=0, sticky="nsew", padx=(10, 5), pady=10)
        self.markdown_input.insert("1.0", "# Welcome to Markdown Previewer\n\nType some **Markdown** here!")

        # Plain text preview (right side)
        ttk.Label(root, text="Plain Text Preview", font=("Helvetica", 14, "bold"), background="#f7f9fc", foreground="#0078d4").grid(row=0, column=1, pady=(10, 0), sticky="n")
        self.plain_text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), state="disabled", relief="flat", bg="#f9f9f9")
        self.plain_text_output.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=10)

        # Buttons for actions
        button_frame = ttk.Frame(root)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(0, 10), sticky="ew")

        self.preview_button = ttk.Button(button_frame, text="Preview", command=self.update_preview, style="Accent.TButton")
        self.preview_button.pack(side="left", padx=5)

        self.clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_input)
        self.clear_button.pack(side="left", padx=5)

        self.exit_button = ttk.Button(button_frame, text="Exit", command=root.quit)
        self.exit_button.pack(side="left", padx=5)

        # Developer credit
        tk.Label(root, text="Developed by Shazil Shahid", font=("Helvetica", 10, "italic"), bg="#f7f9fc", fg="#6c757d").grid(row=3, column=0, columnspan=2, pady=5, sticky="s")

        # Apply styles
        self.apply_styles()

    def apply_styles(self):
        """Apply modern styles to buttons."""
        style = ttk.Style()
        style.theme_use("clam")

        # Accent Button for Preview
        style.configure("Accent.TButton", font=("Helvetica", 12, "bold"), foreground="white", background="#0078d4")
        style.map("Accent.TButton", background=[("active", "#005a9e")])

        # Default Button
        style.configure("TButton", font=("Helvetica", 12), padding=6)

    def markdown_to_plain_text(self, markdown_text):
        """Convert Markdown to plain text by removing HTML tags."""
        html_content = markdown(markdown_text)
        plain_text = re.sub(r'<[^>]*>', '', html_content)
        return plain_text

    def update_preview(self):
        """Convert Markdown to plain text and display it in the preview."""
        markdown_text = self.markdown_input.get("1.0", tk.END).strip()
        if markdown_text:
            plain_text = self.markdown_to_plain_text(markdown_text)
            self.plain_text_output.config(state="normal")
            self.plain_text_output.delete("1.0", tk.END)
            self.plain_text_output.insert("1.0", plain_text)
            self.plain_text_output.config(state="disabled")
        else:
            self.plain_text_output.config(state="normal")
            self.plain_text_output.delete("1.0", tk.END)
            self.plain_text_output.insert("1.0", "No content to preview.")
            self.plain_text_output.config(state="disabled")

    def clear_input(self):
        """Clear the Markdown input field and the preview."""
        self.markdown_input.delete("1.0", tk.END)
        self.plain_text_output.config(state="normal")
        self.plain_text_output.delete("1.0", tk.END)
        self.plain_text_output.config(state="disabled")

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownPreviewer(root)
    root.mainloop()
