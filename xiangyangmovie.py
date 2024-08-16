import os
import requests

# 获取一级和二级目录
def get_directory_names(path):
    directories = []
    sub_directory_count = 0  # 用于统计二级目录的数量
    try:
        # 获取一级目录
        for dir_name in os.listdir(path):
            dir_path = os.path.join(path, dir_name)
            if os.path.isdir(dir_path):
                directories.append(dir_name)  # 添加一级目录
                # 获取二级目录
                sub_dirs = [f"  └── {sub_dir}" for sub_dir in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, sub_dir))]
                directories.extend(sub_dirs)  # 添加二级目录并缩进
                sub_directory_count += len(sub_dirs)  # 统计二级目录数量
    except PermissionError as e:
        print(f"无法访问路径 {path}：权限被拒绝。错误信息：{e}")
    except Exception as e:
        print(f"无法访问路径 {path}：{e}")
    return directories, sub_directory_count

# 生成包含所有目录名的文本
def generate_document(all_directories, total_sub_directories):
    document_content = "\n".join(all_directories)
    document_content += f"\n\nTotal number of second-level directories: {total_sub_directories}"
    return document_content

# 通过Telegram API发送消息到频道
def send_to_telegram(channel_id, bot_token, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": channel_id,
        "text": message
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("消息发送成功")
        else:
            print(f"消息发送失败，错误代码：{response.status_code}, 响应内容：{response.text}")
    except requests.exceptions.RequestException as e:
        print(f"网络请求失败：{e}")

# 主任务函数
def job():
    # 多个文件存储路径
    storage_paths = ["/app/cc1", "/app/cc2", "/app/cc3", "/app/cc4"]  # 添加你要扫描的路径

    all_directories = []
    total_sub_directories = 0
    for path in storage_paths:
        directories, sub_directory_count = get_directory_names(path)
        all_directories.extend(directories)
        total_sub_directories += sub_directory_count

    # 生成文档
    document_content = generate_document(all_directories, total_sub_directories)

    # 输出文档内容到控制台
    print(document_content)

    # Telegram bot 和 频道信息
    telegram_channel_id = os.getenv("TELEGRAM_CHANNEL_ID")
    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    if telegram_channel_id and telegram_bot_token:
        # 发送到Telegram频道
        send_to_telegram(telegram_channel_id, telegram_bot_token, document_content)
    else:
        print("Telegram频道ID或Bot Token未设置，无法发送消息。")

if __name__ == "__main__":
    # 立即运行任务
    job()
