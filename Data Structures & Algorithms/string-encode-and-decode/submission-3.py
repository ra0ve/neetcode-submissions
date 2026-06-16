class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        encoded_string = ""
        for word in strs:
            number_letters = str(len(word))
            encoded_string += number_letters + "#" + word
        # print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            # Find the next delimiter starting from current position
            j = s.find('#', i)
            length = int(s[i:j])
            
            # Use the length to slice the exact word
            word = s[j + 1 : j + 1 + length]
            decoded_string.append(word)
            
            # Move pointer to the start of the next length prefix
            i = j + 1 + length
            
        return decoded_string