import tkinter as tk
from tkinter import filedialog, messagebox
from aip import AipOcr

# 初始化AipOcr对象
client = None


# 读取图片文件
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


def recognize_text(image):
    """
    调用百度AI的通用文字识别API，返回识别到的文字内容
    """
    options = {
        "detect_direction": "true",  # 检测文字方向
        "language_type": "CHN_ENG"  # 中文和英文混合识别
    }

    result = client.basicGeneral(image, options)

    # 提取文字内容
    text_content = ""
    if 'words_result' in result:
        for item in result['words_result']:
            text_content += item['words'] + "\n"  # 每个识别的文字后加换行

    return text_content.strip()  # 移除首尾空白字符


def select_image():
    """选择图片并进行文字识别"""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        image = get_file_content(file_path)
        recognized_text = recognize_text(image)

        # 写入到文本文件
        output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if output_file_path:
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(recognized_text)
            messagebox.showinfo("成功", "识别结果已保存到文本文件！")
        else:
            messagebox.showwarning("警告", "没有选择保存文件的路径！")


def initialize_client():
    """初始化AipOcr对象"""
    global client
    app_id = app_id_entry.get().strip()
    api_key = api_key_entry.get().strip()
    secret_key = secret_key_entry.get().strip()

    if not app_id or not api_key or not secret_key:
        messagebox.showwarning("警告", "请填写完整的API信息！")
        return

    client = AipOcr(app_id, api_key, secret_key)
    messagebox.showinfo("成功", "API信息已设置！请选择图片进行识别。")


# 创建主窗口
root = tk.Tk()
root.title("文字识别工具")
root.geometry("400x400")  # 窗口大小
root.configure(bg="#f0f0f0")  # 背景颜色

# 创建标题标签
title_label = tk.Label(root, text="文字识别工具", font=("Arial", 16), bg="#f0f0f0")
title_label.pack(pady=10)

# 创建输入框和标签
tk.Label(root, text="APP_ID:", bg="#f0f0f0").pack(pady=5)
app_id_entry = tk.Entry(root, width=50)
app_id_entry.pack(pady=5)

tk.Label(root, text="API_KEY:", bg="#f0f0f0").pack(pady=5)
api_key_entry = tk.Entry(root, width=50)
api_key_entry.pack(pady=5)

tk.Label(root, text="SECRET_KEY:", bg="#f0f0f0").pack(pady=5)
secret_key_entry = tk.Entry(root, width=50)
secret_key_entry.pack(pady=5)

# 创建初始化按钮
init_button = tk.Button(root, text="设置API信息", command=initialize_client, bg="#4CAF50", fg="white", width=20)
init_button.pack(pady=10)

# 创建选择图片按钮
select_button = tk.Button(root, text="选择图片", command=select_image, bg="#2196F3", fg="white", width=20)
select_button.pack(pady=20)

# 运行GUI
root.mainloop()
