def quadraticRoots(self, a, b, c):
        # code here
        d=b*b-4*a*c
        if d<0:
            return [-1]
        else:
            x=math.floor((-b+(math.sqrt(d)))/(2*a))
            y=math.floor((-b-(math.sqrt(d)))/(2*a))
            return sorted([x,y],reverse=True)
