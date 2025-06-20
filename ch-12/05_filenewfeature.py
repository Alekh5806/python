
## in old way 
with open('file1.txt') as f1:
    with open('file2.txt') as f2:
        data1 = f1.read()
        data2 = f2.read()

## in new way
with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    data1 = f1.read()
    data2 = f2.read()

print(data1)
print(data2)