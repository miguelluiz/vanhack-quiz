from compare import compareVersion


a,b = '1.2', '1.1'
print (compareVersion(a,b))
a,b = '1.2', '1.2'
print (compareVersion(a,b))

a,b = '1.2', '1.3'
print (compareVersion(a,b))

a,b = '1.0', '1'
print (compareVersion(a,b))

a,b = '1.0', '1.0.1'
print (compareVersion(a,b))


a,b = '1.0', '1.0.0.0.0.0.0.1'
print (compareVersion(a,b))

a,b = '10.0', '8.0.0.0.0.0.0.0'
print (compareVersion(a,b))


a,b = '10.0.0.0.0.0.0.1', '010.0.0.0.0.0.0.0'
print (compareVersion(a,b))

a,b = '10.0.0.0.0.0.0.1', '010.0.0.0.0.0.1.0'
print (compareVersion(a,b))

a,b = '10.0', '010.0.0.0.0.0.0.0'
print (compareVersion(a,b))

a,b = '10.0', '110.0.0.0.0.0.0.0'
print (compareVersion(a,b))

a,b = '010.0', '010.0.0.0.0.0.0.0'
print (compareVersion(a,b))

a,b = '101.0', '110.0.0.0.0.0.0.0'
print (compareVersion(a,b))

a,b = 'A-101.0', '110.0.0B.C0.D0.E0.#0.0)(*&'
print (compareVersion(a,b))

a, b = '01.10.100.001', '1.10.100.1'
print (compareVersion(a,b))

#only one value
print (compareVersion('10'))


#no one value
print (compareVersion())

#integers
print (compareVersion(10,5))

#help
print (compareVersion('-h'))

#HELP
print (compareVersion('-H'))

