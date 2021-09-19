# EZ PowerPoint

EZPPT runs Natural Language Processing algorithms that is able to analyze a DOCX document and return a powerpoint file with the most important points summarized into a neat powerpoint template that is ready to use with only a few tweaks from the user. 

Visit the project on [devpost](https://devpost.com/software/ez-powerpoint) to see details on our inspiration and plans.


## Local Development Instructions

1. Clone the project
2. CD to root directory
3. Run `python3 -m venv venv` to create a new virtual env
4. Run `source venv/bin/activate` to start the virtual env
5. Run `pip install -r requirements.txt` to install project dependencies
6. Run `deactivate` and `source venv/bin/activate` to restart the virtual env to load bootstrap-flask (the package has a bug)
1. Run `export FLASK_APP=flaskr` and `export FLASK_ENV=development` to set env variables
1. Run `flask run` to start the server
2. Navigate to http://127.0.0.1:5000/ to see the product!
