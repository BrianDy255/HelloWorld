highet_bidder = {
    "David": 31,
    "Lisa": 11,
    "Bren": 98,
    "howard": 48,
}
current_value = 0
for keys, values in highet_bidder.items():
    print(keys, values)
    if current_value < values:
        current_value = values
    print(current_value)