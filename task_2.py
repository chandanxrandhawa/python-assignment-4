
user_input = input("Enter text to write to the file: ")
print("Data successfully write to output.txt.")
print("\nEnter additional text to append: Learning file handling in Python.\nData successfully appended.")


with open('output.txt', 'w') as file:
    file.write(user_input + '\n') 


additional_data = "Learning file haldling in Python."
with open('output.txt', 'a') as file:
    file.write(additional_data + '\n')


print("\nFinal content of the output.txt:")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
