
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
  """Render the homepage."""
  return render_template('index.html')

@app.route('/about')
def about():
  """Render the about page."""
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  """Render the contact page and handle form submission."""
  if request.method == 'POST':
    # Get form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Send message to website creators (not implemented for this example)

  return render_template('contact.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
