# Dictionaries
# - Store and retrieve information
# - Key and Values

# EC2
ec2_instance = {
    "InstanceId": "i-123456abcde",
    "InstanceType": "t2.micro",
    "State": "running",
    "PublicIpAddress": "203.0.111.2"
}

instance_id = ec2_instance["InstanceId"]
print(f"this is a {instance_id} instance")

public_ip = ec2_instance.get("PublicIpAddress", "No Public IP address is here")
print(f"the instances public ip is: {public_ip}")