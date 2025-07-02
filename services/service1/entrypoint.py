import sys
import hashlib


def generate_md5(inp):
  #Checking if input is empty
  if not inp:
    sys.exit("Error: No input.")

  #Generates the MD5 hash of a given string if hash_func is md5
  hash_func = inp[0].strip().lower()
  if hash_func != "md5":
    sys.exit(f"Error: First row has to be 'md5', first row is: '{hash_func}'")


  #If we wanted to allow other hash functions (other than md5)
  #if hash_func not in hashlib.algorithms_available:
  #  sys.exit(f"Unsupported algorithm: {hash_func}")
  #message = '\n'.join(inp[1:]).strip()
  #return hashlib.md5(message.encode()).hexdigest()

  #hasher = hashlib.new(hash_func)
  #hasher.update(message.encode())
  #return hasher.hexdigest()

  message = '\n' + ''.join(inp[1:]).rstrip('\n')
  
  
  # Or if we wanted to read it in chunks of 8KB
  # h = hashlib.new(md5)
  # for chunk in iter(lambda: message.buffer.read(8192), b''):
  #    h.update(chunk)
  #    h.hexdigest()

  return hashlib.md5(message.encode()).hexdigest()
  

inp = sys.stdin.readlines()
print(generate_md5(inp))