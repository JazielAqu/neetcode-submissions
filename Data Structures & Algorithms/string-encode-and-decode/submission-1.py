class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for i in strs:
            encoded_string += str(len(i)) + "#" + str(i)

        return encoded_string

    def decode(self, s: str) -> List[str]:
        # print('This is the string: ' + s)
        i = 0
        word_size = ""
        decoded_strs = []

        while i < len(s):
            if s[i] == "#":
                # print("Entered if, here is the number: " + word_size)
                length = int(word_size)
                word = ""
                for j in range(i + 1, i + length + 1):
                    # print("This is i: " + str(i) + " which is: " + s[i])
                    # print("This is how long the string is: " + str(len(s)))
                    # print("This is j: " + str(j))
                    # print("This is where j should be: " + s[j-1])
                    # print("i = " + str(i) + ", j = " + str(j) + " and represents: " + s[j])
                    word += s[j]
                # print("Word is |" + word + "|")
                decoded_strs.append(word)
                
                word_size = ""
                i += length + 1
            else:
                word_size += s[i]
                i += 1


        # print("decoded_strings: " + str(decoded_strs))
        return decoded_strs;
