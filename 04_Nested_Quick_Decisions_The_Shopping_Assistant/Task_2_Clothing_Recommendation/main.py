weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
additional_item = "hat" if weather == "sunny" else "boots" if weather == "rainy" else "scarf"

print("Recommended clothing:", clothing)
print("Also consider:", additional_item)
