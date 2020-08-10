#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Importing all the required Libraries

#Importing matplotlib
import matplotlib.pyplot as mpl

#Impoting numpy

import numpy as np

#Defining values for x and y
x = np.linspace(-50, 51, 200)
y = np.linspace(-50, 51, 200)
#meshgrid makes an array, this is useful in defining functions
x, y = np.meshgrid(x, y)

#Axes() as a function, this will highlight our origin
def axes():
    mpl.axhline(0, alpha= .2, linewidth= 2, color='k' )
    #Printing Horizontal line, X axis
    mpl.axvline(0, alpha= .2, linewidth= 2, color='k' )
    #Printing Vertical line, Y axis
    #mpl.axis('equal')

#For taking valid inputs as values, defining a f(n)
def options(prompt):
    while True:
        try:
            #Ensuring the input to be integer
            number = int(input(prompt))
            break
        except ValueError :
            #Printing Output for correction, Giving user another chance to enter value
            print('Please enter a Valid input ')
            pass
    return number
def delta(a,b,c,f,g,h):
    if a*(b)*c +2*f*g*h -a*f^2 -b*g^2 -c*h^2 != 0:
        return True
    else :
        return False
   

while True :
    print('Conic section Graphs')
    print('Menu \n 1. Parabola \n 2. Ellipse and circles \n 3. Hyperbolas \n 4.EXIT')
    opts = options(' Please enter any one of the options  ')
    if opts == 1:
        while True:
            print('PARABOLA')
            print("MENU \n 1. Parabola in standard equation \n 2. Parabola in Expanded equation \n 3.EXIT")
            ch = int(input('Choose an option'))
            if ch == 1:
                print('1. Parabola in standard equation')
                a = float(input('Please enter the value of \'a\' '  ))
                print(' Parabolas in standard eqn are of the form \n y^2 = 4ax ')
                print('Do you Want to see directrix and focus as well ? ')
                duff = input ('  y for YES and n for NO ')
                if duff == 'y':
                    axes()
                    # Printing Focus as a DOT.
                    mpl.plot(a, 0, '.')
                    # Printing Directrix, using a vertical line axvline.
                    mpl.axvline(-a)
                    mpl.contour(x, y, (y**2 - 4*a*x), [0], colors='r' )
                    mpl.show()
                   
                else :
                    axes()
                    mpl.contour(x, y, (y**2 - 4*a*x), [0], colors='k')
                    mpl.show()
                   
            elif ch == 2:
                while True:
                    print('2. Parabola in Expanded equation')
                    print('Parabolas in non-standard eqn are of the form :')
                    print('Ax^2+2Hxy+By^2+2Gx+2Fy+C=0, \n where H^2−4AB=0')
                    a = options(' Please enter the Value of A ')
                    b = options(' Please enter the Value of B ')
                    c = options(' Please enter the Value of C ')
                    f = options(' Please enter the Value of F ')
                    g = options(' Please enter the Value of G ')
                    h = options(' Please enter the Value of H ')
                   
                   
                   
                    if delta(a,b,c,f,g,h) and h**2 - 4*a*b == 0 :
                        print('Your Equation is : ')
                        print('\t',a,'^2x + ',h*2,'xy + ',b,'y^2 + ',g*2,'x + ',f,'y + ',g,' = 0 ' )
                        axes()
                        mpl.contour(x, y,(a*x**2 + 2*h*x*y + b*y**2 + 2*g*x + 2*f*y + c), [0], colors='k')
                        mpl.show()
                    else:
                        print('Condition : h**2 - 4*a*b = 0 \t NOT SATISFIED \n Try again :( ')
                        continue
            elif ch == 3 :
                 
                break
            else:
                continue
    elif opts == 2:
        while True:
            print('ELLIPSE AND CIRCLES')
            print("MENU \n 1. Circle  \n 2. Ellipse in Standard equation \n 3. Ellipse in Expanded equation \n 4.EXIT")
            ch = int(input('Choose an option'))
            if ch ==1 :
                print('1. Circle')
                r= int(input('Please enter radius of circle   '))
                h = int(input('Please enter x coordinate of centre   '))
                k = int(input('Please enter y coordinate of centre   '))
                print('Radius of circle  ',r, 'with centre ','(',h,',',k,')')
                t = np.linspace(0,2*np.pi, 1000)
                x = r*np.cos(t) + h
                y = r*np.sin(t) + k

                mpl.axis('equal')
                mpl.grid()
                mpl.plot(x,y)
                mpl.show()
            if ch==2:
                print('2. Ellipse in Standard equation')
                print('x^2/A^2 + y^2/B^2 = 1')
                a = options(' Please enter the Value of A ')
                b = options(' Please enter the Value of B ')
                print('Do you Want to see directrix and focus as well ? ')
                duff = input ('  y for YES and n for NO ')
                while True:
                    if duff == 'y':
                        axes()
                        h = int(input('Please enter x coordinate of centre   '))
                        k = int(input('Please enter y coordinate of centre   '))
                        t = np.linspace(0,2*np.pi, 1000)
                        p = h + a*np.cos(t)
                        q = k + b*np.sin(t)
                        mpl.axis('equal')
                        mpl.grid()
                        mpl.plot(p,q)
                        # Defining Eccentricity.
                        e = np.sqrt(1 - b**2/a**2)
                        # Printing Foci as DOTs.
                        mpl.plot(a*e, 0, '.', -a*e, 0, '.')
                        # Printing Directrix, using a vertical lines axvline
                        mpl.axvline(a/e)
                        mpl.axvline(-a/e)
                        mpl.show()
                        break
                    elif duff == 'n' :
                        axes()
                        h = int(input('Please enter x coordinate of centre   '))
                        k = int(input('Please enter y coordinate of centre   '))
                        t = np.linspace(0,2*np.pi, 1000)
                        p = h + a*np.cos(t)
                        q = k + b*np.sin(t)
                        mpl.axis('equal')
                        mpl.grid()
                        mpl.plot(p,q)
                        mpl.show()
                        break
                    else :
                        continue

            if ch ==3:
                while True:
                    print('3. Ellipse in Expanded equation')
                    print('For ellipses, the eccentricity,e is 0<e<1 \n It is defined as e**2 = 1 - B**2/A**2 ')
                    print('To define a ellipse in a non-standard position is has to follow the form :')
                    print('Ax^2+2Hxy+By^2+2Gx+2Fy+C=0, \n where H^2−4AB<0')
                    a = options(' Please enter the Value of A ')
                    b = options(' Please enter the Value of B ')
                    c = options(' Please enter the Value of C ')
                    f = options(' Please enter the Value of F ')
                    g = options(' Please enter the Value of G ')
                    h = options(' Please enter the Value of H ')
                    if delta(a,b,c,f,g,h) and h**2 - 4*a*b < 0:
                        print('Your Equation is : ')
                        print('\t',a,'^2x + ',h*2,'xy + ',b,'y^2 + ',g*2,'x + ',f,'y + ',g,' = 0 ' )
         
                        axes()
                        mpl.contour(x, y,(a*x**2 + 2*h*x*y + b*y**2 + 2*g*x + 2*f*y + c), [0], colors='k')
                        mpl.show()
                        break
                    else :
                        print('Condition : h**2 - 4*a*b < 0 \t NOT SATISFIED \n Try again :( ')
                        continue
   
            elif ch==4:
                break
            else:
                continue
    elif opts == 3:
        q = np.linspace(-100, 101, 200)
        w = np.linspace(-100, 101, 200)
        q, w = np.meshgrid(q, w)
        while True:
            print('HYPERBOLA')
            print('*** PRO TIP : Users are requested to use values less than 50, for best results :) ***')
            print("MENU \n 1. Hyperbola in standard equation \n 2. Hyperbola in Expanded equation \n 3.EXIT")
            ch = int(input('Choose an option'))
            if ch == 1:
                print('1. Hyperbolas in standard equation are of the form')
                print('x^2/A^2 - y^2/B^2 = 1 ')
                a = options(' Please enter the Value of A ')
                b = options(' Please enter the Value of B ')
       
                print('Do you Want to see directrix and focus as well ? ')
                duff = input ('  y for YES and n for NO ')
                while True:
                    if duff == 'y':
           
                        axes()
                        mpl.contour(q, w,(q**2/a**2 - w**2/b**2), [1], colors='k')
                        # Defining Eccentricity.
                        e = np.sqrt(1 + b**2/a**2)
                        # Printing Foci as DOTs.
                        mpl.plot(a*e, 0, '.', -a*e, 0, '.')
                        # Printing Directrix, using a vertical line axvline
                        mpl.axvline(a/e)
                        mpl.axvline(-a/e)
                        mpl.show()
                        break
                    elif duff =='n' :
                        axes()
                        mpl.contour(q, w,(q**2/a**2 - w**2/b**2), [1], colors='k')
                        mpl.show()
                        break
                    else:
                        continue
            elif ch == 2:
                while True:
                    print('2. Hperbola in Expanded equation')
                    print('Hyperbolas in non-standard eqn are of the form ::')
                    print('Ax^2+2Hxy+By^2+2Gx+2Fy+C=0, \n where H^2−4AB=0')
                    a = options(' Please enter the Value of A ')
                    b = options(' Please enter the Value of B ')
                    c = options(' Please enter the Value of C ')
                    f = options(' Please enter the Value of F ')
                    g = options(' Please enter the Value of G ')
                    h = options(' Please enter the Value of H ')
       
                    if delta(a,b,c,f,g,h) and h**2 - 4*a*b > 0 :
                        print('Your Equation is : ')
                        print('\t',a,'^2x + ',h*2,'xy + ',b,'y^2 + ',g*2,'x + ',f*2,'y + ',c,' = 0 ' )
                        axes()
                        mpl.contour(x, y,(a*x**2 + b*x*y + c*y**2 + d*x + e*y + f), [0], colors='k')
                        mpl.show()
                        break
                    else:
                        print('Condition : h**2 - 4*a*b > 0  \t NOT SATISFIED \n Try again :( ')
                        continue
            elif ch == 3 :
                break
            else:
                continue
    if opts == 4:
        break
print('EOP')


# In[ ]:




