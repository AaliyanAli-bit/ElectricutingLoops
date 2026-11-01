# Project: Power Series Generator
# Topic: Loops (for loop & exponents)

# 1Step 1: Get base number and total terms (n) from the user
base = int(input("Enter the base number: "))
terms = int(input("Enter the number of terms (n): "))

print(f"\n=== Power Series for Base {base} up to {terms} Terms ===")

# Step 2: Loop from 1 up to n terms
for i in range(1, terms + 1):
    # Calculate base raised to power i
    result = base ** i
    print(f"Term {i}: {base}^{i} = {result}")

print("=" * 40)
print("Power Series generation complete!")