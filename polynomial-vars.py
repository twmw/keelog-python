#
# Print all the variables needed for the BooleanPolynomialRing in sage.
#
# Cahlen Humphreys (2015)
ktxt = ""
ltxt = ""
atxt = ""
btxt = ""
full = ""

for i in range(0,64):
  ktxt+="K" + str(i) + ","

for i in range(0,160):
  atxt+="A" + str(i) + ","
  btxt+="B" + str(i) + ","

for i in range(0,192):
  ltxt+="L" + str(i) + ","

full+= ktxt + atxt + btxt + ltxt

fo = open("vars.txt", "wb")
fo.write(full)
fo.close()
