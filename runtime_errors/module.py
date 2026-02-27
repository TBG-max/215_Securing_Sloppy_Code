


def isdigit(string):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    count = 0
    index = 0
    
    
    while index <= len(string):
        number = string[index]
        
        if number in digits:
            count += 1

    
        
        
        index += 1
        return count
        
           
        
         

        


