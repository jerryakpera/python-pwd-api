# Import Flask module from the flase package
from flask import Flask
# Import Api and Resource modules from flask_restful package
from flask_restful import Api, Resource, reqparse
# Import cors module from flask_cors to allow cross origin requests
from flask_cors import CORS

# Import the request arguments schema validation module to validate
# that the request body follows the required schema
# and every required field is present
from request_arguments import password_args

# Import the function to generate the password
from generate_password import generate_password

# Import the function to validate that at least 2 options have been selected
# User must select one of symbols of numbers
# User must select one of uppercase of lowercase
from validate_parameters import validate_parameters

# Create a new flask app
app = Flask(__name__)
CORS(app)
# Initialize our app as a Restful API
api = Api(app)

# Create a class that inherits from Resource
# Resource has methods that allows us to handle GET, PUT, POST and DELETE requests
class Password(Resource):
  # Define post request for this resource
  def post(self):
    # Get the arguments or send error
    args = password_args.parse_args()

    # Validate the parameters
    invalid_request = validate_parameters(args)

    # If the request is invalid then return the error as 400 status code
    if (invalid_request):
      return { "message": invalid_request }, 400

    # Call the get password function for the three passwords
    password1 = generate_password(args, args["first_input"])
    password2 = generate_password(args, args["second_input"])
    password3 = generate_password(args, args["third_input"])

    # Return the passwords
    return { "data": {
        "password1": password1,
        "password2": password2,
        "password3": password3,
      }
    }, 200

# Add the Password resource to the api
api.add_resource(Password, "/password")

# Start server and flask application
if __name__ == "__main__":
  # Run application in debug mode
  app.run(debug=True)
