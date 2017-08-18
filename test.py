#----window create using tkinter module with menus---------------
from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    self.init_window()

  def init_window(self):
    self.master.title("Rocky")
    self.pack(fill=BOTH, expand = 1)
    # quitButton = Button(self, text = "Quit", command = self.client_exit)
    # quitButton.place(x=0,y=0)

    menu_da = Menu(self.master)
    self.master.config(menu=menu_da)

    file = Menu(menu_da)
    file.add_command(label='Save')
    file.add_command(label='Exit', command = self.client_exit)
    menu_da.add_cascade(label = 'File', menu= file)

    edit = Menu(menu_da)
    edit.add_command(label='Show Image', command = self.showImg)
    edit.add_command(label='Show text', command = self.showTxt)
    menu_da.add_cascade(label='Edit', menu= edit)

  def client_exit(self):
    exit()

  def showImg(self):
    load = Image.open('image.png')
    render = ImageTk.PhotoImage(load)

    img = Label(self, image=render)
    img.image = render
    img.place(x=0,y=0)

  def showTxt(self):
    text = Label(self, text='Hey there good!!')
    text.pack()

root = Tk()
root.geometry("700x300")
app = Window(root)
root.mainloop()


#-----------------parasing data from website with regular experssion
# import urllib.request
# import urllib.parse
# import re

# url = 'http://pythonprogramming.net'
# values = {'s':'basics',
#           'submit':'search'}

# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()

# paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

# for para in paragraphs:
#   print (para)

#--------------------fetching google results-----------
# import urllib.request
# import urllib.parse

# try:
#   url = 'https://www.google.co.in/search?q=srkrishna412@gmail.com'

#   headers = {"User-Agent":"Mozilla/4.0"}
#   req = urllib.request.Request(url, headers = headers)
#   resp = urllib.request.urlopen(req)
#   respData = resp.read()

#   saveFile = open('searchResult.html', 'w')
#   saveFile.write(str(respData))
#   saveFile.close()

# except Exception as e:
#   print (str(e))