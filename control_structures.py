# # Control Sructures / Control Flow
# instance_running = "running"
# # If Statements
# if instance_running == "running":
#     print("The ec2 is running")
#     # code to execute if condition is True 
# elif instance_running == "stopped":
#     print("the ec2 is stopped...")
#     # code to execute if another_condition is True
# else:
#     print("the ec2 instance is in an unexpected state")
#     # code to execute if all conditions are False

public_access_block = True

# Write the if statement
# if condition
if public_access_block == True:
    print("s3 bucket is secured")
# else 
else:
    print("s3 bucket is not secure")