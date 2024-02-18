attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"

# Adding additional facilities recommendation based on the number of attendees
facilities = "audio system" if attendees > 50 else "projector"
print("Venue:", venue)
print("Recommended facilities:", facilities)
