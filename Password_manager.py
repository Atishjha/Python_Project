import base64

'''
def encrypt_pass(password):
    encoded_byte = base64.b64encode(password.encode())
    print(encoded_byte)


user_pass = input("Enter your password: ")
encrypt_pass(user_pass)
'''
def decrypt_pass(password):
    decode_byte = base64.b64decode(password)
    decode_data = decode_byte.decode()
    print(f"Decode password {decode_data}")
    pass
encode_string = input("Enter the base64 string: ")
decrypt_pass(encode_string)
