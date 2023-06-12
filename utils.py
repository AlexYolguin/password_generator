import random


class Password_generator():
    """
Use this class to generate password with your personal settings.
Variable settings:
alphabet: default - Eng
numbers: default - 0-9
special symbols: default - "!", "_", "#", "*", "-"
    """
    
    # DEFAULT CLASS PARAMS

    DEFAULT_ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
    DEFAULT_ALPHABET_UPPER = DEFAULT_ALPHABET_LOWER.upper()
    DEFAULT_NUMBERS = "0123456789"
    DEFAULT_SPEC_SYMBOLS = "!_#*-"

    def __init__(
            self, 
            alphabet: str=DEFAULT_ALPHABET_LOWER,
            numbers: str=DEFAULT_NUMBERS,
            spec_symbols: str=DEFAULT_SPEC_SYMBOLS
        ):

        self.alphabet_lower = "".join(set(alphabet))
        self.alphabet_upper = "".join(set(alphabet.upper()))
        self.numbers = "".join(set(numbers))
        self.spec_symbols = "".join(set(spec_symbols))
    
    def __repr__(self):
        repr_str = f"""
Class Instance params:
- alphabet: "{"".join(sorted(self.alphabet_lower))}"
- numbers: "{"".join(sorted(self.numbers))}"
- spec_symbols: "{"".join(sorted(self.spec_symbols))}"
        """

        return repr_str

    def generate(
        self,
        password_length: int=12
        ):
        """
Generate your password, variables params: password_length >= 6
        """

        if password_length < 6:
            raise NotImplementedError

        len_alphabet_upper = random.randint(1, password_length // 4)
        len_numbers = random.randint(1, password_length // 4)
        len_spec_symbols = random.randint(1, password_length // 4)
        len_alphabet_lower = password_length - (
            len_alphabet_upper + len_numbers + len_spec_symbols
        )
        
        choices_alphabet_upper = random.choices(
            self.alphabet_upper,
            k=len_alphabet_upper
        )
        choices_numbers = random.choices(
            self.numbers,
            k=len_numbers
        )
        choices_symbols = random.choices(
            self.spec_symbols,
            k=len_spec_symbols
        )
        choices_alphabet_lower = random.choices(
            self.alphabet_lower,
            k=len_alphabet_lower
        )

        password_output = list()
        password_output.extend(choices_alphabet_upper)
        password_output.extend(choices_numbers)
        password_output.extend(choices_symbols)
        password_output.extend(choices_alphabet_lower)
        
        random.shuffle(password_output)
        password = "".join(password_output)
        self.password_last = password

        return password