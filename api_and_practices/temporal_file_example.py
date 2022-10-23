import tempfile


if __name__== "__main__":
        temp = tempfile.TemporaryFile()  # ('w+t')
        
        try:
            temp.write(b'Hello World!.\n')
            temp.write(b'Testing...')
                      
            temp.seek(0)
            
            content = temp.read()
            
            print (content)
        finally:
            
            temp.close()