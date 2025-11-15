r1 = 0
r2 = 0
r3 = 0
r4 = 0
dm = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


while True:
    a = input("cmd:")

    if a == "say":
        a = input("msg:")
        print(a)
    if a == "reg":
        a = input("row:")

        if a == "r":
            a = input("r#:")
            if a == "1":
                print(r1)
            if a == "2":
                print(r2)    
            if a == "3":
                print(r3)
            if a == "4":
                print(r4)
                
        elif a == "w":
            a = input("r#:")
            b = a
            a = int(input("int:"))
            if b == "1":
                r1 = a
            if b == "2":
                r2 = a
            if b == "3":
                r3 = a
            if b == "4":
                r4 = a
    if a == "add":
        a = input("r#:")
        if a == "1":
            c = r1 
        if a == "2":
            c = r2
        if a == "3":
            c = r3  
        if a == "4":
            c = r4
              
        a = input("r#:")
        if a == "1":
            d = r1 
        if a == "2":
            d = r2
        if a == "3":
            d = r3  
        if a == "4":
            d = r4
            
        a = input("loc:")
        if a == "1":
            r1 = c + d
        if a == "2":
            r2 = c + d
        if a == "3":
            r3 = c + d 
        if a == "4":
            r4 = c + d
    if a == "mul":
        a = input("r#:")
        if a == "1":
            c = r1 
        if a == "2":
            c = r2
        if a == "3":
            c = r3  
        if a == "4":
            c = r4
              
        a = input("r#:")
        if a == "1":
            d = r1 
        if a == "2":
            d = r2
        if a == "3":
            d = r3  
        if a == "4":
            d = r4
            
        a = input("loc:")
        if a == "1":
            r1 = c * d
        if a == "2":
            r2 = c * d
        if a == "3":
            r3 = c * d 
        if a == "4":
            r4 = c * d
    if a == "div":
        a = input("r#:")
        if a == "1":
            c = r1 
        if a == "2":
            c = r2
        if a == "3":
            c = r3  
        if a == "4":
            c = r4
              
        a = input("r#:")
        if a == "1":
            d = r1 
        if a == "2":
            d = r2
        if a == "3":
            d = r3  
        if a == "4":
            d = r4
            
        a = input("loc:")
        if a == "1":
            r1 = c / d
        if a == "2":
            r2 = c / d
        if a == "3":
            r3 = c / d 
        if a == "4":
            r4 = c / d
    if a == "sub":
        a = input("r#:")
        if a == "1":
            c = r1 
        if a == "2":
            c = r2
        if a == "3":
            c = r3  
        if a == "4":
            c = r4
              
        a = input("r#:")
        if a == "1":
            d = r1 
        if a == "2":
            d = r2
        if a == "3":
            d = r3  
        if a == "4":
            d = r4
            
        a = input("loc:")
        if a == "1":
            r1 = c - d
        if a == "2":
            r2 = c - d
        if a == "3":
            r3 = c - d 
        if a == "4":
            r4 = c - d
    if a == "dta":
        a = input("los:")
        if a == "l":
            a = input("r#:")
            b = a
            a = int(input("d#:"))
            if a <= 32:
                if b == "1":
                    dm[a] = r1
                if b == "2":
                    dm[a] = r2
                if b == "3":
                    dm[a] = r3
                if b == "4":
                    dm[a] = r4
        if a == "s":
            a = input("r#:")
            b = a
            a = int(input("d#:"))
            if a <= 32:
                if b == "1":
                    r1 = dm[a]
                if b == "2":
                    r2 = dm[a]
                if b == "3":
                    r3 = dm[a]
                if b == "4":
                    r4 = dm[a]
                
                
            
                    
            
            
            
            
            
            
            
         
     
                           
                      
                
          
          
      

    
    
    
