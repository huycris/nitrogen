import string, requests, random

f = open("codes.txt", "a")
code_counter = 0
input("Press enter to activate\n")

while True:
  code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
  code_counter += 1
  print(f"{code_counter}  |  {code}")
  f.write(f"{code}\n")
  f.close
