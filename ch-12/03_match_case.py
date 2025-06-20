def http_status(): 
   
    
    status = int(input("enter the frequency status you want to see: "))
    match status:  
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status"  

print(http_status())