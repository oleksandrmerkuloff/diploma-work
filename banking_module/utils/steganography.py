from PIL import Image


def encode_lsb(img_path, output_path, data):
    img = Image.open(img_path).convert('RGB')

    # Convert message to binary + unique delimiter
    binary_data = ''.join(format(ord(char), '08b') for char in data) + '1111111111111110'
    data_len = len(binary_data)

    pixels = list(img.getdata())
    new_pixels = []
    data_index = 0

    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):
            if data_index < data_len:
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_data[data_index])
                data_index += 1
        new_pixels.append(tuple(new_pixel))

    img.putdata(new_pixels)
    img.save(output_path, 'JPEG')
    print(f"Data encoded and saved to {output_path}")


def decode_lsb(img_path):
    img = Image.open(img_path).convert('RGB')
    pixels = list(img.getdata())

    binary_data = ''
    for pixel in pixels:
        for i in range(3):
            binary_data += str(pixel[i] & 1)

    # Search for delimiter directly
    delimiter = '1111111111111110'
    end_index = binary_data.find(delimiter)

    if end_index != -1:
        # Decode up to the delimiter
        binary_message = binary_data[:end_index]
        all_bytes = [binary_message[i:i + 8] for i in range(0, len(binary_message), 8)]
        decoded_data = ''.join([chr(int(byte, 2)) for byte in all_bytes])
        return decoded_data
    else:
        return "Delimiter not found or corrupted data."


if __name__ == '__main__':
    # encode_lsb('pyt.jpg', 'secret-pyt.jpg', 'Oleksandr Merkulov')
    print(decode_lsb('secret-pyt.jpg'))
