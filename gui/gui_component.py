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
    dir_name = ""
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
    icon_setting = [
        ('0001_防潮', 0, 0),
        ('0002_小心划伤', 0, 1)
    ]
    icon_states = []

    def help(self):
        tkinter.messagebox.showinfo(self.root, ' Author: liye \n Version: 1.0 \n Help email: liye.forwork@foxmail.com')

    def __init__(self, master=None):
        # menu
        self.root = master
        self.menu_bar = Menu(master)

        # file menu
        file_menu = Menu(self.menu_bar, tearoff=0)
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

        self.english_name = StringVar()
        self.english_label = Label(top_frame, text=u'英文名称')
        self.english_entry = Entry(top_frame, width=50, textvariable=self.english_name)

        self.chinese_label = Label(top_frame, text=u'中文名称')
        self.chinese_entry = Entry(top_frame, width=50)

        self.code_label = Label(top_frame, text=u'产品编号')
        self.code_entry = Entry(top_frame, width=50)

        self.size_label = Label(top_frame, text=u'贴纸尺寸')
        self.size_comboBox = Pmw.ComboBox(top_frame, selectioncommand=self.change_backend_size,
                                          scrolledlist_items=self.backend_size, entry_width=39)
        self.current_backend_size = self.backend_size[0]
        self.size_comboBox.selectitem(self.current_backend_size)

        self.count_label = Label(top_frame, text=u'图标数量')
        self.count_comboBox = Pmw.ComboBox(top_frame, scrolledlist_items=self.icon_count, entry_width=39)
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

        # icon style frame: icon checkBox
        icon_style_frame = LabelFrame(master, text=u'注意事项图标选择', padx=5)
        icon_style_frame.pack(side=TOP, fill=BOTH, padx=20)

        for text, row, column in self.icon_setting:
            var = IntVar()
            Checkbutton(icon_style_frame, width=20, text=text, state='normal',
                        variable=var, onvalue=1, offvalue=0, anchor=W).grid(row=row, column=column, sticky=W)
            self.icon_states.append((text, var))

        # icon size frame: icon size
        self.icon_var = IntVar()
        icon_size_frame = LabelFrame(master, text=u'图标大小选择', padx=5)
        icon_size_frame.pack(side=TOP, fill=BOTH, padx=20, pady=10)
        Radiobutton(icon_size_frame, text=u"添加小图标", variable=self.icon_var, value=1).grid(row=0, column=0, sticky=W)
        Radiobutton(icon_size_frame, text=u"添加中图标", variable=self.icon_var, value=2).grid(row=0, column=1, sticky=W)
        Radiobutton(icon_size_frame, text=u"添加大图标", variable=self.icon_var, value=3).grid(row=0, column=2, sticky=W)
        self.icon_var.set(1)

        # bottom frame: path filedialog,
        bottom_frame = Frame(master)
        bottom_frame.pack(side=TOP, fill=BOTH, padx=20)
        self.entry_var = StringVar()
        self.dir_entry = Entry(bottom_frame, textvariable=self.entry_var, width=38)
        self.dir_button = Button(bottom_frame, command=self.open_dir, text=u'选择导出路径')
        self.dir_entry.grid(row=0, column=0, sticky=W)
        self.dir_button.grid(row=0, column=1, padx=5, sticky=E)

        # confirm fame: confirm bottom
        confirm_frame = Frame(master)
        confirm_frame.pack(side=TOP, fill=BOTH, padx=20, pady=10)
        self.confirm_button = Button(confirm_frame, width=50, command=self.confirm, text=u'确认')
        self.confirm_button.grid(row=0, column=0, sticky=W)

    def confirm(self):
        for text, var in self.icon_states:
            print(text)
            print(var.get())
        print(self.icon_var.get())
        print(self.english_name.get())
        print(self.current_backend_size)

    def open_dir(self):
        self.dir_name = tkinter.filedialog.askdirectory()
        self.entry_var.set(self.dir_name)
        if not self.dir_name:
            self.message_info("No directory was choose!")
            self.dir_name = ""
            return

    def message_info(self, message):
        tkinter.messagebox.showinfo(self.root, message)

    def change_backend_size(self, size):
        self.current_backend_size = size


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
