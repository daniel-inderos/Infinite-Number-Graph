import random
import matplotlib.pyplot as plt

# Generate 1000 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(1000)]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 16))

# Line plot
ax1.plot(range(1000), numbers, linewidth=1)
ax1.set_title('Line Plot of 1000 Random Numbers (1-100)', fontsize=16)
ax1.set_xlabel('Generation Order', fontsize=12)
ax1.set_ylabel('Random Number', fontsize=12)
ax1.set_ylim(0, 101)
ax1.grid(True, alpha=0.3)

# Histogram
ax2.hist(numbers, bins=20, range=(1, 101), edgecolor='black')
ax2.set_title('Histogram of 1000 Random Numbers (1-100)', fontsize=16)
ax2.set_xlabel('Number', fontsize=12)
ax2.set_ylabel('Frequency', fontsize=12)
ax2.grid(True, alpha=0.3)

plt.tight_layout()

# Add an explanation text
fig.text(0.5, 0.01, 
         "The line plot shows the sequence of generated numbers.\n"
         "Look for any visible patterns or trends in the line.\n"
         "The histogram shows how often each number appears.\n"
         "A truly random distribution should be roughly even across all numbers.",
         ha='center', fontsize=12, wrap=True)

# Show the plot
plt.show()

# Print some basic statistics
print(f"Lowest number generated: {min(numbers)}")
print(f"Highest number generated: {max(numbers)}")
print(f"Average of generated numbers: {sum(numbers) / len(numbers):.2f}")