import blocksmith

kg = blocksmith.KeyGenerator()
kg.seed_input('Truly random string. I rolled a dice and got 4.')
key = kg.generate_key()
print(key)
