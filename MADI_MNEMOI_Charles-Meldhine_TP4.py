#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:33:01 2020

@author: Charles-Meldhine Madi Mnemoi
"""
import math

#Exercice 1 :

class inSet(object):
    def __init__(self):
        self.vals= []
    def __str__(self):
        r_val = '{'
        for i,val in enumerate(self.vals):
            r_val = r_val + str(val) + ','
        
        r_val = r_val[:len(r_val)-1] + '}'
        return r_val
    def insert(self,e):
        if not e in self.vals:
            self.vals.append(e)     
    def member(self,e):
        return e in self.vals
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+' not found')
    def intersect(self,s2):
        I = inSet()
        for i in range(len(self.vals)):
            if self.vals[i] in s2.vals:
                I.insert(self.vals[i])
        
        return I
    def union(self,s2):
        U = inSet()
        U.vals = list(set(self.vals + s2.vals))
        return U
    def difference(self,s2):
        D = inSet()
        for i in range(len(self.vals)):
                if self.vals[i] not in s2.vals:
                    D.insert(self.vals[i])     
        return D
    def diff_sym(self,s2):
        DS = inSet()
        for i in range(len(self.vals)):
            if self.vals[i] not in s2.vals:
                DS.insert(self.vals[i])
        for i in range(len(s2.vals)):
            if s2.vals[i] not in self.vals:
                DS.insert(s2.vals[i])
                
        return DS
    def diff_sym_bis(self,s2):
        return self.union(s2).difference(self.intersect(s2))
    
#Exercice 2
class Complex(object):
    def __init__(self,a,b,cartesian=True):
            if cartesian:
                self.real = a
                self.imag = b
                self.to_polaire()
            else:
                self.rho = a
                self.theta = b
                self.to_cartesien()            
    def __add__(self,z):
        return Complex(self.real +z.real, 
                       self.imag +z.imag)
    def __sub__(self,z):
        return Complex(self.real -z.real, 
                       self.imag -z.imag)
    def __mul__(self,z):
        return Complex(self.rho*z.rho,
                       self.theta+z.theta)
    def __truediv__(self,z):
        return Complex(self.rho/z.rho,
                       self.theta-z.theta)
    def __module__(self):
        return math.sqrt(self.real**2 + self.imag**2)
    def __str__(self):
        return str(self.real) + '+' + str(self.imag) +'i'
    def print_polaire(self):
        return str(self.rho) + '.exp('+str(self.theta)+'i)'
    def to_polaire(self):
        self.rho = self.__module__()
        self.theta = math.acos(math.radians(self.real/self.rho))
    def to_cartesien(self):
        self.real = self.rho * math.cos(self.theta)
        self.imag = self.rho * math.sin(self.theta)
        
class Vecteur(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,v):
        return Vecteur(self.x+v.x,
                       self.y+v.y,
                       self.z+v.z)
    def __iadd__(self,v):
        return Vecteur(self.x+v.x,
                       self.y+v.y,
                       self.z+v.z)
    def __eq__(self,v):
        if self.x == v.x and self.y == v.y and self.z == v.z:
            return True
        else:
            return False
    def mult_scalaire(self,k):
        return Vecteur(k*self.x,
                       k*self.y,
                       k*self.z)
    def norme(self):
        return math.sqrt(self.x**2+
                         self.y**2+
                         self.z**2)
    def normaliser(self):
        norm = self.norme()
        self.x /= norm
        self.y /= norm
        self.z /= norm
    def produit_scalaire(self,v):
        return self.x*v.x+self.y*v.y+self.z*v.z
    def produit_vectoriel(self,v):
        return Vecteur(self.y*v.z-self.z*v.y,
                       self.z*v.x-self.x*v.z,
                       self.x*v.y-self.y*v.x)
    def est_orthogonal(self,v):
        if self.produit_scalaire(v) == 0:
            return True
        else:
            return False
    def est_colineaire(self,v):
        if self.produit_vectoriel(v) == Vecteur(0,0,0):
            return True
        else:
            return False
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
        
#Exercice 1

#1)
         
E = inSet()
E.insert(1)
E.insert(2)
E.insert(3)
E.insert(4)


#3) à 6)
s1 = inSet()
s2 = inSet()
s1.insert(1)
s1.insert(3)
s1.insert(4)
s1.insert(5)
s1.insert(8)
s2.insert(5)
s2.insert(7)
s2.insert(8)
s2.insert(9)

print(s1.intersect(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s1.diff_sym(s2))
print(s1.diff_sym_bis(s2))



#Exercice 2
"""
z1 = Complex(1,2)
z2 = Complex(1,math.pi/2,False)

print(z1)
print(z1.print_polaire())
print(z2)
print(z2.print_polaire())
print(z1+z2)
print(z1-z2)
print(z1*z2)
print(z1/z2)
print(z1.__module__())
"""

#Exercice 3

"""
u = Vecteur(1,0,0)
v = u.mult_scalaire(3)
w = Vecteur(0,1,0)
n = Vecteur(0,0,0)
n += u

print(u)
print(v)
print(n)
print(u+v)
print(u.produit_scalaire(w))
print(u.produit_vectoriel(v))
print(u.est_colineaire(v))
print(u.est_orthogonal(v))
print(u.est_orthogonal(w))
print(u.est_colineaire(w))
print(v.norme())
v.normaliser()
print(v)
"""
