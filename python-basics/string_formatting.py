# Alvin Njuguna
# 2/11/2026
# String formatting

# Get string length
sentence = "I watch anime"

string_length = len(sentence)

print(f"The length is: {string_length}")

# Spliting a string
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is: ", split[1])


# Make everything CAPS
mpesa_code = "UB21ddsfhg"

capitalized = mpesa_code.upper()

print("New mpesa code: ", capitalized)

# Make to lower
made_lower = mpesa_code.lower()

print("New mpesa code: ", made_lower)

# Replacing characters in a string

balance = "100Kes"
amount_added = "50Kes"

cleaned_balance = balance.replace("Kes", "")

print("Cleaned balance: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes", "")

print("Cleaned amount added: ", cleaned_amount_added)

# Daudis answer
new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print("The new balance is:", new_balance)
# Money balance
message = "CONFIRMED you have received 40kes from Phillip"
print(message)
split_message = message.split(" ")

print("The amount received is: ", split_message[4])
cleaned_amount_received = split_message[4].replace("kes", "")
print("Cleaned amount received: ", cleaned_amount_received)
balance= "200kes"
cleaned_balance = balance.replace("kes", "")
print("Cleaned balance: ", cleaned_balance)
new_balance = int(cleaned_balance) + int(cleaned_amount_received)
print("The new balance is: ", new_balance)