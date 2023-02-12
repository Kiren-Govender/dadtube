import datetime
import pathlib
from queue import Queue
from threading import Thread, Timer
from time import sleep
from tkinter.filedialog import askdirectory
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap import utility
import pyperclip as pc
import validators
from pytube import YouTube

class YoutubeDownloader(ttk.Frame):
    queue = Queue()

    def __init__(self, master):
        super().__init__(master, padding=(15, 15))
        self.pack(fill=BOTH, expand=YES)
        self.count=0
        # application variables
        _path = pathlib.Path().absolute().as_posix()
        self.url_var = ttk.StringVar(value="")
        self.path_var = ttk.StringVar(value=_path)
        self.maxd_var = ttk.StringVar(value='4')
        self.type_var = ttk.StringVar(value='mp4')
        self.info_name_var = ttk.StringVar(value="")
        self.info_count_var = ttk.StringVar(value='0')


        # header and labelframe option container
        option_text = "Add the URL of the youtube video to begin download"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=10)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        # header and labelframe option container
        #settings_text = None
        #self.settings_lf = ttk.Labelframe(self, text=settings_text, padding=10)
        #self.settings_lf.pack(fill=X, expand=YES, anchor=N, pady=10)

        self.create_url_row()
        self.create_info_row()
        #self.create_path_row()
        #self.create_term_row()
        #self.create_type_row()
        #self.create_results_view()
        

    def create_url_row(self):
        """Add url row to labelframe"""
        url_row = ttk.Frame(self.option_lf)
        url_row.pack(fill=X, expand=YES)
        url_lbl = ttk.Label(url_row, text="URL", width=6)
        url_lbl.pack(side=LEFT, padx=(5, 0))
        url_ent = ttk.Entry(url_row, textvariable='self.url_var', width=55)
        url_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        browse_btn = ttk.Button(
            master=url_row, 
            text="Add to Queue", 
            command=self.addtoQueue, 
            width=13
        )
        browse_btn.pack(side=LEFT, padx=5)

    def create_info_row(self):
        """Add path row to labelframe"""
        info_row = ttk.Frame(self.option_lf)
        info_row.pack(fill=X, expand=YES)
        info_lbl = ttk.Label(info_row, textvariable='self.info_name_var', width=60)
        info_lbl.pack(side=LEFT, fill=X, expand=YES, padx=(15, 15), pady=(20, 20))
        info_lbl = ttk.Label(info_row, textvariable='self.info_count_var', width=4)
        info_lbl.pack(side=RIGHT, fill=X, expand=YES, padx=(15, 15), pady=(15, 15))        

    def create_path_row(self):
        """Add path row to labelframe"""
        button_row = ttk.Frame(self.settings_lf)
        button_row.pack(fill=X, expand=YES)

        Downloads_btn = ttk.Button(
            master=button_row, 
            text="Downloads", 
            command=self.on_browse, 
            width=12
        )
        Downloads_btn.pack(side=LEFT, padx=5)
        
        Exit_btn = ttk.Button(
            master=button_row, 
            text="Exit", 
            command=self.on_browse, 
            width=12
        )
        Exit_btn.pack(side=RIGHT, padx=5)
        
        settings_btn = ttk.Button(
            master=button_row, 
            text="Settings", 
            command=self.on_browse, 
            width=12
        )
        settings_btn.pack(side=RIGHT, padx=5)

        

    def on_browse(self):
        """Callback for directory browse"""
        path = askdirectory(title="Browse directory")
        if path:
            self.path_var.set(path)

    def addtoQueue(self):
        #Messagebox.ok(message='Added to Queue')
        url = pc.paste()
        if validators.url(url):
            # Need to check if url is valid youtube domain url.
            try:
                yt = YouTube(url)
            except URLError:
                Messagebox.ok(message='You are not connected to the internet')  

            dl = Thread(None,self.download,args=[yt])
            dl.start()
            self.count+=1
            self.setvar('self.url_var',url)
            self.setvar('self.info_name_var', yt.title)
            self.setvar('self.info_count_var', 'Downloads remaining'+str(self.count))
            t = Timer(3, self.clear_name, args=None, kwargs=None)
            t.start()
              
        else: 
            Messagebox.ok(message='Incorrect URL')
            self.clear_name()

    def clear_name(self):
        self.setvar('self.url_var','')
        self.setvar('self.info_name_var', '')

    def download(self, yt):
        yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download()
        #.download()
    

def calculate_position(app):
    """Position the toplevel in the center of the screen. Does not
    account for titlebar height."""
    app.update_idletasks()
    w_height = app.winfo_height()
    w_width = app.winfo_width()
    s_height = app.winfo_screenheight()
    s_width = app.winfo_screenwidth()
    xpos = (s_width - w_width) -20
    ypos = (s_height - w_height) -80
    app.geometry(f'+{xpos}+{ypos}')

    


if __name__ == '__main__':

    app = ttk.Window("Dad Youtube Downloader","superhero")
    app.attributes('-topmost', 1)
    YoutubeDownloader(app)
    calculate_position(app)
    app.mainloop()
