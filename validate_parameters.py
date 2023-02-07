# Function to validate the parameters
# This function requires one of numbers or symbols to be true and one of upper or lowercase to be true
def validate_parameters(args):
  # If both lowercase and uppercase are false
  if ((args["lowercase"] != True) and (args["uppercase"] != True)):
    # Return this error
    return "Either lowercase or uppercase must be selected"

  # If both numbers and symbols are false
  if ((args["numbers"] != True) and (args["symbols"]) != True):
    # Return this error
    return "Either numbers or symbols must be selected"

  return False
