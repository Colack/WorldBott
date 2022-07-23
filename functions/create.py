# Create a new message
def create():
    # Create a random number between 1 and 5.
    random_number = random.randint(1, 10)
    
    if random_number == 1:
        # Create a random string of numbers and letters
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 10)))
        message = random_string + " <-- My new favorite word!"
        previous = message
    elif random_number == 2:
        message = "I'm a bot created by (@colack)"
        previous = message
    elif random_number == 3:
        # Grab a random dad joke of the internet.
        url = "https://icanhazdadjoke.com/"
        responce = requests.get(url, headers={"Accept": "application/json"})
        message = responce.json()['joke']
        previous = message
    elif random_number == 4:
        message = "✌(ツ)"
        previous = message
    elif random_number == 5:
        message = "🤖"
        previous = message
    elif random_number == 6:
        message = "Don't forget, if you want to suggest a new message, contact (@colack)!"
        previous = message
    else:
        # Grab a random prompt and send it to the deep ai model.
        r = requests.post(
            "https://api.deepai.org/api/text-generator",
        data={
            'text': random.choice(prompts),
        },
            headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        )
        message = r.json()['output']
        previous = message
