import io
import pickle
import boto3

# your key id
key_id = str("DO00KDBLQLMC9NQGH7K9")
# your secret key
secret_access_key = str("fOvBtHEKO0Il2zf4JV86OByktMV11cdQCPe3RYfD/Vc")

regions = ['ams3', 'nyc3', 'sgp1', 'sfo2']


def space_connect(region_name):
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name=str(region_name),
                            endpoint_url='https://' + str(region_name) + '.digitaloceanspaces.com',
                            aws_access_key_id=key_id,
                            aws_secret_access_key=secret_access_key)
    return client


# def space_connect(region_name):
#     session = boto3.Session(aws_access_key_id=key_id,
#                             aws_secret_access_key=secret_access_key,
#                             region_name=region_name)  # Replace with your space region, e.g., 'nyc3')
#
#     client = session.client('s3',
#                             region_name=str(region_name),
#                             endpoint_url='https://' + str(region_name) + '.digitaloceanspaces.com')
#     return client


def download_file(space_name, region_name, file_name):
    s3 = space_connect(region_name)
    local_path = file_name  # mistake i made so had to fix here :)
    try:
        s3.download_file(space_name, file_name, local_path)

        file_stream = io.BytesIO()
        s3.download_fileobj(space_name, file_name, file_stream)
        file_stream.seek(0)  # Reset the stream to the beginning

        # df = pd.read_csv(file_stream)

        # Load the machine learning model from the pickle file
        # model = pd.(file_stream)
        model = pickle.load(file_stream)
        return model
        # print("Data written to ->" + local_path)
    except:
        print("Error: Maybe file does not exist, or check the path you are saving to ")
        print("Usage: download file_to_download_from_the_space file_name_to_save_on_disk")
        print("Ex: download mytest-from-cloud docs.txt")
    # USAGE: download_file('space_name', 'nyc3', 'file_in_space.txt', 'file.txt')
