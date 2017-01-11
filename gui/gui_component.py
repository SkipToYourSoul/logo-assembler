# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/10
Description: gui component with tkinter
"""
from gui.__init__ import *
import gui.gui_config as config
import gui.gui_controller as controller


class MainContainer(object):
    dir_name = ""
    icon_suffix = "tif"
    conf_suffix = "conf"
    backend_setting = config.get_backend_config()
    icon_count_setting = config.get_icon_count_config()
    icon_setting = config.get_icon_config()
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

        self.chinese_name = StringVar()
        self.chinese_label = Label(top_frame, text=u'中文名称')
        self.chinese_entry = Entry(top_frame, width=50, textvariable=self.chinese_name)

        self.code_number = StringVar()
        self.code_label = Label(top_frame, text=u'产品编号')
        self.code_entry = Entry(top_frame, width=50, textvariable=self.code_number)

        self.size_label = Label(top_frame, text=u'贴纸尺寸')
        self.size_comboBox = Pmw.ComboBox(top_frame, selectioncommand=self.change_backend_size,
                                          scrolledlist_items=self.backend_setting, entry_width=39)
        self.current_backend_size = self.backend_setting[0]
        self.size_comboBox.selectitem(self.current_backend_size)

        self.count_label = Label(top_frame, text=u'图标数量')
        self.count_comboBox = Pmw.ComboBox(top_frame, selectioncommand=self.change_icon_count,
                                           scrolledlist_items=self.icon_count_setting, entry_width=39)
        self.current_icon_count = self.icon_count_setting[0]
        self.count_comboBox.selectitem(self.current_icon_count)

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
        self.icon_size = StringVar()
        icon_size_frame = LabelFrame(master, text=u'图标大小选择', padx=5)
        icon_size_frame.pack(side=TOP, fill=BOTH, padx=20, pady=10)
        Radiobutton(icon_size_frame, text=u"添加小图标", variable=self.icon_size, value='40×30').grid(row=0, column=0, sticky=W)
        Radiobutton(icon_size_frame, text=u"添加中图标", variable=self.icon_size, value='60×40').grid(row=0, column=1, sticky=W)
        Radiobutton(icon_size_frame, text=u"添加大图标", variable=self.icon_size, value='80×60').grid(row=0, column=2, sticky=W)
        self.icon_size.set('40×30')

        # bottom frame: path filedialog
        bottom_frame = Frame(master)
        bottom_frame.pack(side=TOP, fill=BOTH, padx=20)
        self.output_path = StringVar()
        self.dir_entry = Entry(bottom_frame, textvariable=self.output_path, width=38)
        self.dir_button = Button(bottom_frame, command=self.open_dir, text=u'选择导出路径')
        self.dir_entry.grid(row=0, column=0, sticky=W)
        self.dir_button.grid(row=0, column=1, padx=5, sticky=E)

        # confirm fame: confirm bottom
        confirm_frame = Frame(master)
        confirm_frame.pack(side=TOP, fill=BOTH, padx=20, pady=10)
        self.confirm_button = Button(confirm_frame, width=50, command=self.confirm, text=u'确认')
        self.confirm_button.grid(row=0, column=0, sticky=W)

    def confirm(self):
        # step1: english_name, chinese_name, code_number is not empty
        if self.english_name.get().strip() == "":
            self.message_info("英文名不能为空")
            return
        if self.chinese_name.get().strip() == "":
            self.message_info("中文名不能为空")
            return
        if self.code_number.get().strip() == "":
            self.message_info("产品编号不能为空")
            return

        # step2: selected icons must be equal icon size
        selected_icon_count = 0
        icon_name_list = []
        for text, var in self.icon_states:
            if var.get() == 1:
                selected_icon_count += 1
                icon_name = "图标%s_%s.%s" % (self.icon_size.get(), text, self.icon_suffix)
                icon_name_list.append(icon_name)
        if selected_icon_count != int(self.current_icon_count):
            self.message_info("图标数量不匹配")
            return

        # step3: backend size must be equal icon size
        if not self.current_backend_size.startswith(self.icon_size.get()):
            self.message_info("背景图与图标大小不匹配")
            return

        # step4: output path is not empty
        if self.output_path.get().strip() == "":
            self.message_info("输出路径不能为空")
            return

        # get logo config
        conf_file_name = "%s-%s.%s" % (self.current_backend_size, self.current_icon_count, self.conf_suffix)
        config_dict = config.get_logo_config(conf_file_name)
        if not config_dict:
            self.message_info("配置文件'%s'不存在" % conf_file_name)
            return

        # construct output file name
        output_file_name = "%s/%s-%s.jpg" % (self.output_path.get(), self.current_backend_size, self.code_number.get())

        # parameters:
        # english_name, chinese_name, code_number, current_backend_size, current_icon_count, icon_name_list, output_path
        try:
            controller.assemble_logo(self.english_name.get(), self.chinese_name.get(), self.code_number.get(),
                                     self.current_backend_size, config_dict, icon_name_list, output_file_name)
        except Exception as e:
            traceback.print_exc()
            self.message_info("生成失败：%s", e)
            return
        self.message_info("生成成功，输出目录：\n%s" % output_file_name)

    def open_dir(self):
        self.dir_name = tkinter.filedialog.askdirectory()
        self.output_path.set(self.dir_name)
        if not self.dir_name:
            self.message_info("No directory was choose!")
            self.dir_name = ""
            return

    def message_info(self, message):
        tkinter.messagebox.showinfo(self.root, message)

    def change_backend_size(self, size):
        self.current_backend_size = size

    def change_icon_count(self, count):
        self.current_icon_count = count
