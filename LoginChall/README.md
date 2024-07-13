This is th the first challenge you will meet when you are creating your account , since its yourfirst challenge in cryptohack i will try to explain every thing ,actuelly you need zero knowledge to solve it , lets explain how to solve it step by step :

1 - The challenge your are given is the following : ---Solve this Roman emperor's cipher: RTSYM EJGWF AFZQY HFYJLTWD---

2- from this message we can retrieve two important things : /--Roman emperor's cipher--\ and /--RTSYM EJGWF AFZQY HFYJLTWD--\

3 - for "RTSYM EJGWF AFZQY HFYJLTWD" it  represents the encrypted message which we actuelly call it ciphertext , so you should decrypt it to solve the challenge but HOW ?

4- now its the "Roman emperor's cipher" turn , when we google it we find that its actuelly a known famous cipher called Caesar cipher , so we should understand how it works to decrypt the message

5 - i suggest to read the wikipedia article carfuly to understand the cipher `https://en.wikipedia.org/wiki/Caesar_cipher` (not only for this challenge but for almost all the challenges you gonna face)

6 - read it ? cool , you should know that it uses a secret key to  shift every char from the plaintext ( our original message that we want to find )  and the end it will be decrypted and the result the cipher text (the same we were given)

7 - the decryption will do the inverse using the same key , so knowing the key will decrypt the message , but we don't know the key !! , yes but we can bruteforce (test all possible keys) it since its in the range (0-25) because we have only 26 characters ( the shift is circular ) 

7 - now we have 26 possibilities for the key , we can decrypt the the ciphertext each time using the key from 0 to 25 , so we gonna get : m1 , m2 , m3 , m4 ... m26 (each time we do the same using different key so the result will be different)

8 - now we got 26 plaintexts , but which one is the right one ? well you should know that the plaintext mostly have a meaning specially in such cases so the message that have 4 words that have meaning is the right plain text 

9 - congrates you solved your first cryptohack challenge now you should undestand how the old ceasar shift works and how to break it , the solv.py is my implementation for the ceaser shift for this challenge , you can use your own or even use online tools like `https://www.dcode.fr/caesar-cipher`

10 - good luck !!


