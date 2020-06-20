import pickle

# open a file, where you stored the pickled data
file = open('important', 'rb')


data = pickle.load(file)
print(data)
# close the file
file.close()

print('Showing the pickled data:')

cnt = 0
for item in data:
    print('The data ', cnt, ' is : ', item)
    cnt += 1
