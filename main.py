#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re,os



#################### USB API #######################
with open('demo.c', 'r', encoding='utf-8') as file:
    c_code = file.read()
matches = re.findall(r'/\*\*([^*]*\*+(?:[^/*][^*]*\*+)*)/', c_code, re.DOTALL)
# 打开config.h文件
with open('config.h', 'r', encoding='utf-8') as config_file:
    lines = config_file.readlines()

# 初始化计数器
num_hashes_before_usb_api = 0

# 遍历文件的每一行
for line in lines:
    # 如果找到了 "USB API" 所在行，停止搜索
    if "USB API" in line:
        # 计算该行中 # 字符的数量
        num_hashes_before_usb_api += line.count('#')    
        break

# 打印 "# "字符的数量
print("Number of # characters before 'USB API': %d" % num_hashes_before_usb_api)
uuuu = 0
with open('demo.md', 'w', encoding='utf-8') as md_file:
    md_file.write( "#"*(num_hashes_before_usb_api) + " " + "USB API" + "\n")
    for match in matches:
        function_name = re.search(r'\\fn\s+(.*?)\n', match)
        brief = re.search(r'\\brief\s*(.*?)(\n|\*/)', match, re.DOTALL)
        # param = re.search(r'\\param\s*(.*?)(\n|\*/)', match, re.DOTALL)
        param = re.search(r'\\param\s*(.*?)\\return', match, re.DOTALL)
        ret = re.search(r'\\return\s*(.*?)(\n|\*/)', match, re.DOTALL)

        if function_name:

            md_file.write( "#"*(num_hashes_before_usb_api+1) + " " + function_name.group(1) + "\n")

            if brief:
                md_file.write("- 描述\n\n" + brief.group(1).strip() + "\n")

            if param:
                print("*************")
                param_string = param.group(1).strip()
                if "(" in param_string and "#" in param_string:
                    file_name = re.search(r'#(.*?).h', param_string)
                    if file_name:
                        file_name = file_name.group(1) + '.h'
                        if os.path.exists(file_name):
                            with open(file_name, 'r') as header_file:
                                header_code = header_file.read()
                                # struct_match = re.search(r'struct\s+USERAPP_HID_EVENT', header_code)
                                # if struct_match:
                                #     print(">>>>Found USERAPP_HID_EVENT in {}:\n{}".format(file_name,struct_match.group()))
                                # 使用正则表达式匹配以 "USERAPP_HID_EVENT" 开头的 typedef struct
                                struct_match = re.search(r'typedef struct\s+USERAPP_HID_EVENT(.*?)\}USERAPP_HID_EVENT;', header_code, re.DOTALL)
                                uuuu = 1
                                if struct_match:
                                    userapp_hid_event_struct = struct_match.group(0).strip()
                                    print(userapp_hid_event_struct)

                                    
                # 将每一行的开头的*和空格去除
                lines = [line.lstrip('* ').strip() for line in param_string.split('\n') if line.strip()]
                md_file.write("- 参数\n")
                for line in lines:
                    if line:
                        if line.startswith("-"):
                            print(f"        {line}")
                            md_file.write(f"        {line}" + "\n")
                        else:
                            print(f"    - {line}")
                            md_file.write(f"    - {line}" + "\n")

                # if (uuuu == 1):
                #     md_file.write(f"    ")
                #     md_file.write(f"```"+"\n")
                #     userapp_hid_event_struct = struct_match.group(0).strip()
                #     md_file.write(f"        {userapp_hid_event_struct}" + "\n")
                #     md_file.write(f"    ")
                #     md_file.write(f"```"+"\n")
                
                
                # param_str = param.group(1).strip().replace("\n", "\n\t- ")
                # print("******1*******")
                # print(param_str)
                # if "(" in param_str and "#" in param_str:
                #     file_name = re.search(r'#(.*?).h', param_str)
                #     if file_name:
                #         file_name = file_name.group(1) + '.h'
                #         if os.path.exists(file_name):
                #             with open(file_name, 'r') as header_file:
                #                 header_code = header_file.read()
                #                 struct_match = re.search(r'struct\s+USERAPP_HID_EVENT', header_code)
                #                 if struct_match:
                #                     print("Found USERAPP_HID_EVENT in {}:\n{}".format(file_name,struct_match.group()))
                # print("******2*******")
                # lines = [line.lstrip(' * ').strip() for line in param_str.split('\n') if line.strip()]
                # for line in lines:
                #     if line:
                #         if line.startswith("-"):
                #             print(f"        {line}")
                #         else:
                #             print(f"    - {line}")
                # # print("- 参数\n\t- " + param_str + "\n")
                # md_file.write("- 参数\n\t- " + param_str + "\n")

            if ret:
                ret_str = ret.group(1).strip().replace("\n", "\n\t- ")
                md_file.write("- 返回值\n\t- " + ret_str + "\n")

            md_file.write("\n")


#################### Structure #######################
with open('demo2.h', 'r') as file:
    c_code = file.read()
matches = re.findall(r'/\*\*([^*]*\*+(?:[^/*][^*]*\*+)*)/', c_code, re.DOTALL)

# 打开config.h文件
with open('config.h', 'r', encoding='utf-8') as config_file:
    lines = config_file.readlines()

# 初始化计数器
num_hashes_before_usb_api = 0

# 遍历文件的每一行
for line in lines:
    # 如果找到了 "USB API" 所在行，停止搜索
    if "Structure" in line:
        # 计算该行中 # 字符的数量
        num_hashes_before_usb_api += line.count('#')    
        break

# 打印 "# "字符的数量
print("Number of # characters before 'USB API': %d" % num_hashes_before_usb_api)


with open('demo.md', 'a', encoding='utf-8') as md_file:
    md_file.write( "#"*(num_hashes_before_usb_api) + " " + "Structure" + "\n")
    for match in matches:
        function_name = re.search(r'\\fn\s+(.*?)\n', match)
        brief = re.search(r'\\brief\s*(.*?)(\n|\*/)', match, re.DOTALL)
        # param = re.search(r'\\param\s*(.*?)(\n|\*/)', match, re.DOTALL)

        if function_name:

            md_file.write( "#"*(num_hashes_before_usb_api+1) + " " + function_name.group(1) + "\n")

            if brief:
                md_file.write("- 描述\n\n" + brief.group(1).strip() + "\n")

            # if param:
            #     param_str = param.group(1).strip().replace("\n", "\n\t- ")
            #     if "(" in param_str and "#" in param_str:
            #         file_name = re.search(r'#(.*?).h', param_str)
            #         if file_name:
            #             file_name = file_name.group(1) + '.h'
            #             if os.path.exists(file_name):
            #                 with open(file_name, 'r') as header_file:
            #                     header_code = header_file.read()
            #                     struct_match = re.search(r'struct\s+USERAPP_HID_EVENT', header_code)
            #                     if struct_match:
            #                         print("Found USERAPP_HID_EVENT in {}:\n{}".format(file_name,struct_match.group()))
            #     md_file.write("- 参数\n\t- " + param_str + "\n")

            md_file.write("\n")
            
print("done")
