# Define the AWS account ID
account_id = "123456789012"

# Define the project name
project_name = "cloud_project"

# Concatenate strings to form the S3 bucket name
bucket_name = account_id + '-' + project_name + "-bucket"

# Print the resulting bucket name 
print(f"S3 Bucket Name: {bucket_name}")

# EXERCISE EC2 STRING CONCATENATION

# Environment name prod, dev, staging
environment = 'dev'

# application name
application = 'appserver'

# instance number 
instance_name = "02"

# Concatenate 
instance_name = environment + "-" + application + "-instance-" + instance_name

# Print 
print("EC2 instance name: " + instance_name)