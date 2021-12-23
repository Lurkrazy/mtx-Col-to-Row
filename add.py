# coding: UTF-8  #设置编码
ff = open('./input/L-9-1.mtx', 'w')  # 打开一个文件，可写模式
with open('./input/L-9/L-9.mtx', 'r') as f:  # 打开一个文件只读模式
    line = f.readlines()  # 读取文件中的每一行，放入line列表中
    for line_list in line:
        line_new = line_list.replace('\n', '')  # 将换行符替换为空('')
        line_new = line_new+r' 1'+'\n'  # 行末尾加上"1",同时加上"\n"换行符
        print(line_new)
        ff.write(line_new)  # 写入一个新文件中
