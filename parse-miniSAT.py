#!/usr/bin/python
#
# parse the miniSAT output file for the key

originalkey = "0011010011011111100101100001110000011101100111001000001101110100"

keylist = list();
keystr = ""

with open('out.result') as f:
    words = f.read().split()

del words[0]
del words[64:]

for i in range(len(words)):
  if "-" in words[i]:
    keylist.append(0)
  else:
    keylist.append(1)

for i in range(len(keylist)):
  keystr+=str(keylist[i])

print "Original Key"
print originalkey
print "Key Parsed form miniSAT result file"
print keystr

