#coding
import boto3
import click
from botocore.exceptions import ClientError
from bucket import BucketManager

session = boto3.Session(profile_name='pythonAutomation')
bucket_manager = BucketManager(session)
#s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in bucket_manager.all_buckets():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an s3 bucket"
    for obj in bucket_manager.all_objects(bucket):
        print(obj)

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    "Create and Configure s3 bucket"
    bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(bucket)
    bucket_manager.configure_website(bucket_name)

    return



@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    "Sync contents of PATHNAME to BUCKET"
    bucket_manager.sync(pathname, bucket)


if __name__ == '__main__':
    cli()
