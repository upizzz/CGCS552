from math import *

def mul(listA,listB):	#listA(m*n) listB(n*o) matrix
	result=[[0 for x in range(3)]for y in range(3)]#resutl(m*o) 
	temp=int()
	for i in range(3):
		for j in range(3):
			temp=0
			for k in range(3):
				temp+= listA[i][k]*listB[k][j]+temp	
			result[i][j]=temp
	return result

def main():
	tx=input("\nTx:")
	ty=input("\nTy:")
	sx=input("\nSx:")
	sy=input("\nSy:")
	theta=input("\nTheta:\n")
	theta=theta*pi/180
	T=[[1, 0, tx],[0, 1, ty],[0, 0, 1]]
	S=[[sx, 0, 0],[0, sy, 0],[0, 0, 1]]
	R=[[round(cos(theta),2), round(-sin(theta),2), 0],[round(sin(theta),2), round(cos(theta),2), 0],[0, 0, 1]]
	print "Rotation matrix:\n", R
	print "Scaling Matrix:\n", S
	print "Translation:\n", T
	print "\n\n"
	print "multiplication of T,S"	
	print mul(T,S)
	print mul(S,T)
	print mul(R,S)==mul(S,R)
	print mul(T,S)==mul(S,T)
	print mul(T,R)==mul(R,T)
	print mul(S,R)==mul(R,S)
	

if __name__ == "__main__":
	main()
