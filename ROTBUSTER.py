def decrypt_rot(text, rot):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Verificar si el carácter es una letra
            shift = 26 - rot  # Calcular el desplazamiento inverso
            if char.islower():
                # Descifrar letras minúsculas
                decrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                # Descifrar letras mayúsculas
                decrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Si no es una letra, añadir el carácter tal cual
            decrypted_text += char
    return decrypted_text

def brute_force_decrypt(text):
    print("Attempting to brute force ROT ciphers:")
    for rot in range(1, 26):  # Probar todos los desplazamientos posibles desde 1 a 25
        print(f"ROT{rot}: {decrypt_rot(text, rot)}\n")

print('''
 ____            __    ____                     __                   
/\  _`\         /\ \__/\  _`\                  /\ \__                
\ \ \L\ \    ___\ \ ,_\ \ \.\ \  __  __    ____\ \ ,_\    __   _ __  
 \ \ ,  /   / __`\ \ \/\ \  _ <'/\ \/\ \  /',__\\ \ \/  /'__`\/\`'_ \.
  \ \ \\ \  /\ \.\ \ \ \_\ \ \.\ \ \ \_\ \/\__, `\\ \ \_/\  __/\ \ \/ 
   \ \_\ \_\  \____/\ \__\\ \____/\ \____/\/\____/ \ \__\ \____\\ \_\ 
    \/_/\/ /\/___/  \/__/ \/___/  \/___/  \/___/   \/__/\/____/ \/_/ 
                                                                 By LeoL0rd19   
''')

# Entrada de usuario
input_text = input("Enter the encrypted ROT text: ")
choice = input("Do you know the ROT shift? (y/n): ")

if choice.lower() == 'y':
    rot_shift = int(input("Enter the ROT shift number (1-25): "))
    while rot_shift not in range(1, 26):
        print("Invalid ROT shift. Please enter a number between 1 and 25.")
        rot_shift = int(input("Enter the ROT shift number (1-25): "))
    print("Decrypted Text:", decrypt_rot(input_text, rot_shift))
else:
    brute_force_decrypt(input_text)

