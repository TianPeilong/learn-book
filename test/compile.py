filename = "D:/3_learn/MyGit/learn-book/test/2.py"
with open(filename) as f:
    source = f.read()
co = compile(source, filename, "exec")
type(co)
dir(co)

import dis
dis.dis(co) # 编译为字节码