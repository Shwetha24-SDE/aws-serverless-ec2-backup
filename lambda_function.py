import boto3
from datetime import datetime, timezone, timedelta
import json

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')


BUCKET_NAME = 'project-bucket-01'

def lambda_handler(event, context):
    backup_details = []
    deleted_snapshots = []

    # --- Create snapshots ---
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            for block_device in instance.get('BlockDeviceMappings', []):
                if 'Ebs' in block_device:
                    volume_id = block_device['Ebs']['VolumeId']
                    response = ec2.create_snapshot(
                        VolumeId=volume_id,
                        Description='Automated EC2 Backup'
                    )
                    backup_details.append({
                        "InstanceId": instance_id,
                        "VolumeId": volume_id,
                        "SnapshotId": response['SnapshotId'],
                        "Time": str(datetime.now(timezone.utc))
                    })

    # --- Delete snapshots older than 7 days ---
    seven_days_ago = datetime.now(timezone.utc) - timedelta(days=7)
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])

    for snapshot in snapshots['Snapshots']:
        if snapshot['StartTime'] < seven_days_ago:
            ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
            deleted_snapshots.append(snapshot['SnapshotId'])

    # --- Upload audit log to S3 ---
    log_data = {
        "backup_created": backup_details,
        "snapshots_deleted": deleted_snapshots
    }

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"backup-logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json",
        Body=json.dumps(log_data)
    )

    return {
        "status": "Backup, cleanup, and S3 logging completed"
    }
