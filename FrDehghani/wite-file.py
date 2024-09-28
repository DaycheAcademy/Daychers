with open("output.txt", "w") as file:
    # Write text to the file
    file.write("This is the content of the file.")
# ========================================================
print("*"*50)

fid = open("sample.txt", "r")
print(fid.read())
# ========================================================
print("*"*50)
for line in fid:
    print(line)