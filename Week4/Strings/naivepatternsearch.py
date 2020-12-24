#Abhishek Anand
#naive search string

def search(text,pattern):
    
    n=len(text)
    m=len(pattern)
    
    for i in range(n-m+1):
        for j in range(m):
            if text[i+j]!=pattern[j]:
                break
        if j==m-1:
            print(pattern,"found at",i)
text=input()
pattern=input()
search(text,pattern)
