str1 = "This is a sample string."

print(str1)

try:
    if(str1.index("Whatever")):
        pass
except:
    
    print("\"Whatever\" was not found in the string.")