class BitString:
    def __init__(self):
        self.bit_string = 1

    def __ior__(self, other):
        self.bit_string <<= 2  # shift left two bits
        self.bit_string |= other
        return self

    def __str__(self):
        return str(self.bit_string)

    def __rshift__(self, other):
        return self.bit_string >> other

    def __rand__(self, other):
        return self.bit_string & other

    def bit_length(self):
        return self.bit_string.bit_length()


class CompressedGene:

    def __init__(self, gene: str) -> None:
        self.bit = BitString()  # start with sentinel
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        nucleotides = {
            "A": 0b00,
            "C": 0b01,
            "G": 0b10,
            "T": 0b11,
        }

        for nucleotide in gene.upper():
            value = nucleotides.get(nucleotide, None)
            if value is not None:
                self.bit |= value
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        nucleotides = {
            0b00: "A",
            0b01: "C",
            0b10: "G",
            0b11: "T",
        }
        gene: str = ""

        for i in range(0, self.bit.bit_length() - 1, 2):  # - 1 to exclude sentinel
            bits: int = self.bit >> i & 0b11  # get just 2 relevant bits
            value = nucleotides.get(bits, None)
            if value is not None:
                gene += value
            else:
                raise ValueError("Invalid bits:{}".format(bits))

        return gene[::-1]  # [::-1] reverses string by slicing backward

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100

    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)

    # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit.bit_string)))
    print(compressed)

    # decompress
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))