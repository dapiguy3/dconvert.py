#very simple library. just import it and you're good to go!
#from fconv.py import *
#print(ascii_to_binary("this is a test"))

def binary_to_ascii(text):
    
    if " " in text:
        
        list_of_numbers=text.split(' ')
        product=""
        
        for n in range(0,len(list_of_numbers)):
            
            character=list_of_numbers[n]
            product=product+chr(int(character,2))
            
        return(product)
    
def ascii_to_binary(text):
    
    list_of_numbers=[]
    product=""
    
    for n in range(0,len(text)):
        list_of_numbers.append(ord(text[n]))
        
    for n in range(0,len(list_of_numbers)):
        
        character=list_of_numbers[n]
        binary_number=bin(character)[2:]
        product=product+" {}".format(binary_number)
        
    product=product[1:]
    return(product)

def ascii_to_decimal(text):
    
    product=""
    for n in range(0,len(text)):
        
        product=product+" {}".format(ord(text[n]))
    product=product[1:]
    print(product)

def decimal_to_ascii(text):
    
    list_of_numbers=text.split(' ')
    product=""
    
    for n in range(0,len(list_of_numbers)):
        product=product+(chr(int(list_of_numbers[n])))
    
    return(product)

def binary_to_ascii_file(filename,newfilename):
  txt=open(str(filename),'r')
  content=txt.read()
  binary_list=content.split(" ")
  ascii_list=[]
  for n in range(0,len(binary_list)):
    ascii_list.append(int(binary_list[n],2))

  write_file=open(newfilename,'w+')
  for n in range(0,len(ascii_list)):
      write_file.write(chr(ascii_list[n]))
      
class dconvert:
    def help():
        print("""
        commands:
        ascii_to_binary(TEXT) \#converts an ascii string to a binary string
        binary_to_ascii(TEXT) \#converts a binary string to an ascii string
        ascii_to_decimal(TEXT) \#converts an ascii string to a decimal string
        decimal_to_ascii(TEXT) \#converts a decimal string to an ascii string
        dconvert.help() displays help
        """)
