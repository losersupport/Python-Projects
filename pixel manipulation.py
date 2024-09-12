from PIL import Image 


def encrypt_image(input_image_path, output_image_path, key):
    
    img = Image.open(input_image_path)
    pixels = img.load()
    
    
    width, height = img.size
    
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]  
            
            encrypted_pixel = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
            pixels[x, y] = encrypted_pixel  
    
    
    img.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")


def decrypt_image(input_image_path, output_image_path, key):
    
    img = Image.open(input_image_path)
    pixels = img.load()
    
    
    width, height = img.size
    
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]  
            
            decrypted_pixel = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
            pixels[x, y] = decrypted_pixel  
    
    
    img.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")


def main():
    print("Image Encryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select either 'E' or 'D'.")
        return
    
    
    input_image_path = "D:\\New folder"  
    output_image_path = input("D:\\New folder\\New folder ")
    key = int(input("Enter the key (a number between 1 and 255): "))
    
    if choice == 'E':
        encrypt_image(input_image_path, output_image_path, key)
    else:
        decrypt_image(input_image_path, output_image_path, key)

# Run the program
if __name__ == "__main__":
    main()