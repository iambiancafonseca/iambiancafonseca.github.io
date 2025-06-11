import string
import itertools

# Change to the value you got when you ran the nc command
hex_encoded = "25242e1d07400d0f080334141727030558000d1430021155161d201a0e2203181a560203142c140a" 

flag_prefix = "THM{"
flag_suffix = "}"

xored = bytes.fromhex(hex_encoded).decode()

charset = string.ascii_letters + string.digits
key_size = 5

for key_tuple in itertools.product(charset, repeat=key_size):
    key = ''.join(key_tuple)
    flag_attempt = ""

    for i in range(len(xored)):
        flag_attempt += chr(ord(xored[i]) ^ ord(key[i%len(key)]))
        # Uncomment the following lines to make the script faster, this is a bit hacky, but oh well
        #if i == 0:
            #if flag_attempt[0] != 'T':
                #break

    if flag_attempt.startswith(flag_prefix) and flag_attempt.endswith(flag_suffix):
        print("Flag:", flag_attempt)
        print("Key:", key)
        break