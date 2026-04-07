# 🚀 Automated EC2 Backup & Lifecycle Management Using AWS Serverless Services

## 📌 Project Overview
This project automates the backup and lifecycle management of EC2 instances using AWS serverless services. It ensures that EBS volumes are backed up regularly and old snapshots are deleted automatically to optimize storage and cost.

---

## 🏗️ Architecture

**Flow:**
EC2 Instance → EBS Snapshot → Lambda → S3 → Old Snapshot Deletion

---

## ⚙️ Services Used
- Amazon EC2  
- Amazon EBS (Snapshots)  
- AWS Lambda  
- Amazon S3  
- AWS IAM  
- Amazon VPC  

---

## ✨ Features
- Automated EBS snapshot creation  
- Scheduled backup system  
- Automatic deletion of old snapshots (7 days lifecycle)  
- Fully serverless architecture  
- Cost optimization using lifecycle management  

---

## 🛠️ Step-by-Step Implementation

### 1️⃣ VPC Setup
- Created custom VPC with CIDR `10.0.0.0/16`  
- Configured:
  - 1 Public Subnet  
  - 1 Private Subnet  
- Enabled Internet Gateway  

---

### 2️⃣ EC2 Instance Setup
- Launched **Amazon Linux 2** instance  
- Instance type: `t2.micro`  
- Configured Security Group:
  - SSH (22)  
  - HTTP (80)  

---

### 3️⃣ S3 Bucket Creation
- Bucket Name: `ec2-backup-storage`  
- Enabled:
  - Versioning  
  - Server-side encryption  

---

### 4️⃣ IAM Role Configuration
- Created IAM Role for Lambda  
- Attached Policies:
  - AmazonEC2FullAccess  
  - AmazonS3FullAccess  

---

### 5️⃣ Lambda Automation
- Created Lambda function for:
  - Snapshot creation  
  - Snapshot cleanup (older than 7 days)  

---

## 🔄 Automation Workflow
- Lambda function runs periodically  
- Detects all EC2 volumes  
- Creates snapshots automatically  
- Deletes snapshots older than 7 days  

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
