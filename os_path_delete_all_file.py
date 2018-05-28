#!/usr/bin/env python3
#coding:utf-8
#删除文件和文件夹目录
import os
def delete_file(path):
    res = os.path.exists(path)
    if not res:
        print("指定目录不存在")
        return
    is_file = os.path.isfile(path)
    if is_file:
        os.remove(is_file)
        return
    all_files = os.listdir(path)
    for p in all_files:
        join_path = os.path.join(path,p)
        if os.path.isfile(join_path):
            os.remove(join_path)
        elif os.path.isdir(join_path):
            delete_file(join_path)
    os.rmdir(path)

path = r"E:\Python练习代码\test"
delete_file(path)


#只删除层层嵌套的空文件夹目录
import os
def delete_dir(path):
    res = os.path.exists(path)
    if not res:
        print("目录不存在")
    all_dir = os.listdir(path)
    if all_dir != []:
        for p in all_dir:
            join_path = os.path.join(path,p)
            delete_dir(join_path)
    os.rmdir(path)
    return

path = r"E:\Python练习代码\test - 副本"
delete_dir(path)
