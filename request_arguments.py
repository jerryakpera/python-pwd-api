from flask_restful import reqparse

# REQUIRED FIELDS SETTINGS
# These defines the fields that the request body must have to be valid.
# The type of value is validated at this point, not the value itself so
# a requried field of type String can be empty and be considered valid
required_fields = {
    "numbers": True,
    "symbols": True,
    "uppercase": True,
    "lowercase": True,
    "first_input": True,
    "second_input": True,
    "third_input": True,
}

# Makes sure the required information is passed with request
# Parse through the request and ensure it contains the following arguments
# Return the text in the help field if the argument is not in the request body
password_args = reqparse.RequestParser()

# The numbers is a required field with an boolean type.
password_args.add_argument("numbers", type=bool, help="Numbers field must be true or false.", required=required_fields["numbers"])
# The symbols is a required field with an boolean type.
password_args.add_argument("symbols", type=bool, help="Symbols field must be true or false.", required=required_fields["symbols"])
# The uppercase is a required field with an boolean type.
password_args.add_argument("uppercase", type=bool, help="Uppercase field must be true or false.", required=required_fields["uppercase"])
# The lowercase is a required field with an boolean type.
password_args.add_argument("lowercase", type=bool, help="Lowercase field must be true or false.", required=required_fields["lowercase"])

# The first input is a required field with an boolean type.
password_args.add_argument("first_input", type=str, help="First input field required.", required=required_fields["first_input"])
# The second input input is a required field with an boolean type.
password_args.add_argument("second_input", type=str, help="Second input field required.", required=required_fields["second_input"])
# The third input input is a required field with an boolean type.
password_args.add_argument("third_input", type=str, help="Third input field required.", required=required_fields["third_input"])
