from app import render_template
from app import app 

# views
@app.route('/')
def index():

    '''
    views root page function that returns the index page and its data
    '''

    return render_template('index.html')