import math
def congruent(a, b, mod):
    if b%math.gcd(a,mod)!=0:
        print("theres no solution")

    nsd=math.gcd(a,mod)
    if b%nsd==0:
        a = a/nsd
        b = b/nsd
        mod = mod/nsd
        print("%ix= %i mod %i"%(a,b,mod))

        i=1
        while i<mod:
            if (a*i)%mod==1:
                b=(b*i)%mod
                print("%i je výsledek kongruence"%(b))
                break
            else:
                i=i+1

congruent(9,15,12)