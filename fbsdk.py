import facebook

# Your Page Access Token
ACCESS_TOKEN = 'EAAFRlNnlPO4BO2ZCFfP1zWV7YWin5QW57NFmyYZBUZANqZA67ZC9jmirHgLBj07YQzE6IlAomKUXfunQxJNKQzYk0qGZAZCeQwUhFZC7yn44zvpsRd4kWWFw6gNeToTAyU1ZBicOX9nAK7Bn1q7eDkFuAVreZARiFBQBQNJLtmVoWh1ITW2gzKK3Co9oMDZBTaLbIRmJsnLe31n8suegRgWCf4Stf8P'

# Initialize the Graph API client
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN)

# Message to be posted
message = "Hello, this is a post made using the Facebook SDK for Python!"

# Make the post
post = graph.put_object(parent_object='me', connection_name='feed', message=message)

# Check if the post was successful
print(f"Post ID: {post['id']}")
