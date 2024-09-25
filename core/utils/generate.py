import random
import string

def random_number() -> int:
    return random.randint(0, 255)

def random_text_by_length(length: int = 1) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
