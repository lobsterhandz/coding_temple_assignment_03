attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
facilities = "audio system" if attendees > 50 else "projector"

# Asking for catering preferences
catering_choice = input("Do you want vegetarian food? (yes/no): ")
caterer = "Veggie Delight Caterers" if catering_choice.lower() == "yes" else "Gourmet Meals Caterers"

print("Venue:", venue)
print("Recommended facilities:", facilities)
print("Recommended caterer:", caterer)
