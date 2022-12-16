def get_gcd(a, b):
    if b==0:
        return a 
    else:
        return get_gcd(b, a%b)

def congruent(a, b, mod):
    if b%get_gcd(a,mod)!=0:
        print("theres no solution")

    nsd=get_gcd(a,mod)
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

congruent(11,1,7171)