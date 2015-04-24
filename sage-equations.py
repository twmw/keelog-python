#!/usr/bin/python
#
# Write equations needed to feed into sage in alpha-numeric form
#
# Cahlen Humphreys (2015)
fo = open("anf.txt", "wb")

ptext = "01100010100101110000101011100011"
ctext = "01101000110010010100101001111001"
key   = "00110100110111111001011000011100"

ptextl = list(ptext)
ctextl = list(ctext)
keyl = list(key)

ctextl.reverse()

ptextls = ""
ctextls = ""
keyls = ""

for i in range(0,32):
  ptextls+="L" + str(i) + "+" + str(ptext[i]) + ","
  ctextls+="L" + str(191-i) + "+" + str(ctext[31-i]) + ","
  keyls+="K" + str(i) + "+" + str(keyl[i]) + ","

fo.write("%s%s%s"%(ptextls,ctextls,keyls))
print ctextls;

for i in range(0,160):
  eq1 = str("L" + str(32+i)) + str("+" + "K" + str(i % 64)) + str("+L"+str(i)) + str("+L" + str(i+16)) + str("+L" + str(i+9)) + str("+L" + str(i+1)) + str("+L" + str(i+31) + "*" "L" + str(i+20))+str("+B" + str(i)) + str("+L" + str(i+26) + "*L" + str(i+20)) + str("+L" + str(i+26) + "*L" + str(i+1)) + str("+L" + str(i+20) + "*L" + str(i+9)) + str("+L" + str(i+9) + "*L" + str(i+1)) + str("+B" + str(i) + "*L" + str(i+9)) + str("+B" + str(i) + "*L" + str(i+20)) + str("+A" + str(i) + "*L" + str(i+9)) + str("+A" + str(i) + "*L" + str(i+20)) 
  eq2 = str("A" + str(i) + "+L" + str(i+31) + "*L" + str(i+26))
  eq3 = str("B" + str(i) + "+L" + str(i+31) + "*L" + str(i+1))
  fo.write("%s,%s,%s,"%(eq1,eq2,eq3))


fo.close();
