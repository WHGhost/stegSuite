import types

def steg_encode_alterbits(cover, stream, mask):
    """
    Alter the specified bits from cover to hide stream in a lsb steganography way

    :param cover bytearray: The medium where to hide the data
    :param stream bytearray or bytes: The data to hide whithin the cover 
    :param mask function or iterable: indicates which bits should be changed, it can be:
        - A function taking as arguments the cover and the index of the byte being alterred
          (note that the preceding bytes will already have been changed), and returning the mask
        - An iterable of masks
        - A single mask to use for all bytes
        Where a mask is an integer between 0 and 255 where the bits to change are set to 1
    """

    if type(stream) not in (bytearray, bytes):
        raise TypeError("Stream should be bytes or bytearray")
    if type(cover) != bytearray:
        raise TypeError("Cover should be bytearray")

    if callable(mask):
        gen = mask
    elif type(mask) == int:
        def gen(cover, position):
            return mask
    else:
        try:
            if len(mask) < len(cover):
                raise ValueError("Mask length should be at least the length of the cover")
            else:
                def gen(cover, position):
                    return mask[position]
        except:
            raise TypeError("Invalid types for mask or cover")
    
    stream_byte_index = 0
    stream_bit_index = 0
    for byte_index, cover_byte in enumerate(cover):
        m = gen(cover, byte_index)
        for bit_index in range(8):
            bit_shift = 7 - bit_index
            if m & (1 << bit_shift) != 0:
                cover_byte &= 255 - (1 << (bit_shift)) # unset the bit bit in cover
                cover_byte |= stream[byte_index] & (1<< 7 - stream_bit_index) # set it to the stream
                if stream_bit_index >= 7:
                    stream_bit_index = 0
                    stream_byte_index += 1
                    if stream_byte_index >= len(stream):
                        cover[byte_index] = cover_byte
                        return
                else:
                    stream_bit_index += 1
        cover[byte_index] = cover_byte
    raise CoverError("Cover and masks were to small to hide the stream")


def steg_encode_lsb(cover, stream):
    #TODO tests
    """
    Calls steg_alterbits to encode the stream in the least significant bits of the cover
    
    :param cover bytearray: The medium where to hide the data
    :param stream bytearray or bytes: The data to hide in the cover
    """
    steg_encode_alterbits(cover, stream, 1)

class CoverError(Exception):

    pass
