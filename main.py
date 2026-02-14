import tkinter as tk
from tkinter import messagebox
import subprocess

class RobloxLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Roblox Instance Launcher")
        self.create_widgets()

    def create_widgets(self):
        self.launch_button = tk.Button(self.root, text="Launch Roblox Instance", command=self.launch_instance)
        self.launch_button.pack(pady=20)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=20)

    def launch_instance(self):
        try:
            subprocess.Popen(["C:\\Path\\To\\RobloxPlayer.exe"])  # Change the path as needed
            messagebox.showinfo("Success", "Roblox instance launched!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Roblox: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RobloxLauncher(root)
    root.mainloop()