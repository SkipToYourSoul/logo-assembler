# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/10
Description: gui component with tkinter
"""

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import Pmw


class MainContainer(object):
    backend_size = ('40×30',
                    '40×30（加长50×30）',
                    '40×30横',
                    '40×30横（加长49×30）',
                    '40×30横（加长58×30）',
                    '40×30横（加长67×30）',
                    '60×40',
                    '60×40（加长75×40）',
                    '80×60',
                    '80×60（加长100×60）')
    icon_count = ('1', '2', '3', '4', '5', '6')

    def guide(self):
        self.console_text.insert(END, 'Please check the README.md\n'
                                      'More information will show in https://github.com/SkipToYourSoul/format-transfer')

    def clear(self):
        self.console_text.delete('1.0', '999999.0')

    def help(self):
        tkinter.messagebox.showinfo(self.root, ' Author: liye \n Version: 1.0 \n Help email: liye.forwork@foxmail.com')

    def __init__(self, master=None):
        # menu
        self.root = master
        self.menu_bar = Menu(master)

        # file menu
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Guide", command=self.guide)
        file_menu.add_command(label="Clear", command=self.clear)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=file_menu.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # help menu
        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.help)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        master.config(menu=self.menu_bar)

        # top frame: english_name, chinese_name, code
        top_frame = Frame(master, height=80)
        top_frame.pack(side=TOP, padx=20, pady=10)
        self.english_label = Label(top_frame, text=u'英文名称')
        self.english_entry = Entry(top_frame, width=50)

        self.chinese_label = Label(top_frame, text=u'中文名称')
        self.chinese_entry = Entry(top_frame, width=50)

        self.code_label = Label(top_frame, text=u'产品编号')
        self.code_entry = Entry(top_frame, width=50)

        self.size_label = Label(top_frame, text=u'贴纸尺寸')
        self.size_comboBox = Pmw.ComboBox(top_frame, selectioncommand=self.change_size,
                                          scrolledlist_items=self.backend_size)
        self.size_comboBox.selectitem(self.backend_size[0])

        self.count_label = Label(top_frame, text=u'图标数量')
        self.count_comboBox = Pmw.ComboBox(top_frame, scrolledlist_items=self.icon_count)
        self.count_comboBox.selectitem(self.icon_count[0])

        self.english_label.grid(row=0, column=0, sticky=W)
        self.english_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        self.chinese_label.grid(row=1, column=0, sticky=W)
        self.chinese_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        self.code_label.grid(row=2, column=0, sticky=W)
        self.code_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        self.size_label.grid(row=3, column=0, sticky=W)
        self.size_comboBox.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.count_label.grid(row=4, column=0, sticky=W)
        self.count_comboBox.grid(row=4, column=1, padx=10, pady=5, sticky=W)

    def open_dir(self):
        self.dir_name = tkinter.filedialog.askdirectory()
        self.entry_var.set(self.dir_name)
        if not self.dir_name:
            self.message_info("No directory was choose!")
            self.dir_name = ""
            return
        self.console_text.insert(END, '> You choose:\n' + self.dir_name + '\n> Files are as follows:' + '\n')
        for each_dir in os.listdir(self.entry_var.get()):
            self.console_text.insert(END, '> ' + each_dir + '\n')
        self.console_text.insert(END, '\n')
        self.console_text.update()

    def transfer_files(self):
        if self.dir_name == "":
            self.message_info("You must choose your file directory first!")
            return

    def message_info(self, message):
        tkinter.messagebox.showinfo(self.content_frame, message=message)

    def change_size(self, size):
        print(size)

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)

if __name__ == '__main__':
    root = Tk()
    root.title('Logo-assembler')
    root.resizable(0, 0)
    center_window(root, 400, 800)
    container = MainContainer(root)
    root.mainloop()
