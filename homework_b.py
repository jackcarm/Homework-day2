users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary

twitter_handle = users["Jonathan"]["twitter"]
print(twitter_handle)

eriks_hometown = users["Erik"]["home_town"]
print(eriks_hometown)

eriks_lotto_numbers = users["Erik"]["lottery_numbers"]
print(eriks_lotto_numbers)

print(users["Avril"]["pets"])

print(min(eriks_lotto_numbers))

avrils_lotto_numbers = users["Avril"]["lottery_numbers"]

for num in avrils_lotto_numbers:
    if num % 2 == 0:
        print(num)

eriks_lotto_numbers.append(7)
print(eriks_lotto_numbers)

users["Erik"]["home_town"] = "Edinburgh"
print(users)

eriks_pets = users["Erik"]["pets"]
new_pet = {"name": "fluffy", "species": "dog"}
eriks_pets.append(new_pet)
print(eriks_pets)

new_user_me = {"Jack": {"twitter": "Jackcarm", "lottery_numbers": [18, 27, 5, 12, 45], "home_town": "Perth"}}
users.update(new_user_me)
print(users)

    






















