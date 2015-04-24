# keeloq-python
A repository of code that I used to break 160 rounds of the KeeLoq cryptosystem.  Everything is written in python
with the exception of some sage code which is used to converge a system of ANF boolean polynomial equations into
DIMACS CNF form.  Once in this form we can feed the output file to miniSAT which determines if the system is 
satisfiable.  If it is you can pipe the output to a file and parse it with the other python file and check to see
if the correct key was recovered.  

Usually you're going to have to feed miniSAT at least 32 bits of your key as a hint.  If you start taking away bits
of the key then your system is going to be underdefined (espeically if you're only giving it one pair of plaintext/ciphertext).  In this case the system is still satisifiable except you'll get the wrong key back since 
miniSAT stops as soon as it has found the system is satisfiable, and if the system is underdefined it will have 
multiple solutions.

The quick fix to this is to produce another of plaintext/ciphertext under the same key.  Then produce more equations
for the new plaintext/ciphertext, and all the intermediate variables.  The only thing that should remain the same is
the actual key variables.  Of course this system takes longer to solve, but you get the correct key back each time.  I experimented with this and was able to cut the key bit hints down to 25 bits with two pairs of plaintext/ciphertext -- however it took 14 hours to solve this system.
