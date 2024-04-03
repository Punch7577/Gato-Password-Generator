import base64, hashlib, random, Homoglyphs

while True:  # Allows the user to generate a new password if they want
    password = input('Type in anything random')  # Type in a random series of numbers and\or letters to create the password
    encoded = base64.b64encode(password.encode('utf-8'))

    r = base64.b64decode(encoded)  # Retrieve the Base64 encoded user input as a string of characters
    e = encoded.decode('utf-8')

    chars = list(e)  # Turn the string into a list by separating each individual character
    random.shuffle(chars)  # Shuffle the characters
    shuffled_string = ''.join(chars)  # Rejoin the characters. This process is repeated for every encryption


    def sha256_encode(data):
        sha256_hash = hashlib.sha256()

    #Update the hash object with the data to be hashed
        sha256_hash.update(data.encode('utf-8'))

    # Get the hexadecimal representation of the hashed data
        hashed_data = sha256_hash.hexdigest()

        return hashed_data

    hashed_data = sha256_encode(shuffled_string)
    hash_chars = list(hashed_data)
    random.shuffle(hash_chars)
    real_hashed_chars = ''.join(hash_chars)


    def MD5_encode(stuff):
        MD5_hash = hashlib.md5()

        MD5_hash.update(stuff.encode('utf-8'))

        hashed_stuff = MD5_hash.hexdigest()

        return hashed_stuff

    md5_encoding = MD5_encode(real_hashed_chars)
    md5_chars = list(md5_encoding)
    random.shuffle(md5_chars)
    new_hashed_chars = ''.join(md5_chars)


    def sha512_encode(stuff):
        sha512_hash = hashlib.sha512()

        sha512_hash.update(stuff.encode('utf-8'))

        hashed_stuff = sha512_hash.hexdigest()

        return hashed_stuff

    sha_encoding = sha512_encode(real_hashed_chars)
    sha_chars = list(sha_encoding)
    random.shuffle(sha_chars)
    sha_hashed_chars = ''.join(sha_chars)

    sha_chars2 = list(sha_encoding)
    random.shuffle(sha_chars2)
    sha_hashed_chars2 = ''.join(sha_chars2)

    Full_password = ''.join([sha_hashed_chars, sha_hashed_chars2] * 10)

    w = int(input(' How many characters do you want the password to have?'))
    substring = Full_password[:w]
    print(substring)
    if w > len(Full_password):
        print('The length specification exceeds the maximum length. (<= 660 is most recommended)')

# print(''.join([Homoglyphs.homoglyphs.get(letter, letter) for letter in password]))

    print(
    ' * User input:', password, '\n',
    '* User input (with homoglyphs):', '"', ''.join([Homoglyphs.homoglyphs.get(letter, letter) for letter in password]), '"', '\n',
    '* Base64 encoded password:', '"', e, '"', '\n',
    '* Shuffled Base64 encoded password:', '"', shuffled_string, '"', '\n',
    "* SHA-256 hash:", '"', hashed_data, '"', '\n',
    '* Shuffled SHA-256 hash:', '"', real_hashed_chars, '"', '\n',
    '* MD5 hash:', '"', md5_encoding, '"', '\n',
    '* Shuffled MD5 hash:', '"', new_hashed_chars, '"', '\n',
    '* Sha-512 encoding:', '"', sha_encoding, '"', '\n',
    '* Shuffled SHA-512 encoding:', '"', sha_hashed_chars, '"', '\n',
    '* The full password:', '"', ''.join([Homoglyphs.homoglyphs.get(letter, letter) for letter in Full_password]), '"', '\n',
    '* Your new Password:', '"', ''.join([Homoglyphs.homoglyphs.get(letter, letter) for letter in substring]), '"', '\n',
    '* Your new password without homoglyphs:', substring
    )  # The stuff that will be printed out

    try:
        plaintext = (''.join([Homoglyphs.homoglyphs.get(letter, letter) for letter in substring]))
        l = base64.b64encode(plaintext.encode('utf-8'))
        with open('Saved Passwords', 'w') as password_manager:
            password_to_store = base64.b64decode(l)
            password_to_store_real = l.decode('utf-8')
            password_manager.write(password_to_store_real)
    except UnicodeEncodeError:
        print('The password with the homoglyphs cannot be saved as text here.')

    rerun = input('\nDo you want to generate a new password?\n'
              'Type in "yes" to generate a new password.\n'
              'Type in "no" to exit.').lower()
    if rerun.lower() == 'no':
        break
