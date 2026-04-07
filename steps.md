# 🚀 Automated EC2 Backup and Lifecycle Management

## 🔄 Project Workflow (Step-by-Step Implementation)

---

### 1. VPC Setup

A custom Virtual Private Cloud (VPC) was created to provide a secure and isolated environment for all AWS resources. Subnets and routing tables were configured to enable proper network communication.

![VPC Setup](images/vpc-ip.png)
![VPC Setup](images/vpc.png)

---

### 2. Security Group Configuration

Security groups were configured to control inbound and outbound traffic for the EC2 instance. Only required ports (such as SSH) were allowed to ensure secure access.

![Security Group](images/sg.png)

---

### 3. EC2 Instance Creation

An EC2 instance was launched within the VPC to act as the primary server. This instance serves as the source for backup operations.

![EC2 Instance](images/ec2.png)
![EC2 Instance](images/ec2-instance.png)


---

### 4. IAM Role Setup

An IAM role was created with appropriate permissions for EC2, S3, and CloudWatch. This enables secure interaction between AWS services, especially for Lambda execution.
 
![IAM Role](images/iam.png)
![IAM Role](images/iam-roles.png)

---

### 5. S3 Bucket Creation

An S3 bucket was created to store backup logs and metadata. It ensures high durability and easy retrieval of backup-related information.

![S3 Bucket](images/s3.png)
![S3 Bucket](images/s3-bucket.png)


---

### 6. Lambda Function Development

A Lambda function was developed to automate the backup process. It creates snapshots of EC2 volumes and stores logs in the S3 bucket.

![Lambda Function](images/lambda.png)
![Lambda Function](images/lambda-functions.png)
![Lambda Function](images/basic-settings.png)
![Lambda Function](images/lambda-code1.png)
![Lambda Function](images/lambda-code2.png)


---

### 7. Snapshot Creation (Automation)

The Lambda function automatically creates EBS snapshots of the EC2 instance at scheduled intervals, ensuring reliable and consistent backups.

![Snapshot Creation](images/snapshots.png)

---

### 8. S3 Object Storage

Snapshot details and execution logs are stored as objects in the S3 bucket. This helps in tracking backup history and maintaining records.

![S3 Object](images/s3-objects.png)


---

### 9. EventBridge Scheduling

Amazon EventBridge was configured to trigger the Lambda function at regular intervals (e.g., daily), enabling complete automation of the backup process.

![EventBridge](images/event-bridge.png)
![EventBridge](images/bridge.png)


---

### 10. Automatic Deletion (Lifecycle Management)

The Lambda function also checks the age of snapshots and automatically deletes backups older than 7 days. This helps optimize storage usage and reduce costs.

![Lambda Execution](images/lambda-code2.png)

---

### 11. CloudWatch Monitoring

CloudWatch was used to monitor Lambda execution and log activities. It assists in debugging and ensures smooth operation of the automation workflow.

![CloudWatch Logs](images/cloudwatch-log.png)

---

### 12. Log Storage in S3

All execution logs and backup details are stored in the S3 bucket, providing auditing capability and full transparency of operations.

![S3 Logs](images/bucket-log.png)

---

## ✅ Conclusion

This project demonstrates an automated EC2 backup solution using AWS services such as VPC, EC2, Lambda, EventBridge, S3, IAM, and CloudWatch.
It not only ensures regular backups but also implements lifecycle management by deleting snapshots older than 7 days, achieving efficient storage utilization and cost optimization.
