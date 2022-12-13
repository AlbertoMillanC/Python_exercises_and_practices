import tempfile


if __name__== "__main__":
        temp = tempfile.TemporaryFile('w+t')  # ('w+t')
        
        try:
            temp.write('Hello World!.\n')
            temp.write('Testing...')
                      
            temp.seek(0)
            
            content = temp.read()
            
            print (content)
        finally:
            
            temp.close()