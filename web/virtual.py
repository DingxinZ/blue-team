import random

rand_num = random.randint(1,4)
filename = "virtual_users/virtual_users%d.py" % rand_num
print(filename)
exec(open(filename).read())
