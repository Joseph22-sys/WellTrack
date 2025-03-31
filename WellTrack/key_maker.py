import secrets
import random
#make random key for our flask app
secret_key_list = [secrets.token_hex(16) for _ in range(10)]

secret_key = random.choice(secret_key_list)

