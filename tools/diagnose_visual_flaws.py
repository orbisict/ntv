from PIL import Image
import numpy as np

# Let's inspect the crops
# We can also check CSS styles that are causing visual awkwardness on mobile:
# 1. Look at Header on mobile:
#    Is the logo too small? Is the hamburger button floating awkwardly?
# 2. Look at Hero on mobile:
#    Is the text too long or too cluttered?
#    Are there too many buttons stacked?
#    Does the countdown card look like a giant heavy block?
#    Does the audio player look weird?
# 3. Look at Overview (Section 1):
#    Are the 7 pillars stacked into 7 massive boxes taking 1500px of scrolling?
# 4. Look at Artists (Section 2):
#    Does Phuong My Chi portrait take up the entire screen with awkward text?
# 5. Look at Timeline (Section 3):
#    Are the cards too bulky?
# 6. Look at Budget (Section 5):
#    Is the table awkward or cut off?
# 7. Look at Forms & Ticket (Section 9):
#    Is the form huge? Is the ticket card clunky?
print("Ready to analyze visual flaws")
