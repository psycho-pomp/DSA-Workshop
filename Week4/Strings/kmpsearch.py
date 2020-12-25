

#Abhishek Anand
# kmp algorithm

def kmpsearch(text,pattern):
    
    n=len(text)
    m=len(pattern)
    lps=[0]*m
    computelps(pattern,m,lps)
    j=0
    i=0
    while i<n:
        if pattern[j]==text[i]:
            i+=1
            j+=1
        if j==m:
            print("pattern found at",i-j)
            j=lps[j-1]
        elif i<n and pattern[j]!=text[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
def computelps(pattern,m,lps):
    lps[0]
    l=0
    i=1
    while i<m:
        if pattern[i]==pattern[l]:
            l+=1
            lps[i]=l
            i+=1
        else:
            if l!=0:
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1
            
    
        
text=input()
pattern=input()
kmpsearch(text,pattern)

        
