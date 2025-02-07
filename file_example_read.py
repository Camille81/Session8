fp = open("text.txt", "r")
print(fp.read())
fp.close()

with open("text.txt", "r") as fp:
    print(fp.read())

print("we are done, the context closed by the indent")

with open("text.txt", "r") as fp:
    for line in fp:
        print(line, end="")

with open("text.txt", "r") as fp:
    line_number = 1
    for line in fp:
        print(f"{line_number}:{line.rstrip()}")
        line_number +=1

