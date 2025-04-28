import os
import shutil
import glob
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import datetime

# Define language dictionaries
LANG_DATA = {
    "en": {
        "title": "File Organizer Tool",
        "version": "Version 0.1.1",
        "date": "Date: {date}",
        "configuration": "Configuration",
        "source_folder": "Source Folder:",
        "output_folder": "Output Folder:",
        "file_extensions": "File Extensions:",
        "help_text": "Separate extensions with colons (e.g. .txt:.pdf:.docx)",
        "execute_process": "Execute Process",
        "process_log": "Process Log",
        "ready": "Ready",
        "processing_files": "Processing files...",
        "process_started": "=== Process Started ===",
        "process_summary": "=== Process Summary ===",
        "files_processed": "Files processed: {count}",
        "time": "Time: {time} seconds",
        "completed": "Completed: {time}",
        "no_match": "No matching files found.",
        "process_finished": "Process finished.\n{count} files processed in {time} seconds.",
        "error": "Error",
        "source_folder_error": "Please specify a source folder.",
        "source_folder_non_exist": "The source folder does not exist.",
        "output_folder_error": "Please specify an output folder.",
        "output_folder_create_error": "Could not create output folder: {error}",
        "output_folder_created": "Created output folder: {folder}",
        "choose_language": "Choose Language"
    },
    "ja": {
        "title": "ファイル整理ツール",
        "version": "Version 0.1.1",
        "date": "日付: {date}",
        "configuration": "設定",
        "source_folder": "ソースフォルダ:",
        "output_folder": "出力フォルダ:",
        "file_extensions": "ファイル拡張子:",
        "help_text": "拡張子はコロン区切りで入力してください（例: .txt:.pdf:.docx）",
        "execute_process": "実行",
        "process_log": "処理ログ",
        "ready": "準備完了",
        "processing_files": "ファイル処理中...",
        "process_started": "=== 処理開始 ===",
        "process_summary": "=== 処理概要 ===",
        "files_processed": "処理ファイル数: {count}",
        "time": "時間: {time} 秒",
        "completed": "完了: {time}",
        "no_match": "一致するファイルが見つかりませんでした。",
        "process_finished": "処理が完了しました。\n{count} ファイルを {time} 秒で処理しました。",
        "error": "エラー",
        "source_folder_error": "ソースフォルダを指定してください。",
        "source_folder_non_exist": "ソースフォルダが存在しません。",
        "output_folder_error": "出力フォルダを指定してください。",
        "output_folder_create_error": "出力フォルダを作成できませんでした: {error}",
        "output_folder_created": "出力フォルダを作成しました: {folder}",
        "choose_language": "言語を選択"
    }
}

def process_directories(source_dir, output_dir, extensions):
    """Process files in subfolders and rename them to folder name."""
    processed_files = 0
    ext_list = [ext.strip() for ext in extensions.split(':') if ext.strip()]

    if not ext_list:
        ext_list = ['.txt']

    ext_list = [ext if ext.startswith('.') else f'.{ext}' for ext in ext_list]

    try:
        for root, dirs, files in os.walk(source_dir):
            folder_name = os.path.basename(root)
            for file in files:
                file_ext = os.path.splitext(file.lower())[1]
                if file_ext in ext_list:
                    original_file_path = os.path.join(root, file)
                    new_filename = f"{folder_name}{file_ext}"
                    new_file_path = os.path.join(output_dir, new_filename)

                    if os.path.exists(new_file_path):
                        base, ext = os.path.splitext(new_file_path)
                        counter = 1
                        while os.path.exists(f"{base}_{counter}{ext}"):
                            counter += 1
                        new_file_path = f"{base}_{counter}{ext}"

                    try:
                        shutil.copy2(original_file_path, new_file_path)
                        processed_files += 1
                        print(f"Copied: {original_file_path} → {new_file_path}")
                    except Exception as e:
                        print(f"Error copying {original_file_path}: {e}")
    except Exception as e:
        print(f"Error processing directories: {e}")

    return processed_files

class Application(tk.Frame):
    def __init__(self, master=None, lang="en"):
        super().__init__(master)
        self.master = master
        self.lang = LANG_DATA.get(lang, LANG_DATA["en"])
        self.master.title(self.lang["title"])
        self.master.geometry("800x600")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Arial', 11), padding=8)
        self.style.configure('TLabel', font=('Arial', 11))
        self.style.configure('TFrame', background='#f5f5f5')
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('Info.TLabel', font=('Arial', 10), foreground='#555555')
        self.style.configure('TLabelframe', font=('Arial', 11))
        self.style.configure('TLabelframe.Label', font=('Arial', 11, 'bold'))
        self.style.configure('StatusBar.TLabel', font=('Arial', 10), background='#e0e0e0', relief='sunken')
        self.master.configure(bg='#f5f5f5')
        self.configure(bg='#f5f5f5')
        self.style.map('TButton',
                      background=[('active', '#4a7eff'), ('pressed', '#3a6eef')],
                      foreground=[('active', 'white'), ('pressed', 'white')])
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="25 25 25 25")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 25))
        title_label = ttk.Label(title_frame, text=self.lang["title"], style='Header.TLabel')
        title_label.pack(side=tk.LEFT)
        
        version_label = ttk.Label(title_frame, text=self.lang["version"], style='Info.TLabel')
        version_label.pack(side=tk.RIGHT, padx=5)
        
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        date_label = ttk.Label(title_frame, text=self.lang["date"].format(date=current_date), style='Info.TLabel')
        date_label.pack(side=tk.RIGHT, padx=5)

        # Input section
        input_section = ttk.LabelFrame(main_frame, text=self.lang["configuration"], padding=15)
        input_section.pack(fill=tk.X, pady=(0, 15))

        # Source folder
        input_frame = ttk.Frame(input_section)
        input_frame.pack(fill=tk.X, pady=8)
        input_label = ttk.Label(input_frame, text=self.lang["source_folder"], width=15, anchor=tk.W)
        input_label.pack(side=tk.LEFT, padx=5)
        self.input_path = tk.StringVar()
        input_entry = ttk.Entry(input_frame, textvariable=self.input_path, width=55, font=('Arial', 11))
        input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        input_button = ttk.Button(input_frame, text="Browse", command=self.select_input_dir)
        input_button.pack(side=tk.RIGHT, padx=5)

        # Output folder
        output_frame = ttk.Frame(input_section)
        output_frame.pack(fill=tk.X, pady=8)
        output_label = ttk.Label(output_frame, text=self.lang["output_folder"], width=15, anchor=tk.W)
        output_label.pack(side=tk.LEFT, padx=5)
        self.output_path = tk.StringVar()
        output_entry = ttk.Entry(output_frame, textvariable=self.output_path, width=55, font=('Arial', 11))
        output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        output_button = ttk.Button(output_frame, text="Browse", command=self.select_output_dir)
        output_button.pack(side=tk.RIGHT, padx=5)

        # File extensions
        ext_frame = ttk.Frame(input_section)
        ext_frame.pack(fill=tk.X, pady=8)
        ext_label = ttk.Label(ext_frame, text=self.lang["file_extensions"], width=15, anchor=tk.W)
        ext_label.pack(side=tk.LEFT, padx=5)
        self.extensions = tk.StringVar(value=".txt")
        ext_entry = ttk.Entry(ext_frame, textvariable=self.extensions, width=55, font=('Arial', 11))
        ext_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Help text
        help_frame = ttk.Frame(input_section)
        help_frame.pack(fill=tk.X, pady=(0, 8))
        help_icon = ttk.Label(help_frame, text="ℹ", font=('Arial', 11, 'bold'), foreground="#0066cc")
        help_icon.pack(side=tk.LEFT, padx=(98, 5))
        help_text = ttk.Label(help_frame, text=self.lang["help_text"], style='Info.TLabel')
        help_text.pack(side=tk.LEFT)

        # Execute button
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=tk.X, pady=15)
        self.run_button = ttk.Button(action_frame, text=self.lang["execute_process"], command=self.run_process, width=20)
        self.run_button.pack(pady=5)

        # Progress indicators
        self.progress_frame = ttk.Frame(main_frame)
        self.progress_frame.pack(fill=tk.X, pady=5)
        self.progress_label = ttk.Label(self.progress_frame, text="Progress:", anchor=tk.W)
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient=tk.HORIZONTAL,
                                            mode='indeterminate', length=400)

        # Log display
        log_frame = ttk.LabelFrame(main_frame, text=self.lang["process_log"], padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        self.scrollbar = ttk.Scrollbar(log_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text = tk.Text(log_frame, height=15, yscrollcommand=self.scrollbar.set,
                              font=('Consolas', 10), bg='#ffffff', fg='#000000',
                              relief='solid', bd=1, padx=5, pady=5)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.log_text.yview)

        # Status bar
        status_frame = ttk.Frame(main_frame, relief='sunken', padding=2)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        self.status_var = tk.StringVar()
        self.status_var.set(self.lang["ready"])
        status_bar = ttk.Label(status_frame, textvariable=self.status_var,
                             anchor=tk.W, style='StatusBar.TLabel')
        status_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.time_var = tk.StringVar()
        self.update_clock()
        time_display = ttk.Label(status_frame, textvariable=self.time_var,
                               style='StatusBar.TLabel', width=10)
        time_display.pack(side=tk.RIGHT)

    def update_clock(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_var.set(now)
        self.master.after(1000, self.update_clock)

    def select_input_dir(self):
        directory = filedialog.askdirectory(title=self.lang["source_folder"])
        if directory:
            self.input_path.set(directory)

    def select_output_dir(self):
        directory = filedialog.askdirectory(title=self.lang["output_folder"])
        if directory:
            self.output_path.set(directory)

    def log(self, message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{now}] {message}\n")
        self.log_text.see(tk.END)
        self.log_text.update()

    def run_process(self):
        source_dir = self.input_path.get()
        output_dir = self.output_path.get()
        extensions = self.extensions.get()

        if not source_dir:
            messagebox.showerror(self.lang["error"], self.lang["source_folder_error"])
            return

        if not os.path.isdir(source_dir):
            messagebox.showerror(self.lang["error"], self.lang["source_folder_non_exist"])
            return

        if not output_dir:
            messagebox.showerror(self.lang["error"], self.lang["output_folder_error"])
            return

        if not os.path.isdir(output_dir):
            try:
                os.makedirs(output_dir)
                self.log(self.lang["output_folder_created"].format(folder=output_dir))
            except Exception as e:
                messagebox.showerror(self.lang["error"], self.lang["output_folder_create_error"].format(error=e))
                return

        self.log_text.delete(1.0, tk.END)
        self.progress_label.pack(side=tk.LEFT, padx=5)
        self.progress_bar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.progress_bar.start(10)
        self.status_var.set(self.lang["processing_files"])
        self.run_button.configure(state="disabled")
        self.log(self.lang["process_started"])
        self.log(f"{self.lang['source_folder']} {source_dir}")
        self.log(f"{self.lang['output_folder']} {output_dir}")
        self.log(f"{self.lang['file_extensions']} {extensions}")

        try:
            self.master.after(100, lambda: self.process_files(source_dir, output_dir, extensions))
        except Exception as e:
            self.log(f"{self.lang['error']}: {e}")
            self.progress_bar.stop()
            self.progress_label.pack_forget()
            self.progress_bar.pack_forget()
            self.run_button.configure(state="normal")
            self.status_var.set(self.lang["error"])
            messagebox.showerror(self.lang["error"], f"{self.lang['error']}: {e}")

    def process_files(self, source_dir, output_dir, extensions):
        try:
            import sys
            original_stdout = sys.stdout
            class StdoutRedirector:
                def __init__(self, text_widget):
                    self.text_widget = text_widget
                def write(self, string):
                    self.text_widget.insert(tk.END, string)
                    self.text_widget.see(tk.END)
                    self.text_widget.update()
                def flush(self):
                    pass
            sys.stdout = StdoutRedirector(self.log_text)
            start_time = datetime.datetime.now()
            processed = process_directories(source_dir, output_dir, extensions)
            end_time = datetime.datetime.now()
            duration = (end_time - start_time).total_seconds()
            self.log("\n" + self.lang["process_summary"])
            self.log(self.lang["files_processed"].format(count=processed))
            self.log(self.lang["time"].format(time=f"{duration:.2f}"))
            self.log(self.lang["completed"].format(time=end_time.strftime('%Y-%m-%d %H:%M:%S')))
            sys.stdout = original_stdout
            self.progress_bar.stop()
            self.progress_label.pack_forget()
            self.progress_bar.pack_forget()
            self.run_button.configure(state="normal")
            self.status_var.set(self.lang["completed"].format(time=f"{duration:.2f}"))
            if processed == 0:
                messagebox.showinfo(self.lang["error"], self.lang["no_match"])
            else:
                messagebox.showinfo(self.lang["execute_process"], self.lang["process_finished"].format(count=processed, time=f"{duration:.2f}"))
        except Exception as e:
            self.log(f"{self.lang['error']}: {e}")
            self.progress_bar.stop()
            self.progress_label.pack_forget()
            self.progress_bar.pack_forget()
            self.run_button.configure(state="normal")
            self.status_var.set(self.lang["error"])
            messagebox.showerror(self.lang["error"], f"{self.lang['error']}: {e}")

def select_language():
    sel_lang = {"value": None}
    root = tk.Tk()
    root.title("Language Selection")
    root.geometry("300x150")
    lang_label = ttk.Label(root, text=LANG_DATA["en"]["choose_language"], font=('Arial', 12))
    lang_label.pack(pady=20)
    frame = ttk.Frame(root)
    frame.pack(pady=10)
    def set_lang(lang_code):
        sel_lang["value"] = lang_code
        root.destroy()
    btn_en = ttk.Button(frame, text="English", command=lambda: set_lang("en"), width=10)
    btn_en.grid(row=0, column=0, padx=10)
    btn_ja = ttk.Button(frame, text="日本語", command=lambda: set_lang("ja"), width=10)
    btn_ja.grid(row=0, column=1, padx=10)
    root.mainloop()
    return sel_lang["value"]

if __name__ == "__main__":
    language = select_language() or "en"
    root = tk.Tk()
    root.configure(bg='#f5f5f5')
    app = Application(master=root, lang=language)
    app.mainloop()
