#3. Generate 10 Random Numbers (-15 to 15) and Square Them 
import random 
random_numbers = random.sample(range(-15, 16), 10) 
 
squared_numbers = [x ** 2 for x in random_numbers] 
 
print("Original List:", random_numbers) 
print("Squared List:", squared_numbers) 
