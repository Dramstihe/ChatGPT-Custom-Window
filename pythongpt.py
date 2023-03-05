import tkinter as tk
import requests

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("OpenAI Chat")
        self.master.geometry("800x600")
        
        # Create a frame to hold the webview
        self.web_frame = tk.Frame(self.master)
        self.web_frame.pack(fill=tk.BOTH, expand=True)
        
        # Load the webview
        self.webview = Webview(self.web_frame, url="https://chat.openai.com/chat")
        self.webview.pack(fill=tk.BOTH, expand=True)
        
class Webview(tk.Frame):
    def __init__(self, master, url):
        tk.Frame.__init__(self, master)
        
        # Create a webview
        self.webview = tk.Text(self)
        self.webview.pack(fill=tk.BOTH, expand=True)
        
        # Load the URL
        self.webview.insert(tk.END, "Loading...")
        self.webview.update()
        response = requests.get(url)
        html = response.content
        self.webview.delete('1.0', tk.END)
        self.webview.insert(tk.END, html)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
