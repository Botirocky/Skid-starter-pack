
import time

password = input("Enter Password: ")
start = time.time()
chars = "abcdefghijklmnopqrstuvwxyz"
guess = []
for val in range(5):
    a = [i for i in chars]
    for y in range(val):
        a = [x + i for i in chars for x in a]
    guess = guess + a
    if password in guess:
        break
end = time.time()
clock = str(end - start)

print("Your password: " + password)
print("Time taken: " + clock)

print("Number of guesses: " + str(len(guess)))
print("Guessed password: " + guess[guess.index(password)])
print("Position in guesses: " + str(guess.index(password) + 1))
print("All guesses: " + str(guess))
print("Length of guessed password: " + str(len(guess[guess.index(password)])))
print("Length of password: " + str(len(password)))
print("Characters used: " + chars)
print("Total possible combinations: " + str(len(chars) ** len(password)))
print("Average time per guess: " + str((end - start) / len(guess)))
print("Estimated time to brute-force all combinations: " + str((end - start) / len(guess) * (len(chars) ** len(password))))
print("Estimated time to brute-force all combinations (hours): " + str(((end - start) / len(guess) * (len(chars) ** len(password))) / 3600))
print("Estimated time to brute-force all combinations (days): " + str((((end - start) / len(guess) * (len(chars) ** len(password))) / 3600) / 24))
print("Estimated time to brute-force all combinations (years): " + str(((((end - start) / len(guess) * (len(chars) ** len(password))) / 3600) / 24) / 365))
print("--------------------------------------------------")
print("Note: This is a simple brute-force algorithm and may not be efficient for longer passwords.")
print("--------------------------------------------------")
print("Characters in password: " + ', '.join(set(password)))
print("Unique characters in password: " + str(len(set(password))))
print("Password strength (approx.): " + str(len(chars) ** len(password) / len
(guess)))
print("--------------------------------------------------")
print("End of detailed report.")