from matplotlib import pyplot
import math
import numpy
def cheack(arry,a):
	i=0
	while i<len(arry):
		if a==arry[i].var:
			break
		i=i+1
	if i==len(arry):
		return -1
	return i
def nch(arry,a):
	i=0
	while i<len(arry):
		if arry[i][0]==a:
			break
		i=i+1
	if i!=len(arry):
		return i
	if i==len(arry):
		return -1
def giveval(arry,a):
	st=a.var
	i=0
	f1=a.var
	f2=a.coeff
	while i<len(st):
		st1=st[i]+st[i+1]
		r=nch(arry,st1)
		if r!=-1:
			f2=f2*arry[r][1]
			f1=f1.replace(st1,'')
		i=i+2
	if len(f1)==0:
		f1='konst'
	s=variable(f2,0,f1)
	return s	
def arrange(st):
	i=1
	a=st[0]
	arry=[]
	while i<len(st):
		e=int(st[i])
		arry.append(e)
		i=i+2
	arry=sorted(arry)
	i=0
	nst=''
	while i<len(arry):
		nst=nst+a+str(arry[i])
		i=i+1
	return nst


class variable:
	def __init__(self,coeff,tyype,var):
		self.coeff=coeff
		self.tyype=tyype
		self.var=var
	def __add__(self,other):
		count=self.tyype+other.tyype
		if count==1:
			if self.tyype==1:
				c=self
				d=other
			if other.tyype==1: 
				c=other
				d=self
		if count==0:
			if self.var==other.var:
				z=variable(0,0,self.var)
				z.coeff=self.coeff+other.coeff
				return z
			if self.var!=other.var:
				z=variable(0,1,0)
				x=variable(self.coeff,self.tyype,self.var)
				y=variable(other.coeff,other.tyype,other.var)
				arry=[x,y]
				z.var=arry
				return z
		if count==1:
			arry=c.var
			r=cheack(arry,d.var)
			if r==-1:
				arry.append(d)
			if r!=-1:
				arry[r].coeff=arry[r].coeff+d.coeff
			z=variable(0,1,arry)
			return z
		if count==2:
			arry=self.var
			z=self
			arry1=other.var
			i=0
			while i<len(arry1):
				z=z+arry1[i]
				i=i+1
			return z
	def __mul__(self,other):
		count=self.tyype+other.tyype
		if count==1:
			if self.tyype==1:
				c=self
				d=other
			if other.tyype==1:
				c=other
				d=self
		if count==0:
			p=0
			q=0
			if self.var=='konst':
				p=1
			if other.var=='konst':
				q=1
			if p+q==2:
				z=variable(1,0,'konst')
				z.coeff=self.coeff*other.coeff
				return z
			if p+q==1:
				if self.var=='konst':
					c1=self
					d1=other
				if other.var=='konst':
					c1=other
					d1=self
				z=variable(1,0,d1.var)
				z.coeff=d1.coeff*c1.coeff
				return z
			if p+q==0:
				z=variable(0,0,0)
				z.var=arrange(self.var+other.var)
				z.coeff=self.coeff*other.coeff
				return z
		if count==1:
			arry=c.var
			z=d*arry[0]
			i=1
			while i<len(arry):
				z=z+d*arry[i]
				i=i+1
			return z
		if count==2:
			arry=self.var
			arry1=other.var
			z=arry1[0]*self
			i=1
			while i<len(arry1):
				z=z+arry1[i]*self
				i=i+1
			return z
def solve(a,v,arry):
	if v.tyype==0:
		v=giveval(arry,v)
		return [v.var,-a/v.coeff]
	if v.tyype==1:
		i=0
		while i<len(v.var):
			r=giveval(arry,v.var[i])
			if i==0:
				z=r
			if i!=0:
				z=z+r
			i=i+1
		if len(z.var)>2:
			print ('too many variables')
			return 0
		if len(z.var)<2:
			print('too much information')
			return 0
		if len(z.var)==2:
			if z.var[0].var=='konst':
				c=0
				d=1
			if z.var[1].var=='konst':
				c=1
				d=0
			return [z.var[d].var,(a-z.var[c].coeff)/z.var[d].coeff]

v1=variable(3,0,'x1')
v2=variable(2,0,'x2')
v3=variable(2,0,'x1')
v4=variable(3,0,'x2')
a=(v1+v2+v3)*(v2+v1)
print(a.var[2].var)
print(q)
delta=0.001
v1=variable(1,0,'x1')
v2=variable(1,0,'x3')
v3=variable(.3,0,'x2')
v4=variable(1,0,'x0')
equ=v3+v2+v1
arry=[['x0',0],['x1',0],['x2',5]]
i=0
arryx0=[]
arryx1=[]
while i<(20/delta):
	r=solve(0,equ,arry)
	f=int(r[0][1])
	j=0
	while j<len(arry):
		f1=int(arry[j][0][1])
		if f<f1:
			arry.insert(j,r)
			break
		j=j+1
	if j==len(arry):
		arry.append(r)
	arryx0.append(arry[0][1])
	arryx1.append(arry[1][1])
	refarrry=arry
	arry=[]
	j=0
	while j<len(refarrry):
		if j==0:
			arry.append([refarrry[j][0],refarrry[j][1]+delta])
		if j!=0 and j<len(refarrry)-1:
			arry.append([refarrry[j][0],refarrry[j][1]+refarrry[j+1][1]*delta])
		j=j+1
	i=i+1
pyplot.plot(arryx0,arryx1)
pyplot.show()		
	
	

		
		


	






				
				


			
				
