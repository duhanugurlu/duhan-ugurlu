from flask import Flask, request

home_page = 'This app alows you to get answers of a problem.'
square_problem = 'Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner. \n\nHow many such routes are there through a integer x integer grid?'

app = Flask(__name__)

@app.route('/')
def homepage():
   return home_page

@app.route('/sqr-problem')
def question():
   return square_problem

@app.route('/sqr-problem/<integer>')
def sqr_prob(integer):
   try:
      side_length = int(integer)
      total_movement = 2*side_length
      num_variations = (total_movement-1)*2
      output = 'Total number of path is' + ' ' + str(num_variations)
   except:
      output = 'Please input an integer in the form "/sqr-problem/your_integer"'    
   return output

if __name__=='__main__':
   app.run()