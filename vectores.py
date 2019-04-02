def Inclusion(u,v): 
    if len(v)<len(u): u, v = v, u
    return all([i in v for i in u])

def Incluir(U,V):
	m = len(U)
	n = len(V)
	r = 0
	resultado = 0
	if(n>m):
		for j in range(n):
			if (U[0] == V[j]):
				if(n-j>=m):
					for i in range(m):
						if(U[i]==V[j+i]):
							r+=1
				if (r == m):
					resultado+=1
			else:
				r = 0
	return resultado

U = [1,2,3]
V = [1,0,4,1,2,3,5]
print(Incluir(U,V))

print(Inclusion(U,V))

a,b=U,V

print([i in b for i in a]);