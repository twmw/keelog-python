#!/usr/bin/python
# keeloq encryption cipher
# 
# Cahlen Humphreys  (3/12/2015)

# Setup plaintext 32-bit plaintext block and 64-bit key, and number of rounds (keeloq wants 528).  change these at will.
PLAINTEXT = "01010101010101010101010101010101";
KEY = "0000010000100010100011100000000010000110000011001001111000010001"
ROUNDS = 528 

# convert plaintest and keys to variables, easier to shift.  initialize list for ciphertext, and some strings
# so they look pretty when we print them at the end. 
ptextl = list(PLAINTEXT);
keyl = list(KEY);
ciphertext = list();
ctext1="";
ptext1="";

# this is the non-linear function that is the heart of keeloq in algebraic normal form.
def core(a,b,c,d,e):
  return (d+e+a*c+a*e+b*c+b*e+c*d+d*e+a*d*e+a*c*e+a*b*d+a*b*c) % 2;

# these four functions shift the plaintext and the key according to the encryption scheme.  the shifting functions
# appended with a 'd' are used for decryption since we must go backwards.
def shiftp(p,newbit):
  p.append(newbit);
  del p[0];

def shiftpd(p,newbit):
  p.insert(0,newbit);
  del p[-1];

def shiftk(k):
  k.append(k[0]);
  del k[0];

def shiftkd(k):
  k.insert(0,k[-1]);
  del k[-1];

# this is a typical round function, where newb is our new bit we append to the end of the plaintext.
def encroundfunction(p,k,r):
  for i in range(0,r):
    newb = (int(k[0]) + int(p[0]) + int(p[16])  + core(int(p[31]),int(p[26]),int(p[20]),int(p[9]),int(p[1]))) % 2;
    shiftp(p,newb);
    shiftk(k);

# in a similar fashion, this is how we decrypt.  note we have to use the other shift functions because we're shifting
# the keys and plaintext the other way.
def decroundfunction(p,k,r):
  for i in range(0,r):
    newb = (int(k[15]) + int(p[31]) + int(p[15])  + core(int(p[30]),int(p[25]),int(p[19]),int(p[8]),int(p[0]))) % 2;
    shiftpd(p,newb);
    shiftkd(k);

# apply the actual encryption
encroundfunction(ptextl,keyl,ROUNDS);

# make ciphertext a string for pretty formatting
for i in range(len(ptextl)):
  ctext1+=str(ptextl[i]);

# print encryption results
print "Plaintext: " + PLAINTEXT;
print "Key: " + KEY;
print "Ciphertext: " + ctext1;

# our key is 64 bits, and we are going through 528 rounds.  note 528=64*8+16, so the key returns to its normal state 8 times,
# but is off by 16 shifts at the end.  so when we decrypt, we have to reinitialize the key (ie., we empty the list and fill it with 
# the original key.
del keyl[:];
keyl=list(KEY);

# apply the decryption
decroundfunction(ptextl,keyl,ROUNDS);

# make plaintext pretty for formatting
for i in range(len(ptextl)):
  ptext1+=str(ptextl[i]);

# print out plaintext
print "Decrypted: " + ptext1;
