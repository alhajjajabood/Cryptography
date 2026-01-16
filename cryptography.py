def caeser_enc (plaintxt,key,n):
    ciphertxt=''
    for x in plaintxt:
        if ord(x)==32 :
            ciphertxt=ciphertxt+x
        else:
          char_value = ord (x)-65
          new_value = (char_value+key)%n
          new_char = chr ((new_value+65))
          ciphertxt = ciphertxt+new_char
        #   print (x,"\t",char_value,"\t",new_value,"\t",new_char)
    print (ciphertxt)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3' Brut-force '4' Frequency Attack '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(1) 
    elif n==3:
        task(2)
    elif n==4:
        task(3)
    elif n==5:
        task(4)    
def caeser_dec (ciphertxt,key,n):
    plaintxt=''
    for x in ciphertxt:
        if ord(x)==32 :
            plaintxt=plaintxt+x
        else:
          char_value = ord (x)-65
          new_value = (char_value-key)%n
          new_char = chr ((new_value+65))
          plaintxt = plaintxt+new_char
    print ('plaintxt = ', plaintxt)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Brute Force '3' Frequency Attack '4' Encryption '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(2) 
    elif n==3:
        task(3)
    elif n==4:
        task(4)
    elif n==5:
        task(1)    
def caeser_analizy(ciphertxt,n):
    for key in range(0,26,1):
        print ('key = ',key, end="\t" )
        plaintxt=''
        for x in ciphertxt:
            if ord(x)==32:
                plaintxt=plaintxt+x
            else:
              char_value = ord (x)+65
              new_value = (char_value-int(key))%n
              new_char = chr(new_value+65)
              plaintxt = plaintxt + new_char
        print ('plaintxt = ', plaintxt,end='\n' )
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Frequency Attack '3' Decryption '4' Encryption '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(3) 
    elif n==3:
        task(4)
    elif n==4:
        task(2)
    elif n==5:
        task(1)   
def multi_enc(plaintxt,key,n):
    ciphertxt=''
    for x in plaintxt:
        if ord(x)==32 :
            ciphertxt=ciphertxt+x
        else:
           char_value = ord (x)+65
           new_value = (char_value*key)%n
           new_char = chr(new_value+65)
           ciphertxt=ciphertxt+new_char
    print( "ciphertxt = ",ciphertxt)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3' Brute Force '4'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(5)  
    elif n==3:
        task(6)
    elif n==4:
        task(7)
 
def multi_dec(ciphertxt,key_invers,n):
        def gcd(n,key_invers):
           q=[]
           r1=n
           r2=key_invers
           i=0
           while r2 > 0:
            q.insert(i,r1//r2)
            r=r1%r2
            r1=r2
            r2=r
            i=i+1
           Q=q
           if r1 == 1:
            return q
           return False
        def inverse(Q):
            t1=0
            t2=1
            for a in Q:
                t=t1-(t2*a)
                t1=t2
                t2=t
            if t1<0:
                t1=26+t1
            return t1
        gcd(n,key_invers)
        result=gcd(n,key_invers)
        if result!=False:
             invk= inverse(result)
        plaintxt=''
        for x in ciphertxt :
            if ord(x)==32 :
                plaintxt=plaintxt+x
            else:
               char_value=ord (x)-65
               new_value=(char_value*invk)%n
               new_char=chr(new_value+65)
               plaintxt=plaintxt+new_char
        print ('plaintxt = ',plaintxt)
        print('\n')
        print("Exit '00' Main Menu '1' Run Again '2' Encryption '3' Brute Force '4'")
        n=int(input())
        if n==00 or n==1:
         h(n)
        elif n==2:
            task(6)  
        elif n==3:
            task(5)
        elif n==4:
            task(7)
def multi_analizy(ciphertxt,n):
    def gcd(n,key_invers):
       q=[]
       r1=n
       r2=key_invers
       i=0
       while r2 > 0:
        q.insert(i,r1//r2)
        r=r1%r2
        r1=r2
        r2=r
        i=i+1
       Q=q
       if r1 == 1:
        return q
       return False
    def inverse(Q):
        t1=0
        t2=1
        for a in Q:
            t=t1-(t2*a)
            t1=t2
            t2=t
        if t1<0:
            t1=26+t1
        return t1
    for key_invers in range (1,n,2):
        print('Encrption_Key = ', key_invers,end="\t")
        gcd(n,key_invers)
        result=gcd(n,key_invers)
        if result!=False:
             invk= inverse(result)
        plaintxt=''
        for x in ciphertxt :
            if ord(x)==32 :
                plaintxt=plaintxt+x
            else:
               char_value=ord (x)-65
               new_value=(char_value*invk)%26
               new_char=chr(new_value+65)
               plaintxt=plaintxt+new_char
        print ('Plaintxt = ',plaintxt,"\t","Decryption Key = ", invk)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2'")
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3' Encryption '4'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(7)  
    elif n==3:
        task(6)
    elif n==4:
        task(5)  
def affine_enc(plaintxt,caeser_key,n,multi_key):
    ciphertxt=''
    for x in plaintxt:
        if ord(x)==32 :
            ciphertxt=ciphertxt+x
        else:
           s1 = ord (x)-65
           s2 = (s1*multi_key)
           s3=(s2+caeser_key)%n
           s4 = chr(s3+65)
           ciphertxt=ciphertxt+s4
        #print(x,'//',ord(x),'//',s1,'//',s2,'//',s3,'//',s4,'//',ord(s4),multi_key)
    print(ciphertxt)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3' Brute Force '4'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(8)  
    elif n==3:
        task(9)
    elif n==4:
        task(10) 
def affine_dec(ciphertxt,caesr_key,n,multi_key):
    def gcd(n,multi_key):
       q=[]
       r1=n
       r2=multi_key
       i=0
       while r2 > 0:
        q.insert(i,r1//r2)
        r=r1%r2
        r1=r2
        r2=r
        i=i+1
       Q=q
       if r1 == 1:
        return q
       return False
    def inverse(Q):
        t1=0
        t2=1
        for a in Q:
            t=t1-(t2*a)
            t1=t2
            t2=t
        if t1<0:
            t1=26+t1
        return t1
    gcd(n,multi_key)
    result=gcd(n,multi_key)
    if result!=False:
         invk= inverse(result)
    pplain=''
    for x in ciphertxt:
        if ord(x)==32 :
            pplain=pplain+x
        else:
           s1 = ord (x)-65
           s2 = (s1-caesr_key)
           s3=(s2*invk)%n
           s4 = chr(s3+65)
           pplain=pplain+s4
        #print(x,'//',ord(x),'//',s1,'//',s2,'//',s3,'//',s4,'//',ord(s4),'//',invk)
    print(pplain)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3' Brute Force '4'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(9)  
    elif n==3:
        task(8)
    elif n==4:
        task(10) 
def affine_analizing(ciphertxt,n):

    def gcd(n,multi_key):
       q=[]
       r1=n
       r2=multi_key
       i=0
       while r2 > 0:
        q.insert(i,r1//r2)
        r=r1%r2
        r1=r2
        r2=r
        i=i+1
       Q=q
       if r1 == 1:
        return q
       return False
    def inverse(Q):
        t1=0
        t2=1
        for a in Q:
            t=t1-(t2*a)
            t1=t2
            t2=t
        if t1<0:
            t1=26+t1
        return t1
    for i in range (0,n,1):
        for j in range (1,n,2):
            gcd(n,j)
            result=gcd(n,j)
            if result!=False:
                 invk= inverse(result)
            print('caesr_key = ',i,'\t','multi_key = ',j,'\t','inverse = ',invk,end='\t')
            pplain=''
            for x in ciphertxt:
                if ord(x)==32 :
                    pplain=pplain+x
                else:
                   s1 = ord (x)-65
                   s2 = (s1-i)
                   s3=(s2*invk)%n
                   s4 = chr(s3+65)
                   pplain=pplain+s4
            print(pplain)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3' Encryption  '4'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(10)  
    elif n==3:
        task(9)
    elif n==4:
        task(8)  
def Playfair_enc(plaintext,key):
    def build_key_matrix(key):
        key = key.upper().replace("J", "I").replace(" ", "")
        key_prepare = list(dict.fromkeys(key))  
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  

        for ch in alphabet:
            if ch not in key_prepare:
                key_prepare.append(ch)


        matrix = [["" for _ in range(5)] for _ in range(5)]
        index = 0
        for i in range(5):  #matrix[0][] i=0 j=0,j=1,j=2,j=3,j=4
            for j in range(5):
                matrix[i][j] = key_prepare[index]
                index += 1
        return matrix


    def prepare_plaintext(text):
        text = text.upper().replace("J", "I").replace(" ", "")
        pairs = []
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else "X" 
            if a == b:  
                pairs.append(a + "X")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        if len(pairs[-1]) == 1: 
            pairs[-1] += "X"
        return pairs


    def find_position(matrix, letter): 
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j
        return None


    def encrypt_pair(pair, matrix): #a,b o,x o,d
        a, b = pair[0], pair[1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  
            return matrix[row_a][(col_a+1)%5] + matrix[row_b][(col_b+1)%5]
        elif col_a == col_b:  
            return matrix[(row_a+1)%5][col_a] + matrix[(row_b+1)%5][col_b]
        else:  
            return matrix[row_a][col_b] + matrix[row_b][col_a]


    def playfair_encrypt(plaintext, matrix):
        pairs = prepare_plaintext(plaintext)
        ciphertext = ""
        for pair in pairs:
            ciphertext += encrypt_pair(pair, matrix)
        return ciphertext



    key_matrix = build_key_matrix(key)

    print("\nKey Matrix:")
    for row in key_matrix:
        print(row)

    ciphertext = playfair_encrypt(plaintext, key_matrix)
    print("\nPlaintext:", plaintext.upper())
    print("Ciphertext:", ciphertext)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3' World List Brute Force '4' N! Brute Force '5' Frequency Attack '6' ")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(11) 
    elif n==3:
        task(12)
    elif n==4:
        task(13)
    elif n==5:
        task(14)
    elif n==6:
        task(15)   
def Playfair_dec(ciphertext,key):
    
    def build_key_matrix(key):
        key = key.upper().replace("J", "I").replace(" ", "")
        key_prepare = list(dict.fromkeys(key))  
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  

        for ch in alphabet:
            if ch not in key_prepare:
                key_prepare.append(ch)

        matrix = [["" for _ in range(5)] for _ in range(5)]
        index = 0
        for i in range(5):
            for j in range(5):
                matrix[i][j] = key_prepare[index]
                index += 1
        return matrix

    def find_position(matrix, letter):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j
        return None

    def decrypt_pair(pair, matrix):
        a, b = pair[0], pair[1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  
            return matrix[row_a][(col_a-1)%5] + matrix[row_b][(col_b-1)%5]
        elif col_a == col_b:  
            return matrix[(row_a-1)%5][col_a] + matrix[(row_b-1)%5][col_b]
        else:  
            return matrix[row_a][col_b] + matrix[row_b][col_a]

    def playfair_decrypt(ciphertext, matrix):
        pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        plaintext = ""
        for pair in pairs:
            plaintext += decrypt_pair(pair, matrix)
        return cleanup_text(plaintext)

    def cleanup_text(text):
        result = ""
        i = 0
        while i < len(text):
            if i < len(text)-2 and text[i] == text[i+2] and text[i+1] == "X":
                result += text[i]
                i += 2
            else:
                result += text[i]
                i += 1
        if result.endswith("X"):
            result = result[:-1]
        return result



    key_matrix = build_key_matrix(key)

    print("\nKey Matrix:")
    for row in key_matrix:
        print(row)

    decrypted = playfair_decrypt(ciphertext.upper(), key_matrix)

    
    print("\nCiphertext:", ciphertext.upper())
    print("Decrypted (with I):", decrypted)
    print("Decrypted (with J):", decrypted.replace("I", "J"))  
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3' World List Brute Force '4' N! Brute Force '5' Frequency Attack '6' ")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(12) 
    elif n==3:
        task(11)
    elif n==4:
        task(13)
    elif n==5:
        task(14)
    elif n==6:
        task(15)   
def Playfair_analizing(ciphertext):
    ciphertext=ciphertext.upper()
    def build_key_matrix(key):
        key = key.upper().replace("J", "I").replace(" ", "")
        key_prepare = list(dict.fromkeys(key))  
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
        for ch in alphabet:
            if ch not in key_prepare:
                key_prepare.append(ch)
        matrix = [["" for _ in range(5)] for _ in range(5)]
        index = 0
        for i in range(5):
            for j in range(5):
                matrix[i][j] = key_prepare[index]
                index += 1
        return matrix

    def find_position(matrix, letter):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j
        return None

    def decrypt_pair(pair, matrix):
        a, b = pair[0], pair[1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b: 
            return matrix[row_a][(col_a-1)%5] + matrix[row_b][(col_b-1)%5]
        elif col_a == col_b: 
            return matrix[(row_a-1)%5][col_a] + matrix[(row_b-1)%5][col_b]
        else:  
            return matrix[row_a][col_b] + matrix[row_b][col_a]

    def playfair_decrypt(ciphertext, matrix):
        pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        plaintext = ""
        for pair in pairs:
            plaintext += decrypt_pair(pair, matrix)
        return cleanup_text(plaintext)

    def cleanup_text(text):
        result = ""
        i = 0
        while i < len(text):
            if i < len(text)-2 and text[i] == text[i+2] and text[i+1] == "X":
                result += text[i]
                i += 2
            else:
                result += text[i]
                i += 1
        if result.endswith("X"):
            result = result[:-1]
        return result


    candidate_keys = [ "PLAYFAIR", "EXAMPLE", "MONARCHY", "KEYWORD", "CIPHER",
            "SECRET", "ENCRYPT", "DECODE", "MESSAGE", "CODE",
            "BREAK", "FREQUENCY", "ATTACK", "ANALYSIS", "CRYPTO",
            "SECURITY", "ALGORITHM", "COMPUTER", "PROGRAM", "LANGUAGE",
            "PYTHON", "MATRIX", "CIPHER", "DECRYPT", "ENCODE",
            "LONDON", "ENGLAND", "AMERICA", "GERMANY", "FRANCE",
            "RUSSIA", "CHINA", "JAPAN", "CANADA", "AUSTRALIA",
            "ROME", "PARIS", "BERLIN", "MOSCOW", "TOKYO",
            "PASSWORD", "PRIVATE", "CONFIDENTIAL", "CLASSIFIED",
            "MILITARY", "GOVERNMENT", "OFFICIAL", "DOCUMENT",
            "REPORT", "INFORMATION", "INTELLIGENCE", "BATTLE",
            "VICTORY", "STRATEGY", "TACTICAL", "OPERATION",
            "COMMUNICATION", "TELEGRAM", "RADIO", "WIRELESS",
            "AGENT", "SPY", "ESPIONAGE", "COVERT", "UNDERCOVER",
            "KEY", "CODE", "WORD", "TEXT", "DATA", "FILE", "NOTE",
            "LETTER", "PAGE", "BOOK", "PAPER", "WRITE", "READ",
            "WAR", "PEACE", "ARMY", "NAVY", "AIRFORCE", "MARINE",
            "GENERAL", "COLONEL", "CAPTAIN", "LIEUTENANT", "SERGEANT",
            "SOLDIER", "OFFICER", "COMMAND", "CONTROL", "DEFENSE",
            "WEAPON", "MISSION", "TARGET", "OBJECTIVE", "POSITION",
            "ALICE", "BOB", "CHARLIE", "DAVID", "EVE", "FRANK",
            "GRACE", "HENRY", "IVAN", "JOHN", "KATE", "LINDA",
            "MICHAEL", "NANCY", "OSCAR", "PETER", "QUEEN", "ROBERT",
            "SMITH", "THOMAS", "UNION", "VICTOR", "WILLIAM", "XAVIER",
            "YVONNE", "ZACHARY", "ADAM", "BEN", "CAROL", "DANIEL",
            "UNITED", "STATES", "KINGDOM", "EUROPE", "ASIA", "AFRICA",
            "AMERICAN", "BRITISH", "FRENCH", "GERMAN", "RUSSIAN",
            "CHINESE", "JAPANESE", "ITALIAN", "SPANISH", "DUTCH",
            "LONDON", "WASHINGTON", "BERLIN", "MOSCOW", "BEIJING",
            "TOKYO", "PARIS", "ROME", "MADRID", "AMSTERDAM", "VIENNA",
            "ALGORITHM", "PROTOCOL", "SYSTEM", "NETWORK", "DATABASE",
            "SOFTWARE", "HARDWARE", "COMPUTING", "PROCESSING", "ANALYSIS",
            "CALCULATION", "COMPUTATION", "ENCRYPTION", "DECRYPTION",
            "CIPHER", "CODE", "KEY", "SECRET", "PASSWORD", "AUTHENTICATION",
            "BATTLE", "WARFARE", "STRATEGY", "TACTICS", "OPERATION",
            "MISSION", "COMMAND", "CONTROL", "INTELLIGENCE", "SECURITY",
            "DEFENSE", "OFFENSE", "ATTACK", "DEFEND", "CAPTURE",
            "RETREAT", "ADVANCE", "VICTORY", "DEFEAT", "SURRENDER",
            "PLAY", "FAIR", "MONARCH", "SECRETKEY", "MESSAGECODE",
            "BREAKCODE", "FREQUENCYANALYSIS", "CIPHERBREAK", "DECODER",
            "ENCODER", "CRYPTANALYSIS", "CRYPTOGRAPHY", "STEGANOGRAPHY",
            "QUANTUM", "COMPUTING", "ANALYTICS", "STATISTICS", "MATHEMATICS",
            "GEOMETRY", "ALGEBRA", "CALCULUS", "PROBABILITY", "STATISTICAL", "SHADI","ABOOD"]

    for key in candidate_keys:
        matrix = build_key_matrix(key)
        decrypted = playfair_decrypt(ciphertext, matrix)
        print(f"\nKey: {key}")
        print("Decrypted (with I):", decrypted)
        print("Decrypted (with J):", decrypted.replace("I", "J"))
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3' Encryption '4' N! Brute Force '5' Frequency Attack '6' ")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(13) 
    elif n==3:
        task(12)
    elif n==4:
        task(11)
    elif n==5:
        task(14)
    elif n==6:
        task(15)    
def hill_enc():
    def mod_inverse(a, m=26):
            a = a % m
            for x in range(1, m):
                if (a * x) % m == 1:
                    return x
            return None

    def determinant(matrix, m=26):  
        n = len(matrix)
        if n == 1:
            return matrix[0][0] % m
        if n == 2:
            return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % m
        det = 0
        for c in range(n):
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1)**c) * matrix[0][c] * determinant(minor, m)
        return det % m

    def is_invertible(matrix, m=26):    
        det = determinant(matrix, m)
        inv_det = mod_inverse(det, m)
        return inv_det is not None

    def multiply_row(row, matrix, m=26):    
            n = len(matrix)
            result = []
            for j in range(n):
                total = 0
                for k in range(n):
                    total += row[k] * matrix[k][j]
                result.append(total % m)
            return result

    plaintxt = input("Enter the message to encrypt (A-Z only): ").upper()
    n = int(input("Enter the value of N: "))

    while len(plaintxt) % n != 0:  
        plaintxt += "X"

    while True: 
        matrix_letters = [["" for _ in range(n)] for _ in range(n)]
        matrix_prepare = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                char = input(f"Enter the value of key[{i}][{j}](A-Z only) : ").upper()
                matrix_letters[i][j] = char
                matrix_prepare[i][j] = ord(char) - 65


        if is_invertible(matrix_prepare, 26):
            print("Key matrix is invertible. Proceeding with encryption...")
            break
        else:
            print("Key matrix is NOT invertible mod 26. Please enter new values.")

    plaintxt_prepare = [ord(p) - 65 for p in plaintxt]
    z = len(plaintxt_prepare) // n 
    pmatrix_prepare = [[0 for _ in range(n)] for _ in range(z)]

    k = 0
    for x in range(z):  
        for y in range(n):
            pmatrix_prepare[x][y] = plaintxt_prepare[k]
            k += 1

    cipher_matrix = []
    cipher = ""

    for row in pmatrix_prepare:
        result = multiply_row(row, matrix_prepare, 26)
        cipher_matrix.append(result)
        cipher += "".join(chr(val + 65) for val in result)

    print("\n==================\n")
    print("Key matrix (letters as entered) : \n")
    for row in matrix_letters:
        print(row)
    print("\n==================\n")
    print("Ciphertext:", cipher)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3' Brute Force '4' Frequency Attack '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(16)  
    elif n==3:
        task(17)
    elif n==4:
        task(18)
    elif n==5:
        task(19)
def hill_dec():
    def mod_inverse(a, m=26):
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def determinant(matrix, m=26):
        n = len(matrix)
        if n == 1:
            return matrix[0][0] % m
        if n == 2:
            return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % m
        det = 0
        for c in range(n):
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1)**c) * matrix[0][c] * determinant(minor, m)
        return det % m

    def cofactor_matrix(matrix, m=26):
        n = len(matrix)
        cof = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                minor = [row[:j] + row[j+1:] for k,row in enumerate(matrix) if k != i]
                cof[i][j] = ((-1)**(i+j)) * determinant(minor, m)
        return cof

    def transpose(matrix):
        return [list(row) for row in zip(*matrix)]

    def matrix_mod_inverse(matrix, m=26):
        det = determinant(matrix, m)
        inv_det = mod_inverse(det, m)
        if inv_det is None:
            raise ValueError("Key matrix is not invertible under mod {}".format(m))
        cof = cofactor_matrix(matrix, m)
        adj = transpose(cof)
        inv = [[(adj[i][j] * inv_det) % m for j in range(len(matrix))] for i in range(len(matrix))]
        return inv

    def multiply_row(row, matrix, m=26):
        n = len(matrix)
        result = []
        for j in range(n):
            total = 0
            for k in range(n):
                total += row[k] * matrix[k][j]
            result.append(total % m)
        return result

    cipher = input("Enter the ciphertext (A-Z only): ").upper()
    n = int(input("Enter the value of N: "))

    while len(cipher) % n != 0:
        cipher += "X"

    matrix_prepare = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            char = input(f"Enter the value of key[{i}][{j}](A-Z only) : ").upper()
            matrix_prepare[i][j] = ord(char) - 65  

    cipher_prepare = [ord(c) - 65 for c in cipher]
    z = len(cipher_prepare) // n
    cmatrix_prepare = [[0 for _ in range(n)] for _ in range(z)]

    k = 0
    for x in range(z):
        for y in range(n):
            cmatrix_prepare[x][y] = cipher_prepare[k]
            k += 1


    inv_key = matrix_mod_inverse(matrix_prepare, 26)


    plaintext_matrix = []
    plaintext = ""

    for row in cmatrix_prepare:
        result = multiply_row(row, inv_key, 26)
        plaintext_matrix.append(result)
        plaintext += "".join(chr(val + 65) for val in result)


    print("\n==================")
    print("Decrypted Plaintext : \n", plaintext)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3' Brute Force '4' Frequency Attack '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(17)  
    elif n==3:
        task(16)
    elif n==4:
        task(18)
    elif n==5:
        task(19)  
def hill_analizing ():
    def mod_inverse(a, m=26):
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def determinant(matrix, m=26):
        return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % m

    def is_invertible(matrix, m=26):
        det = determinant(matrix, m)
        return mod_inverse(det, m) is not None

    def multiply_row(row, matrix, m=26):
        result = []
        for j in range(2):  
            total = 0
            for k in range(2):
                total += row[k] * matrix[k][j]
            result.append(total % m)
        return result

    def inverse_matrix_2x2(matrix, m=26):
        det = determinant(matrix, m)
        inv_det = mod_inverse(det, m)
        if inv_det is None:
            return None
        a, b = matrix[0]
        c, d = matrix[1]
        inv = [[d, -b],
            [-c, a]]
        for i in range(2):
            for j in range(2):
                inv[i][j] = (inv[i][j] * inv_det) % m
        return inv

    print ("This task work with n = 2 only ")
    cipher = input("Enter ciphertext (A-Z only): ").upper()

    cipher_nums = [ord(c) - 65 for c in cipher]
    z = len(cipher_nums) // 2
    cmatrix = [[0, 0] for _ in range(z)]

    k = 0
    for x in range(z):
        for y in range(2):
            cmatrix[x][y] = cipher_nums[k]
            k += 1

    letters = [chr(i + 65) for i in range(26)]
    count = 0

    with open("all_candidates.txt", "w") as f:
        for a in letters:
            for b in letters:
                for c in letters:
                    for d in letters:
                        key_letters = [[a, b], [c, d]]
                        key_nums = [[ord(a)-65, ord(b)-65],
                                    [ord(c)-65, ord(d)-65]]
                        if is_invertible(key_nums, 26):
                            inv_key = inverse_matrix_2x2(key_nums, 26)
                            if inv_key is None:
                                continue
                            plaintext = ""
                            for row in cmatrix:
                                result = multiply_row(row, inv_key, 26)
                                plaintext += "".join(chr(val + 65) for val in result)
                            count += 1
                            line = f"Key {key_letters} -> Plaintext: {plaintext}\n"
                            f.write(line)

        f.write(f"\nTotal invertible keys tested: {count}\n")

    print(f"\nAll {count} results saved to all_candidates.txt")   
    print("\n==================")
    # print("Decrypted Plaintext : \n", plaintext)
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2'")
    n=int(input())
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3' Decryption '4' Frequency Attack '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(18)  
    elif n==3:
        task(16)
    elif n==4:
        task(17)
    elif n==5:
        task(19)
def playfair_n():
    def create_playfair_grid(key):
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        grid = []
        used_chars = set()
    
        for char in key:
            if char not in used_chars:
                grid.append(char)
                used_chars.add(char)
    
        for char in alphabet:
            if char not in used_chars:
                grid.append(char)
    
        return [grid[i:i+5] for i in range(0, 25, 5)]

    def find_position(grid, char):
        for i in range(5):
            for j in range(5):
                if grid[i][j] == char:
                    return i, j
        return None

    def prepare_text(text):
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        text = text.upper().replace('J', 'I')
        clean_text = ''
        for char in text:
            if char in alphabet:
                clean_text += char
    
        pairs = []
        i = 0
        while i < len(clean_text):
            if i + 1 < len(clean_text):
                if clean_text[i] == clean_text[i + 1]:
                    pairs.append(clean_text[i] + 'X')
                    i += 1
                else:
                    pairs.append(clean_text[i] + clean_text[i + 1])
                    i += 2
            else:
                pairs.append(clean_text[i] + 'X')
                i += 1
        return pairs

    def decrypt_pair(grid, pair):
        a, b = pair[0], pair[1]
        row1, col1 = find_position(grid, a)
        row2, col2 = find_position(grid, b)
    
        if row1 == row2:
            return grid[row1][(col1 - 1) % 5] + grid[row2][(col2 - 1) % 5]
        elif col1 == col2:
            return grid[(row1 - 1) % 5][col1] + grid[(row2 - 1) % 5][col2]
        else:
            return grid[row1][col2] + grid[row2][col1]

    def decrypt_playfair(ciphertext, key):
        grid = create_playfair_grid(key)
        pairs = prepare_text(ciphertext)
        plaintext = ''
    
        for pair in pairs:
            plaintext += decrypt_pair(grid, pair)
    
        return plaintext

    def format_key_matrix(key):
        """Format the key as a 5x5 matrix"""
        matrix_str = ""
        for i in range(0, 25, 5):
            row = key[i:i+5]
            matrix_str += "  " + " ".join(row) + "\n"
        return matrix_str

    def brute_force_all_keys(ciphertext):
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
        file = open("playfaier_brutN!_attack.txt", "w")
        file.write("Playfair Complete Brute Force - All 25! Possible Keys\n")
        file.write("=" * 60 + "\n")
        file.write(f"Ciphertext: {ciphertext}\n")
        file.write("Total possible keys: 15,511,210,043,330,985,984,000,000\n")
        file.write("=" * 60 + "\n\n")
    
        count = 0
    
        def generate_keys(current_key, remaining_chars):
            nonlocal count
        
            if len(current_key) == 25:
                try:
                    plaintext = decrypt_playfair(ciphertext, current_key)
                    file.write(f"Key {count}: {current_key}\n")
                    file.write("Key Matrix:\n")
                    file.write(format_key_matrix(current_key))
                    file.write(f"Plaintext: {plaintext}\n")
                    file.write("-" * 50 + "\n")
                    count += 1
                
                    if count % 1000 == 0:
                        print(f"Progress: {count} keys tried...")
                    
                except Exception as e:
                    file.write(f"Key {count}: {current_key} - ERROR: {str(e)}\n")
                    file.write("-" * 50 + "\n")
                    count += 1
                return
        
            for i in range(len(remaining_chars)):
                new_key = current_key + remaining_chars[i]
                new_remaining = remaining_chars[:i] + remaining_chars[i+1:]
                generate_keys(new_key, new_remaining)
    
        print("Starting complete brute force attack...")
        print("This will try ALL 25! possible keys (15,511,210,043,330,985,984,000,000)")
        print("This will take longer than the age of the universe to complete")
        print("Output will be saved to 'playfaier_brutN!_attack.txt'")
        print("Press Ctrl+C to stop execution")
    
        generate_keys("", alphabet)
    
        file.write(f"\nTotal keys tried: {count}\n")
        file.close()
        print(f"Brute force completed. All 25! keys tried.")
        print(f"Results saved to 'playfaier_brutN!_attack.txt'")


    ciphertext = input("Enter the ciphertext: ")
    if len(ciphertext)%2==0:
        brute_force_all_keys(ciphertext)
    else:
        print("Ciphertext Not Valid Try Again")
        playfair_n()

    playfair_n()

    playfair_n()
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3' Decryption '4' World List Brute Force '5' Frequency Attack '6' ")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(14) 
    elif n==3:
        task(11)
    elif n==4:
        task(12)
    elif n==5:
        task(13)
    elif n==6:
        task(15)   
def hillfreq():

    mod = 26
    ascii_A = 65
    
    english_freq = [
        8.17, 1.29, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15,
        0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.06,
        2.76, 0.98, 2.36, 0.15, 1.97, 0.07
    ]

    def char_to_num(char):
        return ord(char) - ascii_A

    def num_to_char(num):
        return chr(num + ascii_A)

    def text_to_numbers(text):
        return [char_to_num(char) for char in text]

    def numbers_to_text(numbers):
        return ''.join(num_to_char(num) for num in numbers)

    def mod_inverse(a, m):
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def matrix_determinant(matrix):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    def matrix_adjugate(matrix):
        return [
            [matrix[1][1], (-matrix[0][1]) % mod],
            [(-matrix[1][0]) % mod, matrix[0][0]]
        ]

    def matrix_mod_inverse(matrix):
        det = matrix_determinant(matrix)
        det_mod = det % mod
        det_inv = mod_inverse(det_mod, mod)
        
        if det_inv is None:
            return None
        
        adjugate = matrix_adjugate(matrix)
        
        inverse = []
        for i in range(2):
            row = []
            for j in range(2):
                element = (adjugate[i][j] * det_inv) % mod
                row.append(element)
            inverse.append(row)
        
        return inverse

    def matrix_vector_multiply(matrix, vector):
        result = []
        for i in range(2):
            total = 0
            for j in range(2):
                total += matrix[i][j] * vector[j]
            result.append(total % mod)
        return result

    def decrypt(ciphertext, key_matrix):
        numbers = text_to_numbers(ciphertext)
        key_inverse = matrix_mod_inverse(key_matrix)
        
        if key_inverse is None:
            return None
        
        if len(numbers) % 2 != 0:
            numbers.append(char_to_num('A'))
        
        plain_numbers = []
        for i in range(0, len(numbers), 2):
            block = numbers[i:i+2]
            decrypted_block = matrix_vector_multiply(key_inverse, block)
            plain_numbers.extend(decrypted_block)
        
        return numbers_to_text(plain_numbers)

    def calculate_frequency_score(text):
        if len(text) == 0:
            return 999999.0
        
        freq_count = [0] * 26
        total_letters = 0
        
        for char in text:
            idx = char_to_num(char)
            freq_count[idx] += 1
            total_letters += 1
        
        if total_letters == 0:
            return 999999.0
        
        chi_squared = 0
        for i in range(26):
            expected = english_freq[i] * total_letters / 100.0
            observed = freq_count[i]
            if expected > 0:
                chi_squared += ((observed - expected) ** 2) / expected
        
        return chi_squared

    def is_matrix_invertible(matrix):
        det = matrix_determinant(matrix)
        det_mod = det % mod
        return mod_inverse(det_mod, mod) is not None

    def generate_all_possible_keys():
        keys = []
        total_attempts = 0
        invertible_count = 0
        
        print("Generating invertible 2x2 matrices...")
        
        valid_determinants = set()
        for det in range(mod):
            if mod_inverse(det, mod) is not None:
                valid_determinants.add(det)
        
        for char1 in range(ascii_A, ascii_A + 26):
            c1 = char1 - ascii_A
            for char2 in range(ascii_A, ascii_A + 26):
                c2 = char2 - ascii_A
                for char3 in range(ascii_A, ascii_A + 26):
                    c3 = char3 - ascii_A
                    for char4 in range(ascii_A, ascii_A + 26):
                        total_attempts += 1
                        c4 = char4 - ascii_A
                        
                        det = (c1 * c4 - c2 * c3) % mod
                        if det in valid_determinants:
                            matrix = [[c1, c2], [c3, c4]]
                            key_info = {
                                'matrix': matrix,
                                'chars': [chr(char1), chr(char2), chr(char3), chr(char4)]
                            }
                            keys.append(key_info)
                            invertible_count += 1
        
        print(f"Found {invertible_count} invertible keys")
        return keys

    def frequency_attack_all_keys(ciphertext):
        print(f"\nAnalyzing: {ciphertext}")
        
        possible_keys = generate_all_possible_keys()
        print(f"Testing {len(possible_keys)} keys...")
        
        results = []
        
        for key_info in possible_keys:
            plaintext = decrypt(ciphertext, key_info['matrix'])
            if plaintext is not None:
                score = calculate_frequency_score(plaintext)
                results.append((score, plaintext, key_info))
        
        print(f"Found {len(results)} valid decryptions")
        return results

    def get_ciphertext_from_user():
        print("HILL CIPHER FREQUENCY ATTACK")
        print("Tests ALL possible invertible 2x2 key matrices")
        
        while True:
            ciphertext = input("\nEnter ciphertext (A-Z only): ").strip().upper()
            
            if not ciphertext:
                print("Error: Ciphertext cannot be empty!")
                continue

            valid = True
            for char in ciphertext:
                if not ('A' <= char <= 'Z'):
                    valid = False
                    break
            
            if not valid:
                print("Error: Ciphertext must contain only A-Z!")
                continue
            
            return ciphertext

    def save_all_results_to_file(results, ciphertext, filename=None):
        if filename is None:
            filename = f"hill_cipher_attack_results_{ciphertext}.txt"
        
        print(f"Saving {len(results)} results to {filename}")
        
        f = open(filename, 'w')
        f.write("HILL CIPHER FREQUENCY ATTACK RESULTS\n")
        f.write(f"Ciphertext: {ciphertext}\n")
        f.write(f"Total decryptions found: {len(results)}\n")
        f.write("Results in original order\n\n")
        
        for i, (score, plaintext, key_info) in enumerate(results, 1):
            matrix = key_info['matrix']
            chars = key_info['chars']
            
            f.write(f"RESULT #{i}\n")
            f.write(f"Frequency Score: {score:.6f}\n")
            f.write(f"Decrypted Text: {plaintext}\n")
            f.write(f"Key Matrix Characters: {chars[0]}{chars[1]}{chars[2]}{chars[3]}\n")
            f.write(f"Numeric Key Matrix:\n")
            f.write(f"  [{matrix[0][0]:2d} {matrix[0][1]:2d}] = [{chars[0]} {chars[1]}]\n")
            f.write(f"  [{matrix[1][0]:2d} {matrix[1][1]:2d}]   [{chars[2]} {chars[3]}]\n")
            f.write("-" * 60 + "\n\n")
        
        f.close()
        
        print(f"Saved to {filename}")

    def display_top_results(results, top_n=20):
        print(f"\nFirst {top_n} results:")
        
        for i, (score, plaintext, key_info) in enumerate(results[:top_n], 1):
            chars = key_info['chars']
            
            print(f"{i:2d}. Score: {score:8.2f} | Key: {chars[0]}{chars[1]}{chars[2]}{chars[3]} | Text: {plaintext}")

    while True:
        ciphertext = get_ciphertext_from_user()
        
        print(f"\nStarting analysis...")
        
        results = frequency_attack_all_keys(ciphertext)
        
        if results:
            # display_top_results(results, 20)
            save_all_results_to_file(results, ciphertext)
            
            print(f"\nComplete! Found {len(results)} decryptions")
        else:
            print("No valid decryptions found!")
        break
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3' Decryption '4' Brute Force '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(19)  
    elif n==3:
        task(16)
    elif n==4:
        task(17)
    elif n==5:
        task(18)  
def plyfairfreq():
    english_freq = {
        'A': 8.17, 'B': 1.29, 'C': 2.78, 'D': 4.25, 'E': 12.70,
        'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 6.97, 'K': 0.77,
        'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51, 'P': 1.93,
        'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06, 'U': 2.76,
        'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97, 'Z': 0.07
    }
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    def generate_matrix(key):
        key = key.upper().replace('J', 'I')
        used_chars = set()
        matrix = []
        
        for char in key:
            if char not in used_chars and char in alphabet:
                used_chars.add(char)
                if len(matrix) == 0 or len(matrix[-1]) == 5:
                    matrix.append([])
                matrix[-1].append(char)
        
        for char in alphabet:
            if char not in used_chars:
                used_chars.add(char)
                if len(matrix) == 0 or len(matrix[-1]) == 5:
                    matrix.append([])
                matrix[-1].append(char)
        
        return matrix

    def find_position(matrix, char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return -1, -1

    def decrypt_pair(matrix, pair):
        a, b = pair[0], pair[1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == -1 or row2 == -1:
            return None
            
        if row1 == row2:
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            return matrix[row1][col2] + matrix[row2][col1]

    def decrypt(key, ciphertext):
        matrix = generate_matrix(key)
        ciphertext = ciphertext.upper().replace(' ', '').replace('J', 'I')
        
        if len(ciphertext) % 2 != 0:
            ciphertext += 'X'
        
        pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        plaintext = ""
        
        for pair in pairs:
            decrypted_pair = decrypt_pair(matrix, pair)
            if decrypted_pair:
                plaintext += decrypted_pair
            else:
                return None
        
        return plaintext

    def calculate_frequency_score(text):
        if len(text) == 0:
            return 999999.0
        
        freq_count = {}
        total_letters = 0
        
        for char in text:
            if char in english_freq:
                freq_count[char] = freq_count.get(char, 0) + 1
                total_letters += 1
        
        if total_letters == 0:
            return 9999999999.0
        
        chi_squared = 0
        for char, expected_pct in english_freq.items():
            expected = expected_pct * total_letters / 100.0
            observed = freq_count.get(char, 0)
            if expected > 0:
                chi_squared += ((observed - expected) ** 2) / expected
        
        return chi_squared

    def generate_all_possible_keys():
        all_keys = []
        
        common_keys = [
            "PLAYFAIR", "EXAMPLE", "MONARCHY", "KEYWORD", "CIPHER",
            "SECRET", "ENCRYPT", "DECODE", "MESSAGE", "CODE",
            "BREAK", "FREQUENCY", "ATTACK", "ANALYSIS", "CRYPTO",
            "SECURITY", "ALGORITHM", "COMPUTER", "PROGRAM", "LANGUAGE",
            "PYTHON", "MATRIX", "CIPHER", "DECRYPT", "ENCODE",
            "LONDON", "ENGLAND", "AMERICA", "GERMANY", "FRANCE",
            "RUSSIA", "CHINA", "JAPAN", "CANADA", "AUSTRALIA",
            "ROME", "PARIS", "BERLIN", "MOSCOW", "TOKYO",
            "PASSWORD", "PRIVATE", "CONFIDENTIAL", "CLASSIFIED",
            "MILITARY", "GOVERNMENT", "OFFICIAL", "DOCUMENT",
            "REPORT", "INFORMATION", "INTELLIGENCE", "BATTLE",
            "VICTORY", "STRATEGY", "TACTICAL", "OPERATION",
            "COMMUNICATION", "TELEGRAM", "RADIO", "WIRELESS",
            "AGENT", "SPY", "ESPIONAGE", "COVERT", "UNDERCOVER",
            "KEY", "CODE", "WORD", "TEXT", "DATA", "FILE", "NOTE",
            "LETTER", "PAGE", "BOOK", "PAPER", "WRITE", "READ",
            "WAR", "PEACE", "ARMY", "NAVY", "AIRFORCE", "MARINE",
            "GENERAL", "COLONEL", "CAPTAIN", "LIEUTENANT", "SERGEANT",
            "SOLDIER", "OFFICER", "COMMAND", "CONTROL", "DEFENSE",
            "WEAPON", "MISSION", "TARGET", "OBJECTIVE", "POSITION",
            "ALICE", "BOB", "CHARLIE", "DAVID", "EVE", "FRANK",
            "GRACE", "HENRY", "IVAN", "JOHN", "KATE", "LINDA",
            "MICHAEL", "NANCY", "OSCAR", "PETER", "QUEEN", "ROBERT",
            "SMITH", "THOMAS", "UNION", "VICTOR", "WILLIAM", "XAVIER",
            "YVONNE", "ZACHARY", "ADAM", "BEN", "CAROL", "DANIEL",
            "UNITED", "STATES", "KINGDOM", "EUROPE", "ASIA", "AFRICA",
            "AMERICAN", "BRITISH", "FRENCH", "GERMAN", "RUSSIAN",
            "CHINESE", "JAPANESE", "ITALIAN", "SPANISH", "DUTCH",
            "LONDON", "WASHINGTON", "BERLIN", "MOSCOW", "BEIJING",
            "TOKYO", "PARIS", "ROME", "MADRID", "AMSTERDAM", "VIENNA",
            "ALGORITHM", "PROTOCOL", "SYSTEM", "NETWORK", "DATABASE",
            "SOFTWARE", "HARDWARE", "COMPUTING", "PROCESSING", "ANALYSIS",
            "CALCULATION", "COMPUTATION", "ENCRYPTION", "DECRYPTION",
            "CIPHER", "CODE", "KEY", "SECRET", "PASSWORD", "AUTHENTICATION",
            "BATTLE", "WARFARE", "STRATEGY", "TACTICS", "OPERATION",
            "MISSION", "COMMAND", "CONTROL", "INTELLIGENCE", "SECURITY",
            "DEFENSE", "OFFENSE", "ATTACK", "DEFEND", "CAPTURE",
            "RETREAT", "ADVANCE", "VICTORY", "DEFEAT", "SURRENDER",
            "PLAY", "FAIR", "MONARCH", "SECRETKEY", "MESSAGECODE",
            "BREAKCODE", "FREQUENCYANALYSIS", "CIPHERBREAK", "DECODER",
            "ENCODER", "CRYPTANALYSIS", "CRYPTOGRAPHY", "STEGANOGRAPHY",
            "QUANTUM", "COMPUTING", "ANALYTICS", "STATISTICS", "MATHEMATICS",
            "GEOMETRY", "ALGEBRA", "CALCULUS", "PROBABILITY", "STATISTICAL","SHADI","ABOOD"
        ]
        
        all_keys.extend(common_keys)
        
        letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        
        for length in range(3, 10):
            for i in range(min(100000, 26 ** length)):
                import random
                key = ''.join(random.choice(letters) for _ in range(length))
                all_keys.append(key)
        
        all_keys = list(set(all_keys))
        
        for i in range(100000):
            key = f"KEY{i:03d}"
            all_keys.append(key)
            key = f"CODE{i:03d}"
            all_keys.append(key)
            key = f"SECRET{i:03d}"
            all_keys.append(key)
        
        return all_keys

    def frequency_attack(ciphertext):
        possible_keys = generate_all_possible_keys()
        
        results = []
        
        for key in possible_keys:
            try:
                plaintext = decrypt(key, ciphertext)
                if plaintext:
                    score = calculate_frequency_score(plaintext)
                    results.append((score, plaintext, key))
            except:
                continue
        
        results.sort(key=lambda x: x[0])
        return results

    def save_all_results_to_file(results, ciphertext, filename=None):
        if filename is None:
            filename = f"playfair_results_{ciphertext}.txt"
        
        print(f"Saving {len(results)} results to {filename}")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Ciphertext: {ciphertext}\n")
            f.write(f"Total decryptions: {len(results)}\n\n")
            
            for i, (score, plaintext, key) in enumerate(results, 1):
                f.write(f"RESULT #{i}\n")
                f.write(f"Score: {score:.6f}\n")
                f.write(f"Key: {key}\n")
                f.write(f"Text: {plaintext}\n")
                
                matrix = generate_matrix(key)
                f.write("Matrix:\n")
                for row in matrix:
                    f.write("  " + " ".join(row) + "\n")
                
                f.write("-" * 60 + "\n\n")

    def get_ciphertext_from_user():
        while True:
            ciphertext = input("Enter ciphertext (A-Z only): ").strip().upper()
            
            if not ciphertext:
                print("Error: Ciphertext cannot be empty!")
                continue

            valid = True
            for char in ciphertext:
                if not ('A' <= char <= 'Z'):
                    valid = False
                    break
            
            if not valid:
                print("Error: Ciphertext must contain only A-Z!")
                continue
            
            return ciphertext

    def display_top_results(results, top_n=10):
        print(f"\nTop {top_n} results:")
        for i, (score, plaintext, key) in enumerate(results[:top_n], 1):
            print(f"{i:2d}. Score: {score:8.2f} | Key: {key:15} | Text: {plaintext[:30]}...")

    ciphertext = get_ciphertext_from_user()
    
    print(f"Analyzing: {ciphertext}")
    
    results = frequency_attack(ciphertext)
    
    if results:
        # display_top_results(results, 10)
        save_all_results_to_file(results, ciphertext)
        print(f"Complete! Found {len(results)} decryptions")
    else:
        print("No valid decryptions found!")
    

    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3' Decryption '4' World List Brute Force '5' N! Brute Force '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(15) 
    elif n==3:
        task(11)
    elif n==4:
        task(12)
    elif n==5:
        task(13)
    elif n==6:
        task(14)    
def ceaserfreq():
    ENGLISH_FREQ = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702,
    'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153,
    'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507,
    'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974,
    'Z': 0.074
    }

    def decrypt_caesar(text, shift):
        """Decrypt Caesar cipher by given shift (0..25).
        Works with uppercase letters; non-letters are left unchanged."""
        result = []
        for ch in text:
            if 'A' <= ch <= 'Z':
                offset = ord('A')
                result.append(chr((ord(ch) - offset - shift) % 26 + offset))
            else:
                result.append(ch)
        return ''.join(result)

    def letter_counts(text):
        counts = {c: 0 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        total = 0
        for ch in text:
            if 'A' <= ch <= 'Z':
                counts[ch] += 1
                total += 1
        return counts, total 
    

    def chi2_score(text):
        """Compute Chi-squared statistic between text letter freq and English expected freq.
        Lower is better (closer to English)."""
        counts, total = letter_counts(text)
        if total == 0:
            return float('inf')
        chi2 = 0.0
        for letter, exp_pct in ENGLISH_FREQ.items():
            observed = counts[letter]
            expected = total * (exp_pct / 100.0)
            chi2 += ((observed - expected) ** 2) / expected
        return chi2

    def frequency_attack(cipher):
        """Try all shifts, score with chi-squared, return sorted candidates (best first)."""
        candidates = []
        for shift in range(26):
            plain = decrypt_caesar(cipher, shift)
            score = chi2_score(plain)
            candidates.append((shift, plain, score))
        candidates.sort(key=lambda x: x[2])
        return candidates

    user_input = input("Enter ciphertext (will be converted to UPPERCASE): ").strip()
    ciphertext = user_input.upper()

    if not ciphertext:
        print("No input provided. Exiting.")
    else:
        print("\nCiphertext (converted to UPPERCASE):")
        print(ciphertext)
        print("\nFrequency attack (top 5 candidates by Chi-squared):")
        candidates = frequency_attack(ciphertext)
        for shift, plain, score in candidates[:20]:
            print(f"shift={shift:2}  score={score:8.2f}  => {plain}")

        best_shift, best_plain, best_score = candidates[0]
        print("\nBest guess (lowest Chi-squared):")
        print(f"shift={best_shift}  score={best_score:.2f}\n{best_plain}")
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3' Brute Force '4'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(5)  
    elif n==3:
        task(6)
    elif n==4:
        task(7) 
def DES_enc():
    def convtbin(message):
        if message == 0:
            return [0,0,0,0,0,0,0,0]
        l = []
        while message > 0:
            remainder = message % 2
            l.append(remainder)
            message = message // 2
        while len(l)<8:
            l.append(0)
        l.reverse()
        return l

    def convt4bin(message):
        l = []
        while message > 0:
            remainder = message % 2
            l.append(remainder)
            message = message // 2
        while len(l) < 4:
            l.append(0)
        l.reverse()  
        return l

    def convtdec(messge):
        dres=0
        x=len(messge)
        for d in range(x):
            i=messge[d]
            dres=dres+i*2**(x-(d+1))
        return dres

    def bits_to_hex(bits_list):
        hex_chars = "0123456789ABCDEF"
        hex_string = ""
        for i in range(0,len(bits_list),4):
            nibble = bits_list[i:i+4]
            value = 0
            for j in range(4):
                value = value * 2 + nibble[j]
            hex_string += hex_chars[value]
        return hex_string

    def ip(binmassege):
        prepbinmass=[]
        prep64=[]
        bitscount=0
        for i in binmassege:
            for j in i:
                bitscount+=1
                prepbinmass.append(j)
    
        current_bytes = bitscount // 8
        padding_bytes = 8 - (current_bytes % 8)
        pad_value = padding_bytes
    
        for _ in range(padding_bytes):
            pad_bits = convtbin(pad_value)
            prepbinmass.extend(pad_bits)
    
        for i in range(0,len(prepbinmass),64):
            block=prepbinmass[i:i+64]
            prep64.append(block)

        iptable=[57,49,41,33,25,17,9,1
            ,59,51,43,35,27,19,11,3
            ,61,53,45,37,29,21,13,5,
            63,55,47,39,31,23,15,7,
            56,48,40,32,24,16,8,0,
            58,50,42,34,26,18,10,2
            ,60,52,44,36,28,20,12,4
            ,62,54,46,38,30,22,14,6]
    
        ip_blocks = []
        for block in prep64:
            ipblock = []
            for pos in iptable:
                ipblock.append(block[pos])
            ip_blocks.append(ipblock)
    
        return ip_blocks

    def pc1(binkey):
        pc1Res=[]
        prepbinkey=[]
        for i in binkey:
            for j in i:
                prepbinkey.append(j)
        pc1Table=[56,48,40,32,24,16,8,0,57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,60,52,44,36,28,20,12,4,27,19,11,3]
        for i in pc1Table:
            pc1Res.append(prepbinkey[i])
        return pc1Res

    def shift_key(key_half,ronum):
        if ronum==1 or ronum==2 or ronum==9 or ronum==16:
            shift=1
        else:
            shift=2
        return key_half[shift:] + key_half[:shift]

    def generate_all_round_keys(keybits):
        pc1res = pc1(keybits)
        left = pc1res[:28]
        right = pc1res[28:]
    
        roundkeys = []
        for ronum in range(1,17):
            left = shift_key(left,ronum)
            right = shift_key(right,ronum)
            combined = left + right
            roundkey = pc2(combined)
            roundkeys.append(roundkey)
        return roundkeys

    def pc2(resofpc1):
        pc2Res=[]
        pc2Table=[13,16,10,23,0,4,2,27,14,5,20,9,22,18,11,3,25,7,15,6,26,19,12,1,40,51,30,36,46,54,29,39,50,44,32,47,43,48,38,55,33,52,45,41,49,35,28,31]
        for i in pc2Table:
            pc2Res.append(resofpc1[i])
        return pc2Res

    def F(R,pc2res):
        Etable=[31,0,1,2,3,4,3,4,5,6,7,8,7,8,9,10,11,12,11,12,13,14,15,16,15,16,17,18,19,20,19,20,21,22,23,24,23,24,25,26,27,28,27,28,29,30,31,0]
        s1=[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
        s2=[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
        s3=[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
        s4=[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
        s5=[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
        s6=[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
        s7=[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
        s8=[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
        sboxes = [s1,s2,s3,s4,s5,s6,s7,s8]
        Ptable=[15,6,19,20,28,11,27,16,0,14,22,25,4,17,30,9,1,7,23,13,31,26,2,8,18,12,29,5,21,10,3,24]
        xor1res=[]
        eRes=[]
        sBoxres=[]
        pTableres=[]
        prepforsbox=[]
        for i in Etable:
            eRes.append(R[i])
        for i in range (min(len(eRes),len(pc2res))):
            xor1res.append(eRes[i]^pc2res[i])
        for i in range (0,len(xor1res),6):
            block=xor1res[i:i+6]
            prepforsbox.append(block)
        for block_index,block in enumerate(prepforsbox):
            sbox = sboxes[block_index]  
            row = [block[0],block[5]]
            col = block[1:5]
            r = convtdec(row)
            c = convtdec(col)
            sval = sbox[r][c]    
            bits = convt4bin(sval)        
            sBoxres.extend(bits)         
        for i in Ptable:
            pTableres.append(sBoxres[i])
        return pTableres

    def round(resofip,rk):
        s = len(resofip) // 2
        left = resofip[:s]
        right = resofip[s:]
        newleft = right
        xor2res = []
        fres = F(right,rk)
        for i in range(32):
            xor2res.append(left[i] ^ fres[i])
        newright = xor2res
        roundres = newleft + newright
        return roundres

    def des_16_rounds(ip_block,round_keys):
        state = ip_block
        for i in range(16):
            state = round(state,round_keys[i])
        s = len(state) // 2
        left = state[:s]
        right = state[s:]
        state = right + left
        return state

    def inverse_ip(block):
        inv_ip_table = [39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25,32,0,40,8,48,16,56,24]
        result = []
        for pos in inv_ip_table:
            result.append(block[pos])
        return result

    plainText = input("Enter the plaintext : ")
    key = input("Enter the key (must be 8 characters): ")

    while len(key) != 8:
        print("Error: Key must be exactly 8 characters for 64-bit DES key")
        key = input("Enter the key (must be 8 characters): ")


    plainTextList = []
    keylist = []
    for i in plainText:
        massegletters = ord(i)
        plainTextList.append(convtbin(massegletters))
    for i in key:
        keyletters = ord(i)
        keylist.append(convtbin(keyletters))

    round_keys = generate_all_round_keys(keylist)
    ip_blocks = ip(plainTextList)

    final_result = []
    for block in ip_blocks:
        encrypted = des_16_rounds(block,round_keys)
        final_block = inverse_ip(encrypted)
        final_result.extend(final_block)

    hex_string = bits_to_hex(final_result)

    print("\n=== ENCRYPTION RESULTS ===")
    print(f"Hexadecimal ciphertext: {hex_string}")
    print(f"Binary length: {len(final_result)} bits")  
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(20)  
    elif n==3:
        task(21)      
def DES_dec():
    def convtbin(message):
        if message == 0:
            return [0,0,0,0,0,0,0,0]
        l = []
        while message > 0:
            remainder = message % 2
            l.append(remainder)
            message = message // 2
        while len(l)<8:
            l.append(0)
        l.reverse()
        return l

    def convt4bin(message):
        l = []
        while message > 0:
            remainder = message % 2
            l.append(remainder)
            message = message // 2
        while len(l) < 4:
            l.append(0)
        l.reverse()  
        return l

    def convtdec(messge):
        dres=0
        x=len(messge)
        for d in range(x):
            i=messge[d]
            dres=dres+i*2**(x-(d+1))
        return dres

    def hex_to_bits(hex_string):
        hex_chars = "0123456789ABCDEF"
        bits_list = []
        for char in hex_string.upper():
            value = hex_chars.index(char)
            bits = convt4bin(value)
            bits_list.extend(bits)
        return bits_list

    def pc1(binkey):
        pc1Res=[]
        prepbinkey=[]
        for i in binkey:
            for j in i:
                prepbinkey.append(j)
        pc1Table=[56,48,40,32,24,16,8,0,57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,60,52,44,36,28,20,12,4,27,19,11,3]
        for i in pc1Table:
            pc1Res.append(prepbinkey[i])
        return pc1Res

    def shift_key(key_half,ronum):
        if ronum==1 or ronum==2 or ronum==9 or ronum==16:
            shift=1
        else:
            shift=2
        return key_half[shift:] + key_half[:shift]

    def generate_all_round_keys(keybits):
        pc1res = pc1(keybits)
        left = pc1res[:28]
        right = pc1res[28:]
    
        roundkeys = []
        for ronum in range(1,17):
            left = shift_key(left,ronum)
            right = shift_key(right,ronum)
            combined = left + right
            roundkey = pc2(combined)
            roundkeys.append(roundkey)
        return roundkeys

    def pc2(resofpc1):
        pc2Res=[]
        pc2Table=[13,16,10,23,0,4,2,27,14,5,20,9,22,18,11,3,25,7,15,6,26,19,12,1,40,51,30,36,46,54,29,39,50,44,32,47,43,48,38,55,33,52,45,41,49,35,28,31]
        for i in pc2Table:
            pc2Res.append(resofpc1[i])
        return pc2Res

    def F(R,pc2res):
        Etable=[31,0,1,2,3,4,3,4,5,6,7,8,7,8,9,10,11,12,11,12,13,14,15,16,15,16,17,18,19,20,19,20,21,22,23,24,23,24,25,26,27,28,27,28,29,30,31,0]
        s1=[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
        s2=[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
        s3=[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
        s4=[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
        s5=[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
        s6=[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
        s7=[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
        s8=[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
        sboxes = [s1,s2,s3,s4,s5,s6,s7,s8]
        Ptable=[15,6,19,20,28,11,27,16,0,14,22,25,4,17,30,9,1,7,23,13,31,26,2,8,18,12,29,5,21,10,3,24]
        xor1res=[]
        eRes=[]
        sBoxres=[]
        pTableres=[]
        prepforsbox=[]
        for i in Etable:
            eRes.append(R[i])
        for i in range (min(len(eRes),len(pc2res))):
            xor1res.append(eRes[i]^pc2res[i])
        for i in range (0,len(xor1res),6):
            block=xor1res[i:i+6]
            prepforsbox.append(block)
        for block_index,block in enumerate(prepforsbox):
            sbox = sboxes[block_index]  
            row = [block[0],block[5]]
            col = block[1:5]
            r = convtdec(row)
            c = convtdec(col)
            sval = sbox[r][c]    
            bits = convt4bin(sval)        
            sBoxres.extend(bits)         
        for i in Ptable:
            pTableres.append(sBoxres[i])
        return pTableres
    def round(resofip,rk):
        s = len(resofip) // 2
        left = resofip[:s]
        right = resofip[s:]
        newleft = right
        xor2res = []
        fres = F(right,rk)
        for i in range(32):
            xor2res.append(left[i] ^ fres[i])
        newright = xor2res
        roundres = newleft + newright
        return roundres

    def des_16_rounds(ip_block,round_keys):
        state = ip_block
        for i in range(16):
            state = round(state,round_keys[i])
        s = len(state) // 2
        left = state[:s]
        right = state[s:]
        state = right + left
        return state

    def inverse_ip(block):
        inv_ip_table = [39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25,32,0,40,8,48,16,56,24]
        result = []
        for pos in inv_ip_table:
            result.append(block[pos])
        return result

    def remove_padding(bit_list):
        bytes_list = []
        for i in range(0, len(bit_list), 8):
            byte_bits = bit_list[i:i+8]
            if len(byte_bits) == 8:
                byte_value = convtdec(byte_bits)
                bytes_list.append(byte_value)
    
        if not bytes_list:
            return ""
    
        pad_length = bytes_list[-1]
    
        if pad_length < 1 or pad_length > 8:
            return bytes_list
    
        if pad_length > len(bytes_list):
            return bytes_list
    
        for i in range(pad_length):
            if bytes_list[-1-i] != pad_length:
                return bytes_list
    
        result_bytes = bytes_list[:-pad_length]
    
        result_text = ""
        for byte in result_bytes:
            if 0 <= byte <= 255:
                result_text += chr(byte)
    
        return result_text

    iptable = [57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7,56,48,40,32,24,16,8,0,58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6]

    print("=== DES DECRYPTION ===")

    ciphertext_hex = input("Enter the ciphertext (hex): ").strip()
    key = input("Enter the key (must be 8 characters): ").strip()

    while len(key) != 8:
        print("Error: Key must be exactly 8 characters for 64-bit DES key")
        key = input("Enter the key (must be 8 characters): ")

    cipher_bits = hex_to_bits(ciphertext_hex)

    if len(cipher_bits) % 64 != 0:
        print("Error: Ciphertext must be multiple of 64 bits")
        DES_dec()

    blocks = []
    for i in range(0, len(cipher_bits), 64):
        block = cipher_bits[i:i+64]
        blocks.append(block)

    keylist = []
    for i in key:
        keyletters = ord(i)
        keylist.append(convtbin(keyletters))

    round_keys = generate_all_round_keys(keylist)
    decrypt_keys = round_keys[::-1]

    decrypted_bits = []
    for block in blocks:
        block_before_ip = []
        for pos in iptable:
            block_before_ip.append(block[pos])
    
        decrypted_block = des_16_rounds(block_before_ip, decrypt_keys)
    
        decrypted_final = inverse_ip(decrypted_block)
    
        decrypted_bits.extend(decrypted_final)

    plaintext = remove_padding(decrypted_bits)

    print("\n=== DECRYPTION RESULTS ===")
    print(f"Decrypted plaintext: {plaintext}")
    print(f"Plaintext length: {len(plaintext)} characters")
    print('\n')
    print('\n')
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(21)  
    elif n==3:
        task(20) 
def AES_enc():
    S_BOX = (
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
    )

    RCON = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )



    def xtime(a):
        """Multiplies a by 2 in GF(2^8)."""
        return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

    def gmul(a, b):
        """Galois Field multiplication of a and b."""
        p = 0
        for i in range(8):
            if b & 1:
                p ^= a
            a = xtime(a)
            b >>= 1
        return p



    def sub_bytes(state):
        """Substitutes bytes using the S-Box."""
        for i in range(4):
            for j in range(4):
                state[i][j] = S_BOX[state[i][j]]

    def shift_rows(state):
        """Cyclically shifts the rows to the left."""
        state[1][0], state[1][1], state[1][2], state[1][3] = state[1][1], state[1][2], state[1][3], state[1][0]
        state[2][0], state[2][1], state[2][2], state[2][3] = state[2][2], state[2][3], state[2][0], state[2][1]
        state[3][0], state[3][1], state[3][2], state[3][3] = state[3][3], state[3][0], state[3][1], state[3][2]

    def mix_columns(state):
        """Mixes the columns of the state matrix."""
        for i in range(4):
            s0 = state[0][i]
            s1 = state[1][i]
            s2 = state[2][i]
            s3 = state[3][i]
            
            state[0][i] = gmul(s0, 2) ^ gmul(s1, 3) ^ s2 ^ s3
            state[1][i] = s0 ^ gmul(s1, 2) ^ gmul(s2, 3) ^ s3
            state[2][i] = s0 ^ s1 ^ gmul(s2, 2) ^ gmul(s3, 3)
            state[3][i] = gmul(s0, 3) ^ s1 ^ s2 ^ gmul(s3, 2)

    def add_round_key(state, round_key):
        """XORs the state with the round key."""
        for i in range(4):
            for j in range(4):
                state[i][j] ^= round_key[i][j]



    def key_expansion(key):
        """Expands the 128-bit key into 11 round keys."""
        key_symbols = [x for x in key]
        
    
        w = []
        for i in range(4):
            w.append([key_symbols[4*i], key_symbols[4*i+1], key_symbols[4*i+2], key_symbols[4*i+3]])

        for i in range(4, 44):
            temp = w[i-1][:] 
            
            if i % 4 == 0:
        
                temp = temp[1:] + temp[:1]
        
                temp = [S_BOX[x] for x in temp]
            
                temp[0] ^= RCON[i // 4]
                
            prev_w = w[i-4]
            new_w = [prev_w[j] ^ temp[j] for j in range(4)]
            w.append(new_w)


        round_keys = []
        for round_idx in range(11):
            round_matrix = [[0]*4 for _ in range(4)]
            for c in range(4): 
                word = w[round_idx * 4 + c]
                for r in range(4): 
                    round_matrix[r][c] = word[r]
            round_keys.append(round_matrix)
            
        return round_keys



    def encrypt_block(input_bytes, expanded_keys):
        """Encrypts a single 16-byte block."""
    
        state = [[0]*4 for _ in range(4)]
        for c in range(4):
            for r in range(4):
                state[r][c] = input_bytes[c*4 + r]
                

        add_round_key(state, expanded_keys[0])
        

        for round_idx in range(1, 10):
            sub_bytes(state)
            shift_rows(state)
            mix_columns(state)
            add_round_key(state, expanded_keys[round_idx])
            

        sub_bytes(state)
        shift_rows(state)
        add_round_key(state, expanded_keys[10])
        
        
        output = []
        for c in range(4):
            for r in range(4):
                output.append(state[r][c])
                
        return output



    def pad(text_bytes):
        """Applies PKCS#7 padding to ensure input is a multiple of 16 bytes."""
        padding_len = 16 - (len(text_bytes) % 16)
        padding = bytes([padding_len] * padding_len)
        return text_bytes + padding

    def encrypt_text(plain_text, key_text):

        key_bytes = key_text.encode('utf-8')
        if len(key_bytes) > 16:
            key_bytes = key_bytes[:16] 
        elif len(key_bytes) < 16:
            key_bytes = key_bytes.ljust(16, b'\0') 
        
    
        expanded_keys = key_expansion(key_bytes)
        
    
        plain_bytes = plain_text.encode('utf-8')
        padded_text = pad(plain_bytes)
        
    
        encrypted_bytes = []
        
    
        for i in range(0, len(padded_text), 16):
            block = padded_text[i : i+16]
            encrypted_block = encrypt_block(block, expanded_keys)
            encrypted_bytes.extend(encrypted_block)
            
        return bytearray(encrypted_bytes).hex()



    
        
    plain_text = input("Enter plain text: ")
    while True:
        key_input = input("Enter a key (exactly 16 chars): ")
        if len(key_input) == 16:
            break
        print("Key must be exactly 16 characters long. Please try again.")
        
    print(f"\nProcessing: '{plain_text}'")
    print(f"Key used:   '{key_input}'")
        
    cipher_hex = encrypt_text(plain_text, key_input)
        
    print("\n-------------------------------------")
    print(f"Cipher Text (Hex): {cipher_hex.upper()}")
    print("-------------------------------------")
    print("Exit '00' Main Menu '1' Run Again '2' Decryption '3'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(22)  
    elif n==3:
        task(23) 
def AES_dec():
    S_BOX = (
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
    )


    INV_S_BOX = (
        0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
        0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
        0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
        0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
        0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
        0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
        0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
        0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
        0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
        0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
        0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
        0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
        0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
        0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
        0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
    )

    RCON = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )


    def xtime(a):
        return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

    def gmul(a, b):
        p = 0
        for i in range(8):
            if b & 1:
                p ^= a
            a = xtime(a)
            b >>= 1
        return p


    def inv_sub_bytes(state):
        """Substitutes bytes using the Inverse S-Box."""
        for i in range(4):
            for j in range(4):
                state[i][j] = INV_S_BOX[state[i][j]]

    def inv_shift_rows(state):
        """Cyclically shifts the rows to the RIGHT."""
        state[1][0], state[1][1], state[1][2], state[1][3] = state[1][3], state[1][0], state[1][1], state[1][2]
        state[2][0], state[2][1], state[2][2], state[2][3] = state[2][2], state[2][3], state[2][0], state[2][1]
        state[3][0], state[3][1], state[3][2], state[3][3] = state[3][1], state[3][2], state[3][3], state[3][0]

    def inv_mix_columns(state):
        """Inverse MixColumns mixing using 0x0e, 0x0b, 0x0d, 0x09."""
        for i in range(4):
            s0 = state[0][i]
            s1 = state[1][i]
            s2 = state[2][i]
            s3 = state[3][i]
            
            state[0][i] = gmul(s0, 0x0e) ^ gmul(s1, 0x0b) ^ gmul(s2, 0x0d) ^ gmul(s3, 0x09)
            state[1][i] = gmul(s0, 0x09) ^ gmul(s1, 0x0e) ^ gmul(s2, 0x0b) ^ gmul(s3, 0x0d)
            state[2][i] = gmul(s0, 0x0d) ^ gmul(s1, 0x09) ^ gmul(s2, 0x0e) ^ gmul(s3, 0x0b)
            state[3][i] = gmul(s0, 0x0b) ^ gmul(s1, 0x0d) ^ gmul(s2, 0x09) ^ gmul(s3, 0x0e)

    def add_round_key(state, round_key):
        for i in range(4):
            for j in range(4):
                state[i][j] ^= round_key[i][j]


    def key_expansion(key):
        key_symbols = [x for x in key]
        w = []
        for i in range(4):
            w.append([key_symbols[4*i], key_symbols[4*i+1], key_symbols[4*i+2], key_symbols[4*i+3]])

        for i in range(4, 44):
            temp = w[i-1][:]
            if i % 4 == 0:
                temp = temp[1:] + temp[:1]
                temp = [S_BOX[x] for x in temp]
                temp[0] ^= RCON[i // 4]
            prev_w = w[i-4]
            new_w = [prev_w[j] ^ temp[j] for j in range(4)]
            w.append(new_w)

        round_keys = []
        for round_idx in range(11):
            round_matrix = [[0]*4 for _ in range(4)]
            for c in range(4):
                word = w[round_idx * 4 + c]
                for r in range(4):
                    round_matrix[r][c] = word[r]
            round_keys.append(round_matrix)
        return round_keys



    def decrypt_block(cipher_bytes, expanded_keys):
        """Decrypts a single 16-byte block."""
        state = [[0]*4 for _ in range(4)]
        for c in range(4):
            for r in range(4):
                state[r][c] = cipher_bytes[c*4 + r]

    
        add_round_key(state, expanded_keys[10])

        
        for round_idx in range(9, 0, -1):
            inv_shift_rows(state)
            inv_sub_bytes(state)
            add_round_key(state, expanded_keys[round_idx])
            inv_mix_columns(state)

    
        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, expanded_keys[0])

        output = []
        for c in range(4):
            for r in range(4):
                output.append(state[r][c])
        return output


    def unpad(text_bytes):
        """Removes PKCS#7 padding."""
        if not text_bytes:
            return bytes()
        padding_len = text_bytes[-1]
    
        if padding_len < 1 or padding_len > 16:
            return text_bytes
        return text_bytes[:-padding_len]

    def decrypt_text(cipher_hex, key_text):
        key_bytes = key_text.encode('utf-8')
        if len(key_bytes) > 16:
            key_bytes = key_bytes[:16]
        elif len(key_bytes) < 16:
            key_bytes = key_bytes.ljust(16, b'\0')

        expanded_keys = key_expansion(key_bytes)

        try:
            cipher_bytes = bytearray.fromhex(cipher_hex)
        except ValueError:
            return "Error: Invalid Hex string"

        if len(cipher_bytes) % 16 != 0:
            return "Error: Cipher text length must be multiple of 16"

        decrypted_bytes = []
        for i in range(0, len(cipher_bytes), 16):
            block = cipher_bytes[i : i+16]
            decrypted_block = decrypt_block(block, expanded_keys)
            decrypted_bytes.extend(decrypted_block)

        try:
            final_bytes = unpad(bytearray(decrypted_bytes))
            return final_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return "Error: Decrypted bytes could not be decoded (Wrong Key?)"

    cipher_input = input("Enter Cipher Text (Hex): ")
    key_input = input("Enter the SAME key used to encrypt: ")
        
    plain_text = decrypt_text(cipher_input, key_input)
        
    print("\n-------------------------------------")
    print(f"Recovered Plain Text: {plain_text}")
    print("-------------------------------------")
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(23)  
    elif n==3:
        task(22)
def RSA_keygen():
    def gcd(a, b):
        while b !=0:
            temp =b 
            b=a%b
            a=temp
        return a
    def is_prime(n):
        if n<2:
            return False
        if n==2:
            return True
        if n%2==0:
            return False
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                return False
        return True
    def modinv(e,phi):
        for d in range (1,phi):
            if (e*d)%phi==1:
                return d
        return None
    while True: 
        p=int(input("Enter The Value Of P : "))
        if is_prime(p):
            break
        print ("P Must Be A Prime Number")
    while True:
        q=int(input ("Enter The Value Of q : "))
        if not is_prime (q):
            print ("q Must Be A Prime Number")
        elif q==p:
            print ("q Must Not Equal p")
        else :
            break
    n=p*q
    phi=(p-1)*(q-1)

    print (f"n= {p} * {q} = {n}")
    print (f"phi(n) = ({p}-1) * ({q}-1) = {phi}")
    while True :
        e=int (input ("Enter The Value Of e :"))
        if not is_prime(e):
            print ("e Must Be A Prime Number")
        elif e<=1 or e>=phi:
            print (f"e Must Be In Range 1 < e < {phi}")
        elif gcd(e,phi)!=1:
            print (f"e Must Be Co-Prime With {phi}")
        else:
            break
    d=modinv(e,phi)
    if d is None :
        print (f"cannot calcluate d for e={e} and phi={phi}")
        return
    if (d*e)%phi !=1:
        print (f"d*e mod phi should be 1 but got {(d*e)%phi}")
        return
    print (f"\nprivate key = ({d},{n})\n")
    print (f"\npublic key = ({e},{n})\n")
    print("Exit '00' Main Menu '1' Run Again '2' Encryption '3' Decryption '4'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(24)  
    elif n==3:
        task(25)
    elif n==4:
        task(26)
def RSA_enc():
    def pow_mod (base,exp,mod):
        result=1
        base=base%mod
        while exp>0:
            if exp%2==1:
                result=(result*base)%mod
            exp=exp //2
            base=(base*base)%mod
        return result
    def str_to_des(s):
        return [ord(c) for c in s]
    def dec_to_hex(dec):
        hex_digits="0123456789ABCDEF"
        if dec==0:
            return "0"
        hex_res=""
        while dec>0:
            hex_res=hex_digits[dec%16]+hex_res
            dec=dec//16
        return hex_res
    e=int(input("Enter The Exponent : "))
    while True:
        n=int(input("Enter The Modulus : "))
        if n<=0 :
            print ("n Must Be A Positive Integer")
        else:
            break
    p=input("\nEnter The Plain Text : ")
    p_nums=str_to_des(p)
    print (f"\nPlain Text In Numbers : {p_nums}")
    valid=True
    for i,num in enumerate (p_nums):
        if num>=n:
            print (f"character '{p[i]}' with ASCII value {num} is >= n ({n})")
            valid=False
    if not valid:
        print ("Encryption failed bucase of the above error")
        return
    c_nums=[]
    for i,m in enumerate (p_nums):
        c=pow_mod(m,e,n)
        c_nums.append (c)
    print (f"\nCipher Text In Numbers : {' '.join(str(c) for c in c_nums)}")
    c_hex=[dec_to_hex(c) for c in c_nums]
    print (f"\nCipher Text In Hex : {' '.join(c_hex)}")
    print("\nExit '00' Main Menu '1' Run Again '2' Decryption '3' Key Generation '4' Trial method '5' Pollard's P-1 method '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(25)  
    elif n==3:
        task(26)
    elif n==4:
        task(24)
    elif n==5:
        task(27)
    elif n==6:
        task(28)
def RSA_dec():
    def pow_mod (base,exp,mod):
        result=1
        base=base%mod
        while exp>0:
            if exp%2==1:
                result=(result*base)%mod
            exp=exp //2
            base=(base*base)%mod
        return result 
    def hex_to_dec(hex_str):
        hex_digits="0123456789ABCDEF"
        hex_str=hex_str.upper()
        hex_res=0 
        for char in hex_str:
            hex_res=hex_res*16+hex_digits.index(char)
        return hex_res
    d=int(input("Enter The Private Exponent : "))
    while True:
        n=int(input("Enter The Modulus : "))
        if n<=0 :
            print ("n Must Be A Positive Integer")
        else:
            break
    dec_types=input("\nEnter The Type Of Cipher Text decimal/hex (d/h) : ")
    cipher_text=input("\nEnter The Cipher Text : ")
    encrypted_nums=[]
    if dec_types.lower()=='d':
        parts=cipher_text.strip().split()
        for part in parts :
            if part:
                try:
                    encrypted_nums.append(int(part))
                except:
                    print (f"Invalid decimal number: {part}")
    elif dec_types.lower()=='h':
        parts=cipher_text.strip().split()
        for part in parts :
            if part:
                try:
                    encrypted_nums.append(hex_to_dec(part))
                except:
                    print (f"Invalid hexadecimal number: {part}")
    if not encrypted_nums:
        print ("No valid encrypted numbers provided.")
        return
    print (f"\nCipher Text In Numbers : {encrypted_nums}")
    valid=True
    for i,num in enumerate (encrypted_nums):
        if num>=n:
            print (f"Encrypted number '{num}' is >= n ({n})")
            valid=False
    if not valid:
        print ("Decryption failed bucase of the above error")
        return
    decrypted_nums=[]
    for i,c in enumerate (encrypted_nums):
        m=pow_mod(c,d,n)
        decrypted_nums.append (m)
        if 32<=m<=126:
            char_display=f"'{chr(m)}'"
        else:
            char_display=f"{m}may not be displayable "
        print(f"Decrypted number {c} to {m} {char_display}")
    decrypted_text=''
    for num in decrypted_nums:
        if 0<=num<=127:
            decrypted_text+=chr(num)
        else:
            decrypted_text+='?'
    print (f"\nPlain Text : {decrypted_text}")
    print("\nExit '00' Main Menu '1' Run Again '2' Encryption '3' Key Generation '4' Trial method '5' Pollard's P-1 method '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(26)  
    elif n==3:
        task(25)
    elif n==4:
        task(24)
    elif n==5:
        task(27)
    elif n==6:
        task(28)
def RSA_trialm():
    def is_prime(n):
        if n<2:
            return False
        if n==2:
            return True
        if n%2==0:
            return False
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                return False
        return True
    def modinv(e,phi):
        for d in range (1,phi):
            if (e*d)%phi==1:
                return d
        return None
    print("Check The Value Befor Press Enter")
    n=int(input ("Enter The Value Of N : "))
    e=int(input ("Enter The Value Of e : "))
    x=int(n**0.5)
    for i in range (x,0,-1):
        if is_prime(i):
            mod=n%i
            if mod==0:
                print (n,'mode',i,'==',n%i)
                p=i
                q=int(n/i)
                print (f"p , q = {p} , {q}")
                phi=int((p-1)*(q-1))
                print (f"Ф (n) = {p-1}*{q-1} = {(p-1)*(q-1)}")
                d=modinv(e,phi)
                print(f"d value = {d}")
    print("\nExit '00' Main Menu '1' Run Again '2' Encryption '3' Decryption '4' Key Generation '5' Pollard's P-1 method '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(27)  
    elif n==3:
        task(25)
    elif n==4:
        task(26)
    elif n==5:
        task(24)
    elif n==6:
        task(28)
def RSA_pollard():
    def gcd(a, b):
        while b !=0:
            temp =b 
            b=a%b
            a=temp
        return a
    def factors(n):
        value=set()
        for a in range (2,n):
            amod=a%n
            for k in range (1,n):
                amod=(amod*a)%n
                gcdres=gcd(amod,n)
                if gcdres!=1 and amod!=n:
                    value.add(gcdres)
        return sorted(value)
    n=int(input("Enter The Value Of N : "))
    print (f"The Values is {factors(n)}")
    print("\nExit '00' Main Menu '1' Run Again '2' Encryption '3' Decryption '4' Key Generation '5' Trial method '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(28)  
    elif n==3:
        task(25)
    elif n==4:
        task(26)
    elif n==5:
        task(24)
    elif n==6:
        task(27)
def dhke_setup():
    def is_prime(n):
        if n<2:
            return False
        if n==2:
            return True
        if n%2==0:
            return False
        for i in range (3,int(n**0.5)+1,2):
            if n%i ==0:
                return False
        return True
    def is_primitive_root(alpha,p):
        seen=set()
        for i in range (1,p):
            val=pow(alpha,i,p)
            if val in seen:
                return False
            seen.add(val)
        return len(seen)==p-1
    while True:
        p=int(input("Enter Prime p : "))
        if is_prime(p):
            break
        print(f"{p} is not a prime number")
    while True:
        alpha=int(input (f"Enter The Primitive Root ALPHA (2 <= ALPHA <= {p-2}) : "))
        if alpha <2 or alpha > p-2:
            print(f"ALPHA Must Be Between 2 and {p-2}")
        elif is_primitive_root(alpha,p):
            break
        else:
            print(f"{alpha} is not a primitive root mod {p}")
    print(f"\np = {p}\nALPHA = {alpha}")
    print("\nExit '00' Main Menu '1' Run Again '2' Person A '3' Person B '4' MITM '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(29)  
    elif n==3:
        task(30)
    elif n==4:
        task(31)
    elif n==5:
        task(32)
def dhke_personA():
    def pow_mod(base,exp,mod):
        result =1
        base=base%mod
        while exp > 0:
            if exp%2 ==1:
                result=(result *base)%mod
            exp = exp // 2
            base =(base*base)%mod
        return result 
    p = int (input ("Enter Prime p : "))
    alpha =int (input ("Enter Primitive Root ALPHA : "))
    while True:
        a=int(input (f"Enter Your Private Key a (2 <= a <={p-2})"))
        if a<2 or a>p-2:
            print (f"a Must Be Between 2 And {p-2}")
        else:
            break
    A=pow_mod(alpha,a,p)
    print (f"\nPrivate Key : a = {a} \nPublic Key A = {A}")
    B=int (input ("\nEnter Person B Public Key B : "))
    shared=pow_mod(B,a,p)
    print(f"\nShared Secret : K = {shared}")
    print("\nExit '00' Main Menu '1' Run Again '2' Setp '3' Person B '4' MITM '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(30)  
    elif n==3:
        task(29)
    elif n==4:
        task(31)
    elif n==5:
        task(32)  
def dhke_personB():
    def pow_mod(base,exp,mod):
        result =1
        base=base%mod
        while exp > 0:
            if exp%2 ==1:
                result=(result *base)%mod
            exp = exp // 2
            base =(base*base)%mod
        return result 
    p=int(input("Enter Prime p : "))
    alpha=int(input("Enter Primitive Root ALPHA : "))
    while True:
        b=int(input(f"Enter Your Prinvate Key b (2<=b<={p-2}) : "))
        if b<2 or b>p-2:
            print(f"b Must Be Between 2 And {p-2}")
        else :
            break
    B=pow_mod(alpha,b,p)
    print(f"\nPrivate Key : b = {b} \nPublic Key B = {B}")
    A=int(input ("\nEnter Person A Public Key A : "))
    shared = pow_mod(A,b,p)
    print (f"\nShared Secret : K = {shared}")
    print("\nExit '00' Main Menu '1' Run Again '2' Setp '3' Person A '4' MITM '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(31)  
    elif n==3:
        task(29)
    elif n==4:
        task(30)
    elif n==5:
        task(32)
def dhke_mitm():
    def pow_mod(base,exp,mod):
        result =1
        base=base%mod 
        while exp>0:
            result =(result*base)%mod
            exp=exp//2
            base= (base*base)%mod
        return result
    p=int(input("Enter Prime p : "))
    alpha=int(input("Enter Primitive Root ALPHA : "))
    a=int(input("Enter Person A Private Key a : "))
    A=pow_mod(alpha,a,p)
    b=int(input("Enter Person B Private key b : "))
    B=pow_mod(alpha,b,p)
    x1=int(input (f"Enter Attacker's Fake Key 1 (for person B) key (2<=key<={p-2}) : "))
    x2=int(input (f"Enter Attacker's Fake Key 2 (for person A) key (2<=key<={p-2}) : "))
    y1=pow_mod(alpha,x1,p)
    y2=pow_mod(alpha,x2,p)
    k_personA=pow_mod(y2,a,p)
    k_personB=pow_mod(y1,b,p)
    k_attacker1=pow_mod(A,x2,p)
    k_attacker2=pow_mod(B,x1,p)
    print(f"\nPerson A computes : K = {k_personA}\nPerson B computes : K = {k_personB}")
    print(f"Attacker With Person A : K = {k_attacker1}\nAttacker With Person B : K = {k_attacker2}")
    if k_personA==k_attacker1 and k_personB==k_attacker2:
        print ("Attack Success") 
    print("\nExit '00' Main Menu '1' Run Again '2' Setp '3' Person A '4' Person B '5'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(32)  
    elif n==3:
        task(29)
    elif n==4:
        task(30)
    elif n==5:
        task(31)
def elgamal_keygen():
    def is_prime(n):
        if n<2:
            return False
        if n==2:
            return True 
        if n%2==0:
            return False 
        for i in range (3,int(n**0.5)+1,2):
            if n%i==0:
                return False 
        return True
    def is_primitve_root(alpha,p):
        seen = set ()
        for i in range (1,p):
            val =pow(alpha,i,p)
            if val in seen :
                return False 
            seen.add(val)
        return len(seen)==p-1
    while True:
        P=int(input("Enter Prime P > 127 To Handel Text : "))
        if is_prime(P):
            break
        print (f"{P} is not a prime number")
    while True:
        a=int(input (f"Enter Generatore a (2 <= a <= {P-2}) : "))
        if a<2 or a>P-2:
            print (f"a must be between 2 and {P-2}")
        elif is_primitve_root(a,P):
            break
        else:
            print(f"{a} is not a primitive root mod {P}") 
    while True:
        x=int(input (f"Enter Private Key x (1 < x <= {P-2}) : "))
        if x <= 1 or x>P-2:
            print (f"x must be between 1 and {P-2}")
        else:
            break
    d=pow(a,x,P)
    print (f"\nPrivate Key : x = {x}\nPuplic key : P = {P}\ta = {a}\td = {d}")
    print("\nExit '00' Main Menu '1' Run Again '2' Encryption '3' Decryption '4' BSGS '5' Chosen Ciphertext '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(33)  
    elif n==3:
        task(34)
    elif n==4:
        task(35)
    elif n==5:
        task(36)
    elif n==6:
        task(37)
def elgamal_enc():
    p=int(input("Enter Prime P : "))
    a=int(input("Enter Generator a : "))
    d=int(input ("Enter Puplic Key d : "))
    k=int (input (f"Enter Random k (1< k <= {p-2}) : "))
    message=input ("Enter Text Massage : ")
    y=pow(a,k,p)
    ciphertext=[]
    for char in message:
        m=ord(char)
        z=(pow(d,k,p)*m)%p
        ciphertext.append(z)
    print(f"ciphertext (y,z) = ({y} , {' '.join(str(z) for z in ciphertext)})")
    print("\nExit '00' Main Menu '1' Run Again '2' Key Genration '3' Decryption '4' BSGS '5' Chosen Ciphertext '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(34)  
    elif n==3:
        task(33)
    elif n==4:
        task(35)
    elif n==5:
        task(36)
    elif n==6:
        task(37)
def elgamal_dec():
    p=int(input("Enter Prime P : "))
    x=int(input ("Enter Private Key x : "))
    cipher=input("Enter The Ciphertext (y,z) space sepated : ")
    values=[]
    for value in cipher.split():
        values.append(int(value))
    y=values[0]
    z=values[1:]
    s_inv=pow(pow(y,x,p),p-2,p)
    decrypted=[]
    for char in z:
        m=(char*s_inv)%p
        if 32<=m<=126:
            decrypted.append(chr(m))
    print(f"Decrypted : {''.join(decrypted)}")
    print("\nExit '00' Main Menu '1' Run Again '2' Key Genration '3' Encryption '4' BSGS '5' Chosen Ciphertext '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(35)  
    elif n==3:
        task(33)
    elif n==4:
        task(34)
    elif n==5:
        task(36)
    elif n==6:
        task(37)
def elgamal_bsgs():
    p=int(input("Enter Prime P : "))
    a= int(input("Enter Generator a : "))
    d=int(input ("Enter Public Key d : "))
    phi=p-1
    m=int(phi**0.5)+1
    M=pow(a,m,p)
    baby={}
    for j in range(m):
        baby[pow(M,j,p)]=j
    a_inv=pow(a,p-2,p)
    giant={}
    for i in range (m):
        giant[(d*pow(a_inv,i,p))%p] = i 
    for val in baby:
        if val in giant:
            j=baby[val]
            i=giant[val]
            x=(m*j+i)%phi
            if pow (a,x,p)==d:
                print(f"Private Key Found : x = {x}")
            else:
                print("private key not found")
    print("\nExit '00' Main Menu '1' Run Again '2' Key Genration '3' Encryption '4' Dectyption '5' Chosen Ciphertext '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(36)  
    elif n==3:
        task(33)
    elif n==4:
        task(34)
    elif n==5:
        task(35)
    elif n==6:
        task(37)
def elgamal_chosencipher():
    def modinv(a,p):
        for i in range(1,p):
            if (a*i)%p==1:
                return i
        return None
    p=int(input("Enter Prime P : "))
    a=int (input ("Enter Generator a : "))
    d=int(input("Enter Public Key d : "))
    y=int (input ("Enter Y From Ciphertext : "))
    i=int(input("Enter i : "))
    while True:
        j=int(input("Enter j : "))
        if modinv(j,p-1):
            break
        else:
            print(f"j={j} has no inverse mod {p-1}")
    j_inv = modinv(j,p-1)
    y_prime=(pow(a,i,p)*pow(y,j,p))%p
    g=((-y_prime)*j_inv)%(p-1)
    x=(i*g)%(p-1)
    if pow (a,x,p)==d:
        print (f"Private Key : x = {x}")
    elif pow(a,(x+1)%(p-1),p)==d:
        print(f"Private Key : x = {(x+1)%(p-1)}")
    else:
        print("Attack Failed")
    print("\nExit '00' Main Menu '1' Run Again '2' Key Genration '3' Encryption '4' Dectyption '5' BSGS '6'")
    n=int(input())
    if n==00 or n==1:
        h(n)
    elif n==2:
        task(37)  
    elif n==3:
        task(33)
    elif n==4:
        task(34)
    elif n==5:
        task(35)
    elif n==6:
        task(36)
def h(n):
    print("\n")
    if n==00:
        exit()
    elif n==1:
        main_menu()
def task(o):
    if o == 1:
        x=str(input("Enter The Masseg to Encrypt : "))
        y=int(input('Enter The Key : '))
        z=26
        X=""
        for i in x:
            if i>="a" and i<="z":
                a=chr(ord(i)-32)
                X=X+a
            else:
                X=X+i
        caeser_enc(X,y,z)
    if o == 2 :
        x=str(input("Enter The Encrypted Masseg : "))
        y=int(input('Enter The Key : '))
        z=26
        X=""
        for i in x:
            if i>="a" and i<="z":
                a=chr(ord(i)-32)
                X=X+a
            else:
                X=X+i
        caeser_dec(X,y,z)
    if o == 3:
        x=str(input("Enter The Encrypted Masseg : "))
        z=26
        X=""
        for i in x:
            if i>="a" and i<="z":
                a=chr(ord(i)-32)
                X=X+a
            else:
                X=X+i
        caeser_analizy(X,z)
    if o == 5:
        x=str(input("Enter The Masseg to Encrypt: "))
        y=int(input('Enter The Key : '))
        z=26
        X=""
        for i in x:
            if i>="a" and i<="z":
                a=chr(ord(i)-32)
                X=X+a
            else:
                X=X+i
        multi_enc(X,y,z)
    if o == 6:
        x=str(input("Enter The Encrypted Masseg : "))
        y=int(input('Enter The Key : '))
        z=26
        X=""
        for i in x:
            if i>="a" and i<="z":
                a=chr(ord(i)-32)
                X=X+a
            else:
                X=X+i
        multi_dec(X,y,z)
    if o == 7:
        x=str(input("Enter The Encrypted Masseg : "))
        z=26
        X=""
        for i in x:
            if i>="a" and i<="z":
                a=chr(ord(i)-32)
                X=X+a
            else:
                X=X+i
        multi_analizy(X,z)
    if o == 8:
        x=str(input("Enter The Masseg to Encrypt: "))
        y=int(input('Enter The Caeser Key : '))
        z=int(input("Enter The Multiplicative Key : "))
        n=26
        X=''
        for plain in x:
            if plain>="a" and plain<="z":
                a=chr(ord(plain)-32)
                X=X+a
            else:
                X=X+plain
        affine_enc(X,y,n,z)
    if o == 9:
        x=str(input("Enter The Masseg to Decryption : "))
        y=int(input('Enter The Caeser Key : '))
        z=int(input("Enter The Multiplicative Key : "))
        n=26
        X=''
        for cipher in x:
            if cipher>="a" and cipher<="z":
                a=chr(ord(cipher)-32)
                X=X+a
            else:
                X=X+cipher
        affine_dec(X,y,n,z)
    if o == 10:
        x=str(input("Enter The Encrypted Masseg : "))
        z=26
        X=""
        for i in x:
            if i>="a" and i<="z":
                a=chr(ord(i)-32)
                X=X+a
            else:
                X=X+i
        affine_analizing(X,z)
    if o == 11:
        key = input("Enter the key: ")
        plaintext = input("Enter the plaintext: ")
        Playfair_enc(plaintext,key)
    if o== 12:
        key = input("Enter the key: ")
        ciphertext = input("Enter the ciphertext: ")
        Playfair_dec(ciphertext,key)
    if o == 13:
        ciphertext = input("Enter the ciphertext: ")
        Playfair_analizing(ciphertext)
    if o==14:
        playfair_n()
    if o==16 :
        hill_enc()
    if o==17:
        hill_dec()
    if o== 18:
        hill_analizing()
    if o==19:
        hillfreq()
    if o==15:
        plyfairfreq()
    if o==4:
        ceaserfreq()
    if o==20:
        DES_enc()
    if o==21:
        DES_dec()
    if o==22:
        AES_enc()
    if o==23:
        AES_dec()
    if o==24:
        RSA_keygen()
    if o==25:
        RSA_enc()
    if o==26:
        RSA_dec()
    if o==27:
        RSA_trialm()
    if o==28:
        RSA_pollard()
    if o==29:
        dhke_setup()
    if o==30:
        dhke_personA()
    if o==31:
        dhke_personB()
    if o ==32:
        dhke_mitm()
    if o==33:
        elgamal_keygen()
    if o==34:
        elgamal_enc()
    if o==35:
        elgamal_dec()
    if o==36:
        elgamal_bsgs()
    if o == 37:
        elgamal_chosencipher()

def main_menu():
    print(""" 
    ================= MAIN MENU =================
    1.Caeser Cipher
    2.Multiplicative Cipher
    3.Affine Cipher 
    4.Playfaier Cipher
    5.Hill Cipher
    6.DES
    7.AES
    8.RSA
    9.DHKE
    10.ELGAMAL
    =============================================
          """)
    choise=int(input("Enter Category Number (1-10) or (00) To Exit : "))
    if choise == 1:
        ceaser_menu()
    elif choise ==2:
        multi_menu()
    elif choise ==3:
        affine_menu()
    elif choise==4:
        playfair_menu()
    elif choise==5:
        hill_menu()
    elif choise==6:
        des_menu()
    elif choise==7:
        aes_menu()
    elif choise==8:
        rsa_menu()
    elif choise==9:
        dhke_menu()
    elif choise==10:
        elgamal_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        main_menu()
def ceaser_menu():
    print("""
    ================= Caeser Cipher =================
    1.Caeser Encryption
    2.Caeser Decryption
    3.Caeser Brute Force 
    4.Caeser Frequency Attack
    =================================================
              """)
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(1)
    elif choise==2:
        task(2)
    elif choise==3:
        task(3)
    elif choise ==4:
        task(4)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        ceaser_menu()
def multi_menu():
    print("""
    ================= Multiplicative Cipher =================
    1.Multiplicative Encyption
    2.Multiplicative Decryption
    3.Multiplicative Brute Force 
    =================================================
          """)
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(5)
    elif choise==2:
        task(6)
    elif choise==3:
        task(7)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        multi_menu()
def affine_menu():
    print("""
    ================= Affine Cipher =================
    1.Affine Encryption
    2.Affine Decryption
    3.Affine Brute Force 
    =============================================
          """)
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(8)
    elif choise==2:
        task(9)
    elif choise==3:
        task(10)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        affine_menu()
def playfair_menu():
    print("""
    ================= Playfaier Cipher =================
    1.Playfaier Encryption
    2.Playfaier Decryption
    3.Playfaier Brute Force (word list)
    4.Playfaier Brute Force (n!)
    5.Playfaier Frequency Attack
    ====================================================
          """)
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(11)
    elif choise==2:
        task(12)
    elif choise==3:
        task(13)
    elif choise ==4:
        task(14)
    elif choise ==5:
        task(15)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        playfair_menu()
def hill_menu():
    print("""
    ================= Hill Cipher ================= 
    16.Hill Encryption
    17.Hill Decryption
    18.Hill Burte Force
    19.Hill Frequency Attack
    =================================================
          """)
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(16)
    elif choise==2:
        task(17)
    elif choise==3:
        task(18)
    elif choise ==4:
        task(19)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        hill_menu()
def des_menu():
    print("""
    ================= DES ================= 
    1.DES Encryption
    2.DES Decryption
    =======================================""")
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(20)
    elif choise==2:
        task(21)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        des_menu()
def aes_menu():
    print("""
    ================= AES ================= 
    22.AES Encryption
    23.AES Decryption
    =======================================""")
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(22)
    elif choise==2:
        task(23)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        aes_menu()
def rsa_menu():
    print("""
    ================= RSA ================= 
    1.RSA Key Genration
    2.RSA Encryption
    3.RSA Decryption
    4.RSA Trial Method
    5.RSA Pollard's P-1 Method
    ========================================
          """)
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(24)
    elif choise==2:
        task(25)
    elif choise==3:
        task(26)
    elif choise ==4:
        task(27)
    elif choise ==5:
        task(28)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        rsa_menu()
def dhke_menu():
    print("""
    ================= DHKE ================= 
    1.DHKE Setup
    2.DHKE Person A
    3.DHKE Person B
    4.DHKE MITM
    ========================================
    """)
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(29)
    elif choise==2:
        task(30)
    elif choise==3:
        task(31)
    elif choise ==4:
        task(32)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        dhke_menu()
def elgamal_menu():
    print("""
    ================= ELGAMAL ================= 
    1.ELGAMAL Key Genration
    2.ELGAMAL Encryption
    3.ELGAMAL Decryption
    4.ELGAMAL BSGS
    5.ELGAMAL Chosen Cihertext
    ===========================================      
          """)
    choise=int(input("Enter Task Number Or '0' To EXIT  Or '99' To Main Menu :  "))
    if choise==1:
        task(33)
    elif choise==2:
        task(34)
    elif choise==3:
        task(35)
    elif choise ==4:
        task(36)
    elif choise==5:
        task(37)
    elif choise==99:
        main_menu()
    elif choise==0:
        exit()
    else:
        print ("invaled choise")
        elgamal_menu()

h(1)