import os

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

    # 将文档内容保存到文件
    with open("directories.txt", "w", encoding="utf-8") as file:
        file.write(document_content)

    print("文档已生成并保存为 'directories.txt'。")

if __name__ == "__main__":
    # 立即运行任务
    job()
