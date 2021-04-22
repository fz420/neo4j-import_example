import random
import string

from IPy import IP, IPint
from pprint import pprint


def gen_host():
    ascii_str = string.ascii_letters
    with open("./host.csv", "a+") as f:
        f.write("name,id:ID, ipv4_str,:LABEL\n")
        for i in range(101):
            name = "".join(random.sample(ascii_str, 6))
            ip_num = random.randint(0, 4294967296)
            ipv4_str = IPint(ip_num).strNormal()

            # name,ip:IP,ipv4_str,:LABEL
            line = name + "," + str(ip_num) + "," + ipv4_str + "," + "HOST"
            print(line)
            f.write(line + "\n")
            f.flush()


def gen_rel_host():
    with open("./host.csv", "r") as f:
        lines = f.readlines()
        lines = lines[1:]
        lines_len = len(lines)
        pprint(lines)

        with open("./rel_host.csv", "a+") as write_file:
            # 写入标题头
            write_file.write(":START_ID,:END_ID,TYPE\n")
            # 生成 100 条关系
            for i in range(101):
                src_host = lines[random.randint(0, lines_len - 1)].split(",")[1]
                dst_host = lines[random.randint(0, lines_len - 1)].split(",")[1]
                line = src_host + "," + dst_host
                write_file.write(line+"\n")
                write_file.flush()







if __name__ == '__main__':
    # gen_host()

    gen_rel_host()
