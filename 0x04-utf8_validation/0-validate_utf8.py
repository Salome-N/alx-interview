#!/usr/bin/python3
''' UTF-8 Validation '''


def validUTF8(data):
    '''
    Determines if a given data set represents a valid UTF-8 encoding
    '''
    num_bytes = 0
    m1 = 1 << 7
    m2 = 1 << 6

    for i in data:
        m_byte = 1 << 7
        if num_bytes == 0:
            while m_byte & i:
                num_bytes += 1
                m_byte = m_byte >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (i & m1 and not (i & m2)):
                return False
        num_bytes -= 1
    if num_bytes == 0:
        return True
    return False
