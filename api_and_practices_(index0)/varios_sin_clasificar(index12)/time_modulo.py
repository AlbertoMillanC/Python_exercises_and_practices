import time 
from datetime import datetime

if __name__ == '__main__':
    while True:
        now= datetime.now()
        current_now = now.strftime(f'%Y-%m-%d %H:%M:%S:%MM' )
        
        with open('./dates.txt','a') as file:
            file.write(current_now + '\n')
            
            time.sleep(5)
            
            
        
        
    