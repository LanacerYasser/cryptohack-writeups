from cryptohack we understand that the `Legendre Symbol` gives an efficient way to determine whether an integer is a quadratic residue modulo an odd prime p , so we have :

    (a / p) = 1 if a is a quadratic residue and a ≢ 0 mod p
    (a / p) = -1 if a is a quadratic non-residue mod p
    (a / p) = 0 if a ≡ 0 mod p 

Where `(a/p)` is simply : `a**((p-1)/2) mod p` and we can calculate it in python using : `pow(a,(p-1)//2,p)`


Cool now we are given a 1024 bit prime `p` and 10 integers `ints` and we have two steps to do :

1 - determine which integer from the 10 given is the quadratic residue using the Legendre symbol

2 - calculate its square root , so for example if the quadratic residue is a , we have  : 

    x**2 = a (mod p)

    which has 2 solutions x and -x mod p

1 - FIND THE QUADRATIC RESIDUE :

So first lets start by finding our quadratic residue integer from the 10 given using this simple loop :

    for i in ints :
      if pow(i,(p-1)//2,p) == 1 :
        a = i
        break


cool now we found the quadratic residue number from the list but the challenge isn't over , the hardest part starts now , we should find x and -x mod p and submit the larger one as your answer like they said , when you read the hint they said that `p = 3 (mod 4)` , every odd prime number can give either `1 mod 4` or `3 mod 4` , in our case we got 3 which is the simple case , i highly recommand to try every possible idea you got and give your time to the challenge before you see the solution , it is simple do not worry but this is very important to get better at math and start solving every challenge by your self

2 - FIND THE SOLUTIONS :


in every math problem the best thing you can do is to gether the informations you got and try to combine them and use them and also understand what you want to get , here we got two things :

    p = 3 (mod 4)
    a^(p-1)/2 = 1 (mod p)

    and we are trying to get this format x**2 = a (mod p) with known x 

from `p = 3 (mod 4)` we can understand that p+1 can be divided by 4 , so (p+1)/4 is an integer , and `(p+1)/4 multiplied by 2 is (p+1)/2` , and we know that in powers rules power is like multiplcation , i mean : `(a^3)^2 = a^6`, so we have :

    (a^(p+1)/4)^2 = a^(p+1)/2   (mod p)
    
    (a^(p+1)/4)^2 = a^(p-1+2)/2 (mod p)
    
    (a^(p+1)/4)^2 = a^(p-1)/2 * a (mod p)
    
    (a^(p+1)/4)^2 =  a (mod p)


    then : x1 = a^(p+1)/4  and x2 = -x1 mod p 
    
    
