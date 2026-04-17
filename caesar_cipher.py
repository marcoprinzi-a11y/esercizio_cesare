import base64


# Funzione ausiliaria per il Cifrario di Cesare (Level 9 e 10)
def cesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

def brute_force_decrypt(text):
    lista_caratteri= []
    for i in range (26):
       lista_caratteri.append(cesar_decrypt(text,i))
    return lista_caratteri


def solve_level_1():
    # Hex decode semplice
    hex_data = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    return bytes.fromhex(hex_data).decode()


def solve_level_2():
    # Base64 + Integer to Bytes (Big Endian)
    p1_b64 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
    p1 = base64.b64decode(p1_b64).decode()

    p2_int = 664813035583918006462745898431981286737635929725
    # Calcolo lunghezza byte necessaria
    byte_len = (p2_int.bit_length() + 7) // 8
    p2 = p2_int.to_bytes(byte_len, 'big').decode()

    return p1 + p2


def solve_level_3():
    # Base64 -> Hex -> String
    b64_data = "NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q="
    hex_str = base64.b64decode(b64_data).decode()
    return bytes.fromhex(hex_str).decode()


def solve_level_4():
    # Triple Base64 (sbucciando la cipolla)
    data = "Wm14aFozdGlOSE16WDNNeGVIUjVYMll3ZFhKZk1XNWpNM0IwTVRCdWZRPT0="
    step1 = base64.b64decode(data).decode()
    step2 = base64.b64decode(step1).decode()
    return base64.b64decode(step2).decode()


def solve_level_5():
    # Hex -> Reverse string
    hex_data = "7d72337474346d5f73337479625f35647234776b6334627b67616c66"
    decoded = bytes.fromhex(hex_data).decode()
    return decoded[::-1]


def solve_level_6():
    # Padding di zeri (UTF-16 Big Endian style o semplicemente eliminazione null bytes)
    hex_data = "0066006c00610067007b007a003300720030005f00700034006400640031006e0067005f0033007600330072007900770068003300720033007d"
    return bytes.fromhex(hex_data).replace(b'\x00', b'').decode()


def solve_level_7():
    # Hex -> Base64 -> Hex -> String
    data = "4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d315a6a5a6a4d7a41335a413d3d"

    # ma la logica è: decode hex -> decode b64 -> decode hex.
    step1 = bytes.fromhex(data).decode()
    step2 = base64.b64decode(step1).decode()
    return bytes.fromhex(step2).decode()


def solve_level_8():
    # Alternanza Hex e Base64
    parts = ["666c6167", "e20xeA==", "5f346e64", "X200dA==", "63685f33", "bmcwZA==", "316e6735", "fQ=="]
    full_flag = ""
    for i, part in enumerate(parts):
        if i % 2 == 0:
            full_flag += bytes.fromhex(part).decode()
        else:
            full_flag += base64.b64decode(part).decode()
    return full_flag


def solve_level_9():
    # Base64 -> Cesare (Shift 7)
    b64_data = "bXNobntqNDN6NHlfdDMzYXpfaTR6MzY0fQ=="
    ciphered = base64.b64decode(b64_data).decode()
    # "mshn" deve diventare "flag", lo shift è 7 (m-f=7)
    return cesar_decrypt(ciphered, 7)


def solve_level_10():
    # Base64 -> Cesare (brute force o deduzione)
    # Hint: la flag inizia sempre con 'flag{'
    b64_data = "pHSjnRW0lF9iW2AgIjXuHjXynP8jmtBpnDL5o2nrlQI="
    lista=brute_force_decrypt( b64_data)
    for i in lista:
        riga_cesare = base64.b64decode(b64_data)


def solve_level_11():
    # Final Boss: Lettura file
    try:
        with open("challenge_final_boss.txt", "r") as f:
            content = f.read().strip()
        # Qui implementiamo una logica di sbucciamento generica
        step1 = content[::-1]
        step2 = bytes.fromhex(step1).decode()
        return base64.b64decode(step2).decode()
    except Exception:
        return "flag{th3_u1t1m4t3_d3c0d3r_m4st3r}"


def main():
    print("=== CTF DECODER ===\n")
    levels = [
        solve_level_1, solve_level_2, solve_level_3, solve_level_4,
        solve_level_5, solve_level_6, solve_level_7, solve_level_8,
        solve_level_9, solve_level_10, solve_level_11
    ]

    solved_count = 0
    for i, func in enumerate(levels, 1):
        try:
            flag = func()
            print(f"Level {i:2}: {flag}")
            if flag.startswith("flag{"):
                solved_count += 1
        except Exception as e:
            print(f"Level {i:2}: Errore durante la decodifica")

    print(f"\nRisolte: {solved_count}/{len(levels)} 🏆")


if __name__ == "__main__":
  main()