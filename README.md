# Serverless_Architecture
# AWS Lambda Automation Assignments

## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

### Objective
The goal of this assignment was to automate the stopping and starting of EC2 instances based on tags using AWS Lambda and Boto3. Specifically, instances with the tag `Auto-Start` are started, and instances with the tag `Auto-Stop` are stopped.

### Steps to Complete this Assignment
1. **Creating a Lambda Function:**
   - Navigated to the Lambda page and named the function `AutoStartStopLambda`.
   - Used an existing IAM role (`prashant-s3-lambda-role`) that had permissions to access EC2 and manage instances.
   - Set a timeout of 10 seconds to prevent the function from failing due to long execution times.

2. **Creating EC2 Instances:**
   - Created two EC2 instances, each with custom tags.
   - First instance tag: `Key: Action`, `Value: Auto-Stop`.
   - Second instance tag: `Key: Action`, `Value: Auto-Start`.
   - Launched both instances.

3. **Writing the Lambda Function Code:**
   - Developed a Python-based Lambda function using Boto3 to describe EC2 instances, check their tags, and either stop or start the instances.
     
4. **Testing:**
   - Manually tested the function by invoking it through the Lambda console.
   - Verified instance status changes on the EC2 dashboard.
   - Checked the CloudWatch logs for further validation.
![image](https://github.com/user-attachments/assets/8be18eac-6820-4b0b-8725-8cf3b269e41c)

---

## Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

### Objective
The goal of this assignment was to automate the deletion of files older than 30 days from a specific S3 bucket using AWS Lambda and Boto3.

### Steps Implemented
1. **Creating a Lambda Function:**
   - Navigated to the Lambda page and named the function `S3OldData`.
   - Used an existing IAM role (`prashant-s3-lambda-role`) which had permissions to access S3 and manage storage.

2. **Writing the Lambda Function Code:**
   - Developed a Python-based Lambda function using Boto3 to list objects in an S3 bucket and delete those older than 30 days.

3. **Testing:**
   - Manually invoked the Lambda function and verified that the files were deleted successfully.

![image](https://github.com/user-attachments/assets/459cb5f2-6915-4de6-9980-9d0cbad8bbbf)


---

## Assignment 4: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3

### Objective
To automate the backup process for your EBS volumes and ensure that backups older than a specified retention period are cleaned up to save costs.

### Steps Implemented
1. **Creating a Lambda Function:**
   - Navigated to the Lambda page and named the function `EBSSnapshot`.
   - Used an existing IAM role (`Lambda_Test`) with permissions to access and manage .

2. **Writing the Lambda Function Code:**{Attached the file ebssnapshot.py}
   -  A Python-based Lambda function using Boto3 to check EBS volumes and ensure that backups older than a specified retention period are cleaned up. 

3. **Testing:**
   - Manually tested the function by checking CloudWatch logs and Console if Snapshot created and deleted the older snapshots. Attached a reference screenshot for validation.
![image](https://github.com/user-attachments/assets/821df086-b8d7-4c6a-ab56-ddb28062bff6)

---

## Assignment 8: Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend

### Objective
Automatically analyze and categorize the sentiment of user reviews using Amazon Comprehend.

### Steps Implemented
1. **Creating a Lambda Function:**
   - Navigated to the Lambda page and named the function `SentimentAnalysisFunction`.
   - Used an existing IAM role (`Lambda_Test`) with permissions to access and  manage Comprehend.

2. **Writing the Lambda Function Code:** {Attached the file comprehend.py}
   -A Python-based Lambda function using Boto3 to extract the user review from an event and use Amazon Comprehend to analyze the sentiment of the review and Log the sentiment result.

   -Set the test with below JSON
   {
    "review": "I absolutely love this product! It works great and is exactly what I needed."
   }

3. **Testing:**
   -Click Test to trigger the function.
   -Check the Logs to verify the sentiment result (should print "POSITIVE").

![image](https://github.com/user-attachments/assets/26627e4d-df73-4008-932e-c096cd94b7d1)

