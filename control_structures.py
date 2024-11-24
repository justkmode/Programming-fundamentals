# Control Sructures / Control Flow
instance_running = "running"
# If Statements
if instance_running == "running":
    print("The ec2 is running")
    # code to execute if condition is True 
elif instance_running == "stopped":
    print("the ec2 is stopped...")
    # code to execute if another_condition is True
else:
    print("the ec2 instance is in an unexpected state")
    # code to execute if all conditions are False