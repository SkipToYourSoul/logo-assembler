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
    out_image_suffix = "tif"
    backend_setting = None
    icon_count_setting = None
    icon_setting = None
    icon_states = []

    root_height = 300
    root_width = 600

    def help(self):
        tkinter.messagebox.showinfo(self.root, ' Author: liye \n Version: 1.0 \n Help email: liye.forwork@foxmail.com')

    def __init__(self, master=None):
        self.root = master

        # initial the config and root height
        try:
            self.backend_setting = config.get_backend_config()
            self.icon_count_setting = config.get_icon_count_config()
            self.icon_setting = config.get_icon_config()
            self.root_height = (int(
                (len(self.icon_setting) - 1) / 3) + 1) * 28 + 280  # 28px a line, base height is 250px
        except Exception as e:
            self.message_info("读取配置文件错误，请检查配置文件路径是否正确并重新运行！\n 错误原因：%s" % e)
            traceback.print_exc()
            sys.exit(1)

        # menu
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
        top_frame = Frame(master)
        top_frame.pack(side=TOP, fill=BOTH, padx=20, pady=10)

        self.english_name = StringVar()
        self.english_label = Label(top_frame, text=u'英文名称')
        self.english_entry = Entry(top_frame, bd=2, textvariable=self.english_name)

        self.chinese_name = StringVar()
        self.chinese_label = Label(top_frame, text=u'中文名称')
        self.chinese_entry = Entry(top_frame, bd=2, textvariable=self.chinese_name)

        self.code_number = StringVar()
        self.code_label = Label(top_frame, text=u'产品编号')
        self.code_entry = Entry(top_frame, bd=2, textvariable=self.code_number)

        self.size_label = Label(top_frame, text=u'贴纸尺寸')
        self.size_comboBox = Pmw.ComboBox(top_frame, selectioncommand=self.change_backend_size,
                                          scrolledlist_items=self.backend_setting, entry_width=25)
        self.current_backend_style = self.backend_setting[0]
        self.size_comboBox.selectitem(self.current_backend_style)

        self.count_label = Label(top_frame, text=u'图标数量')
        self.count_comboBox = Pmw.ComboBox(top_frame, selectioncommand=self.change_icon_count,
                                           scrolledlist_items=self.icon_count_setting, entry_width=25)
        self.current_icon_count = self.icon_count_setting[0]
        self.count_comboBox.selectitem(self.current_icon_count)

        self.english_label.grid(row=0, column=0, sticky=W)
        self.english_entry.grid(row=0, column=1, columnspan=3, sticky=W + E + N + S, padx=10, pady=5)
        self.chinese_label.grid(row=1, column=0, sticky=W)
        self.chinese_entry.grid(row=1, column=1, columnspan=3, sticky=W + E + N + S, padx=10, pady=5)
        self.code_label.grid(row=2, column=0, sticky=W)
        self.code_entry.grid(row=2, column=1, columnspan=3, sticky=W + E + N + S, padx=10, pady=5)
        self.size_label.grid(row=3, column=0, sticky=W)
        self.size_comboBox.grid(row=3, column=1, padx=10, pady=5, sticky=W + E + N + S)
        self.count_label.grid(row=3, column=2, sticky=W)
        self.count_comboBox.grid(row=3, column=3, padx=10, pady=5, sticky=W + E + N + S)

        # icon style frame: icon checkBox
        icon_style_frame = LabelFrame(master, text=u'注意事项图标选择', padx=5, height=50)
        icon_style_frame.pack(side=TOP, fill=BOTH, padx=20)

        for text, row, column in self.icon_setting:
            var = IntVar()
            Checkbutton(icon_style_frame, width=20, text=text, state='normal',
                        variable=var, onvalue=1, offvalue=0, anchor=W).grid(row=row, column=column, sticky=W)
            self.icon_states.append((text, var))

        # bottom frame: path filedialog
        bottom_frame = Frame(master)
        bottom_frame.pack(side=TOP, fill=BOTH, padx=20, pady=10)

        self.output_name = StringVar()
        self.output_name.set("example_filename")
        self.output_label = Label(bottom_frame, text=u'文件名')
        self.output_entry = Entry(bottom_frame, bd=2, width=49, textvariable=self.output_name)
        self.dpi_value = StringVar()
        self.dpi_value.set("300")
        self.dpi_label = Label(bottom_frame, text=u'图片DPI')
        self.dpi_entry = Entry(bottom_frame, bd=2, width=10, textvariable=self.dpi_value)

        self.output_label.grid(row=0, column=0, padx=5, sticky=W)
        self.output_entry.grid(row=0, column=1, padx=5, sticky=W + E + N + S)
        self.dpi_label.grid(row=0, column=2, padx=5, sticky=W)
        self.dpi_entry.grid(row=0, column=3, padx=5, sticky=W + E + N + S)

        file_frame = Frame(master)
        file_frame.pack(side=TOP, fill=BOTH, padx=20)
        self.output_path = StringVar()
        self.output_path.set(os.path.join(os.path.expanduser("~"), 'Desktop'))
        self.dir_entry = Entry(file_frame, textvariable=self.output_path, width=65, bd=2)
        self.dir_button = Button(file_frame, command=self.open_dir, text=u'选择导出路径')
        self.dir_entry.grid(row=1, column=1, sticky=W)
        self.dir_button.grid(row=1, column=0, padx=5, sticky=W + E + N + S)

        # confirm fame: confirm bottom
        confirm_frame = Frame(master)
        confirm_frame.pack(side=TOP, fill=BOTH, padx=20, pady=5)
        self.confirm_button = Button(confirm_frame, width=78, command=self.confirm, text=u'确认')
        self.confirm_button.grid(row=0, column=0, sticky=W + E + N + S)

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
                icon_name = "图标%s_%s.%s" % (self.current_backend_style.split('-')[0], text, self.icon_suffix)
                icon_name_list.append(icon_name)
        if selected_icon_count != int(self.current_icon_count):
            self.message_info("图标数量不匹配")
            return

        # step3: output path is not empty
        if self.output_path.get().strip() == "":
            self.message_info("输出路径不能为空")
            return

        # get logo config
        conf_file_name = "%s-%s.%s" % (self.current_backend_style, self.current_icon_count, self.conf_suffix)
        config_dict = config.get_logo_config(conf_file_name)
        if not config_dict:
            self.message_info("配置文件'%s'不存在" % conf_file_name)
            return

        # construct output file name
        if self.output_name.get() == "":
            self.output_name.set("example_filename")
        output_file_name = "%s/%s.%s" % (self.output_path.get(), self.output_name.get(), self.out_image_suffix)

        # parameters:
        # english_name, chinese_name, code_number, current_backend_style,
        # current_icon_count, icon_name_list, output_path
        try:
            controller.assemble_logo(self.english_name.get(), self.chinese_name.get(), self.code_number.get(),
                                     self.current_backend_style, config_dict, icon_name_list, output_file_name,
                                     self.dpi_value.get())
        except Exception as e:
            traceback.print_exc()
            self.message_info("生成失败，失败原因：\n%s" % e)
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
        self.current_backend_style = size

    def change_icon_count(self, count):
        self.current_icon_count = count
