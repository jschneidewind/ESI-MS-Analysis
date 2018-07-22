from itertools import combinations_with_replacement

mass_CoT = 683.1586
charge_CoT = 3
n_samp = 8
margin = 0.01

#MeCN/HCOOH, high concentration

a = 2.0157
b = 43.9898
c = 46.0419
d = 32.0262
e = 31.0189
f = 1.0073
g = 45.0346
h = 1.0085
i = 46.0055
j = 1.0080
k = 72.0575
l = 30.0106
m = 44.9982
n = 18.0106
o = 17.0033
p = 48.0211
q = 47.0139
r = 279.9178
s = 27.9949
t = 41.0265
u = 99.0451

ca = 0
cb = 0
cc = 0
cd = 0    
ce = -1
cf = 1
cg = -1
ch = -1
ci = 0
cj = 0
ck = 0
cl = 0
cm = -1
cn = 0
co = -1
cp = 0
cq = -1
cr = -1
cs = 0
ct = 0
cu = -1
             
mz_exp = [101.096, 125.953, 140.948, 241.178, 291.253, 393.178, 420.903, 436.214, 529.007, 641.228, 671.239, 699.271, 715.154,
        740.170, 757.313, 813.375, 979.071, 1066.272, 1094.303, 655.244, 683.275, 727.304, 797.380, 629.095, 657.225,
        739.174, 125.961, 320.139, 363.310, 601.064, 782.208]  #782.208

input_m = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
input_c = [ca, cb, cc, cd, ce, cf, cg, ch, ci, cj, ck, cl, cm, cn, co, cp, cq, cr, cs, ct, cu]
input_alp = ['H2', 'CO2', 'EtOH', 'MeOH', 'MeO-', 'H+', 'EtO-', 'H-', 'HCOOH', 'H', 'THF', 'HCOH', 'HCOO-', 'H2O', 'OH-', 'HCOH*H2O', 'HCO-*H2O', 'NTf2-', 'CO', 'MeCN', 'acac-']

output_m = sum([map(list, combinations_with_replacement(input_m, i)) for i in range(1, n_samp)], []) #generation of mass combinations
output_c = sum([map(list, combinations_with_replacement(input_c, i)) for i in range(1, n_samp)], []) #generation of charge combinations
output_alp = sum([map(list, combinations_with_replacement(input_alp, i)) for i in range(1, n_samp)], []) #generation of name combinations

def calc_mz(x,y): #function for m/z calculation
    if y != 0: 
        return x / y
    if y == 0:
        return 0
                   
def main():
    
    mass_l = []
    charge_l = []
    mz_l = []    
    
    for i in range(len(output_m)):    #mass calculation
        mass = mass_CoT
        for j in range(len(output_m[i])):
            mass += output_m[i][j]
        
        mass_l.append(mass)
            
    for p in range(len(output_c)):   #charge calculation
        charge = charge_CoT
        for j in range(len(output_c[p])):
            charge += output_c[p][j]    
        
        charge_l.append(charge)
    
    for t in range(len(mass_l)):    #m/z calculation
        mz = calc_mz(mass_l[t],charge_l[t])
        mz_l.append(mz)           
                                     
    mz_lst = zip(output_alp, mz_l)   #m/z list is merged with name list, generating mz_lst
    
    mz_lst = [item for item in mz_lst if item[1] > 0] #mass/charge ratios equal or smaller than 0 are filtered out

    mz_lst.sort(key=lambda x: x[1]) #mz_lst is sorted by m/z values
    mz_exp.sort()   #experimental data is sorted
    
    print(len(mass_l))
    
    idx = 0       #calculated m/z values are checked against experimental data
    for i in mz_exp:
        while i > mz_lst[idx][1] and not abs(i - mz_lst[idx][1]) <= margin:
            idx+=1
        tempIdx = idx
        while abs(i - mz_lst[tempIdx][1]) <= margin:  
            print mz_lst[tempIdx] #when calculated m/z value is within margin of a peak, name and m/z are printed
            tempIdx+=1
                                            
main()