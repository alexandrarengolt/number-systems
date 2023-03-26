def roman_to_int(s:str)->int: #'MCMXCIV'
    res = 0
    d = {'CM' : 900, 'D' : 500,
    'CD' : 400, 'XC' : 90, 'XL' : 40, 'IX' : 9, 'IV' : 4, 'M' : 1000,
         'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
    for k in d:
        res+=d[k]*s.count(k)
        s=s.replace(k, '')
    return res

def int_to_roman(num:int)->str: #'1994'
    info = ['I', 'X', 'C', 'M']
    weird_number = ''
    i=0
    while num != 0:
        n=num%10
        weird_number=info[i]*n+weird_number
        num//=10 # num = num//10
        i+=1
    res = weird_number
    res = res.replace('IIIIIIIII','IX')
    res = res.replace('IIIII','V')
    res = res.replace('IIII','IV')
    res = res.replace('XXXXXXXXX','XC')
    res = res.replace('XXXXX','L')
    res = res.replace('XXXX','XL')
    res = res.replace('CCCCCCCCC','CM')
    res = res.replace('CCCCC','D')
    res = res.replace('CCCC','CD')
    return res
