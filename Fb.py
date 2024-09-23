from flask import Flask, request
import requests

app = Flask(__name__)

# Replace with your Facebook Page Access Token and Page ID
ACCESS_TOKEN = 'EAAFRlNnlPO4BO2ZCFfP1zWV7YWin5QW57NFmyYZBUZANqZA67ZC9jmirHgLBj07YQzE6IlAomKUXfunQxJNKQzYk0qGZAZCeQwUhFZC7yn44zvpsRd4kWWFw6gNeToTAyU1ZBicOX9nAK7Bn1q7eDkFuAVreZARiFBQBQNJLtmVoWh1ITW2gzKK3Co9oMDZBTaLbIRmJsnLe31n8suegRgWCf4Stf8P'
PAGE_ID = '367900989750493'

@app.route('/')
def index():
    # Render the form (we can use HTML directly here or use templates)
    return '''
    <h1>Post to Facebook Page</h1>
    <form action="/post_to_fb" method="POST">
        <label for="message">Post Content:</label><br><br>
        <textarea name="message" id="message" rows="5" cols="50" required></textarea><br><br>
        <input type="submit" value="Post to Facebook">
    </form>
    '''

@app.route('/post_to_fb', methods=['POST'])
def post_to_facebook():
    # Get the message content from the form
    message = request.form['message']
    
    # Facebook Graph API URL for posting
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    
    # Data to send with the POST request
    payload = {
        'message': message,
        'access_token': ACCESS_TOKEN,
        'published' : True
    }
    
    # Make a POST request to Facebook API
    response = requests.post(url, data=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        return "Post successfully created on Facebook!"
    else:
        return f"Error: {response.json()}"

if __name__ == '__main__':
    app.run(debug=True)
