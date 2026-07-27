 
abc = "abcdefghijklmnopqrstuvwxyz "
 
uzenet = "helloworld"
kulcs = "abcdefgijkl"
 
rejtjeles = ""
 
for i in range(len(uzenet)):
    u_betu = uzenet[i]
    k_betu = kulcs[i]
 
    u_kod = abc.index(u_betu)
    k_kod = abc.index(k_betu)
 
    osszeg = u_kod + k_kod
 
    if osszeg > 26:
        osszeg = osszeg % 27
 
    rejtjeles = rejtjeles + abc[osszeg]
 
print("Eredeti uzenet:      ", uzenet)
print("Rejtjelezett uzenet: ", rejtjeles)
 
visszafejtett = ""
 
for i in range(len(rejtjeles)):
    r_betu = rejtjeles[i]
    k_betu = kulcs[i]
 
    r_kod = abc.index(r_betu)
    k_kod = abc.index(k_betu)
 
    kulonbseg = r_kod - k_kod
 
    if kulonbseg < 0:
        kulonbseg = kulonbseg + 27
 
    visszafejtett = visszafejtett + abc[kulonbseg]
 
print("Visszafejtett uzenet:", visszafejtett)