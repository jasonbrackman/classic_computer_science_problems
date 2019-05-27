import base64

from PIL import Image
from ch1_encryption import encrypt, decrypt


def introspection(obj):
    for attribute in dir(obj):
        if attribute.startswith("_") is False:

            s = getattr(obj, attribute)
            t = type(s)

            print(attribute, t, s)


def load_image_as_string(path):
    with Image.open(path) as im:
        # introspection(im)

        imb = im.tobytes()

    print(im.mode, im.size)
    return im.mode, im.size, imb


if __name__ == "__main__":
    path = "example.jpg"

    mode, size, data = load_image_as_string(path)
    idata = base64.encodebytes(data)

    key, encrypted = encrypt(idata)
    data = decrypt(key, encrypted)
    data = base64.decodebytes(data)

    s = Image.frombytes(mode=mode, size=size, data=data)
    s.show()
    # print(type(im))
    # print(type(im_b.encode()))
    #
    # print("Length IM: ", len(im))
    # print("Length IM_B: ", len(im_b))
    #
    # assert im == im_b

    # with open('output.bin', 'wb') as file:
    #     file.write(encrypted.to_bytes((encrypted.bit_length() + 7) // 8, "big"))
    #
    # with open('output.bin', 'rb') as file:
    #     bytes = file.read()
    #     num = int.from_bytes(bytes, byteorder='big')
    #     # print(num.bit_length())
    #
    # new_image = decrypt(key, num)
    # with open('decrypted.jpg', 'wb') as x:
    #     x.write(new_image.encode())
    #
    # x = Image.open("decrypted.jpg")
    # x.show()
