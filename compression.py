class Compressor(object):
    """Lempel-Ziv-Welch compression encoder.

    Attributes:
        dictionary (dict): map of blocks and their corresponding 12 bit codes
        text (str): text to be compressed
    """
    
    MAX_SIZE = 4096
    def __init__(self, text):
        self.dictionary = {chr(x):x for x in range(256)}
        self.text = text
        self.compressed = self.compress()
        self.shrink_factor = (1.0
                                  - (self.get_compressed_size()
                                  / self.get_uncompressed_size())) * 100
    def compress(self):
        """
        Simple implementation of the LZW algorithm
        """
        position = 0
        idx = 256
        current_block = ""
        output = []
        
        while position < (len(self.text) - 1):
            next_character = self.text[position]
            try:
                self.dictionary[current_block+next_character]
                current_block += next_character
                position += 1
            except KeyError:
                output.append(self.dictionary[current_block])
                self.dictionary[current_block+next_character] = idx
                current_block = next_character
                idx += 1
                position += 1
        output.append(self.dictionary[current_block])
        return output
    def get_compressed_size(self):
        return len(self.compressed) * 12
    def get_uncompressed_size(self):
        return len(self.text) * 8

    
    
