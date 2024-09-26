my_string=("Guvi geeks netwrok private ltd")
l=list(my_string)
freq=[l.count(ele) for ele in l]
d=dict(zip(l,freq))
print(d)
