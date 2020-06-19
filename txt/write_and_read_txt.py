
# Åbner filen i Append mode.
f = open("hej.txt", "a")

print(f.read())
# Skriver noget i filen
f.write(input())

# Lukker filen
f.close()

#open and read the file after the appending:
f = open("hej.txt", "r")
print(f.read())



