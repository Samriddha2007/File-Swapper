def writeDataToFile1(file1,data2):
    with open(file1,'w') as x:
        x.write(data2)

def writeDataToFile2(file2,data1):
    with open(file2,'w') as z:
        z.write(data1)  
    
    print('Your data has been swapped')
    
def main():
    fileA=input("Enter the first file path/name: ")
    with open(fileA,'r') as a:
        dataA = a.read()

    fileB=input("Enter the second file path/name: ")
    with open(fileB,'r') as b:
        dataB = b.read()

    writeDataToFile1(fileA,dataB)
    writeDataToFile2(fileB,dataA)

main()

