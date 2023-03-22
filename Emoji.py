
#Code for emoji creation

message = input("> ")
words = message.split( " ")
emojis = {
   ":)" : "😀",
   ":(" : "😞",
   "lol" : "😂",
   "sick":"😨",
   "happy": "😀",
   "mermaid": "🧜‍"
}
outcome = " "
for word in words:
   outcome += emojis.get(word, word) + " "
print(outcome)






"""
Alternatively, you could use codes to create your emojis.
"""


# grinning face

print("\U0001f600")
 
# grinning squinting face

print("\U0001F606")
 
# rolling on the floor laughing

print("\U0001F923")
