def read(filename):
    with open(filename ,'r') as file:
        for line in file:
            yield line.strip()
        
        
for line in read('data/Retailsales.csv'):
    print(line)


