import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
from Crypto.PublicKey import RSA


def rsa_decrypt(text_encrypted_base64: str , private_key: str):
    '''
    :param text_encrypted_base64:  使用公钥加密后的密文
    :param private_key:    私钥
    :return:  解密后的明文
    '''
    private_key = [private_key[64 * _: 64 * _ + 64] for _ in range(0 , len(private_key) // 64 + 1)]
    private_key = [_ for _ in private_key if _]
    private_key = '''-----BEGIN PRIVATE KEY-----\n''' + '\n'.join(private_key) + '''\n-----END PRIVATE KEY-----'''
    private_key = private_key.encode()
    # 字符串指定编码（转为bytes）
    text_encrypted_base64 = text_encrypted_base64.encode('utf-8')
    # base64解码
    text_encrypted = base64.b64decode(text_encrypted_base64)
    # 构建私钥对象
    cipher_private = PKCS1_v1_5.new(RSA.importKey(private_key))
    # 解密（bytes）
    text_decrypted = cipher_private.decrypt(text_encrypted , Random.new().read)
    # 解码为字符串
    text_decrypted = text_decrypted.decode()
    return text_decrypted


# 私钥
private_key = 'MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAIdf5z/GII3IoO5OymAHEV2c2lG+xLDBwFbkfOhkp0dJA0S0LouEP0vZtbsojKv5Cp8hBRSJWCVfk7iUUOVI0HVcLkMrfUxqevtpNu4gkUjdNhyc0ny9IoBsMhz3HqcNefdclHEXfGD6oi3M2X/MRQWWodtrgH6rCINlldEwQVPzAgMBAAECgYBgSn8ahbsyHrsZx0F7/IsFo0RHUQJnF+nP5MZUJwQ1WGHSxLc21eKP+VOixL0KtiIv/jS23tqr+sgASr8f2CMtzoYc/iZt0kAen+WlgppcJbPG1y+6puDxTZynq6I0yt5dwkBWQqxqZKoN7+4QpEVQmLFUUPycjqOZeDiJ23gzQQJBALqBt9SXIvxyWVRCKcFfxVzhNwSvSbZoUgRPUubLKQztlVP+DCQMF4gr4Eg9DQ57hwdplxUAWxSchXL/IFdPxtUCQQC50NugVkISnp3zuBC6DGWVEZDf2D0je+H4N+c75dUBoR22tL/gZpf+f1a7roBvjYrfKwP2dP5Qb1/Pbk35qaOnAkBwNTzpPSjCYvWVeNzwR3NRRvo36lHZ2XeGukaxLgd7jLDrwIuDYHcD6QndzEU/slfxwLgx3W3uv6CWKCJIBWolAkBwM1p67bsF7TtpUCrhfNzV735we+0nAQYI0RDSjUxaqIP9sBTwlmKPLSsdNxicw3YonZvN9QUfYrES2wNAjxufAkBwO1uXR3Zag6HPpEC28/6C8cN7IrkcJdh0+3jH7KyYPcVph7hT+Q5ekRXWuPsg6zjrwM1pPiseiQ2e711g6fRE'
# 密文
text_encrypted_base64 = 'HeaQM7/DoH3dAP9rJsNwECyJ0hsw6fYpwcvYE5jlY74TU58AuZR6M2Y8yyfwHwpIcTEngqX5tO54FHNuo6eNC+Q8ibHqKwaevMCRxXUBVHQeEyrmKJjRG92A1O/66B+BE4e6x8wtlQ4xuo4Nouilo3uNXVKqa6tN8cXDrC6Fky0='

text_decrypted = rsa_decrypt(text_encrypted_base64 , private_key)
print('明文：' , text_decrypted)  # lk77JARH6yU8j385
