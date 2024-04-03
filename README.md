# Gato-Password-Generator
## Generate long, complex, secure passwords for yourself.

The Gato Password Generator is a software I coded exclusively in Python that generates long, complex, secure passwords for you. It is free, easy to use, and has no setup process. You just download it and use it right away!

## 🐱 This software could be used for the following things:

1. Generating secure passwords for websites and applications.
2. That is pretty much it.

## 🌟 How to use the Gato Password Generator:

1. Type in anything random (it can have anything. Letters, numbers, symbols, anything on your keyboard in general).
2. Type in the number of characters you want your new password to have.
3. Done! It should show a wall of text with random passwords with your new password, both with and without homoglyphs at the bottom of the text.

## 💡 How does the software work?

1. The software works by getting the user input and then putting it through a series of hashing and encoding algorithms. The hashing and encoding algorithms would end up turning the seemingly simple user input, and then turns it into a series of random numbers and letters.
2. After the user input is done going through all of the hashing and encoding algorithms, the length of the final product is multiplied by 10, making it extremely long.
3. Every number, letter, and symbol in the result is replaced with a homoglyph (an ASCII and/or Unicode lookalike character) which makes it more secure, and takes longer to crack.
4. Then, it is shortened after the user inputs their second input, which determines how long the password will be.
5. The final product of the software is a wall of text that shows different passwords, each one at different steps of the encoding and hashing process.
6. The generated password is then encoded in Base64 and decoded onto a text file, which gives one more additional password if the user wants to use it (this is an additional feature for the user. It is not a necessary step in the generation of the password. It is just something that I added for fun!)

A more specific explanation of the password generation process:

1. User input.
2. Characters in user input get replaced with homoglypths.
3. Encodes in Base64.
4. Shuffles the Base64 encoded string.
5. Encodes the shuffled Base64 encoded string in SHA-256.
6. Shuffles the SHA-256 encoded string.
7. Creates an MD5 hash of the SHA-256 encoded string.
8. Shuffles the MD5 hash.
9. Encodes the shuffled MD5 hash in SHA-512.
10. Creates two separate SHA-512 encoded strings and then joins them together into one string.
11. Replaces every character in the combined SHA-512 encoded string with a homoglypth, and then multiplies the length by 10.
12. Generates two new passwords, one without homoglyphs and one with homoglyphs.
13. After all the steps are finished, the user is given the option of generating a new password if they are not satisfied with the result, in which the process repeats.

## ✍ Last Few things:

If you like this software, then you can give me a star. Or don't.

Thank you for checking out my Password Generator!
