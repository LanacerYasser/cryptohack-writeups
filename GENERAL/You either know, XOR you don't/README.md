the hint of this challenge says `Remember the flag format and how it might help you in this challenge!` , as we know the flag format is : `crypto{XXX}` so let follow this steps :

1 - to solve this challenge we should find the weakness or the mistake that they have made using the xor function

2 - no script is provided so we can assume it uses a normal xor operation 

3 - the hint guid us to use the known first bytes of the the flag , here i mean `b'crypto{'` 

4 - so here we can start xor the first 7 bytes of the ciphertext with the known flag bytes i mentioned before to get a part of the key

5 - suprisely we get the following key : `b'myXORke'` , so we can be sure that our secret key is : `b'myXORkey'`

6 - now we xor each 8 bytes of the ciphertext with the secret key to get the FLAG
