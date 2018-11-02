import boto3
# import sys. No more needed since click will handle argv list 
import click 

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

# Now previos click.command will be controlled by cli which we defined above
@cli.command('list-buckets')  
def list_buckets():
    "List all s3 buckets"
# print(sys.argv) # not needed anynore 
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket') 
def list_bucket_objects(bucket):
    "List objects in an s3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
         print(obj)

if __name__=='__main__':
	cli()
