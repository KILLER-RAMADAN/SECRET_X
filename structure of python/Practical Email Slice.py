# ---------------------------
# -- Practical Slice Email --
# ---------------------------

theName = input('What\'s Your Name ?').strip().lower()
theEmail = input('What\'s Your Email ?').strip().lower()

theUsername = theEmail[0:5]
thedomain = theEmail[6:]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} \n Your Website Is {thedomain}")

# email = "Osama@elzero.org"
# print(email[:email.index("@")])