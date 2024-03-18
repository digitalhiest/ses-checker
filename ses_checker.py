import boto3

def check_ses_credentials(access_key_id, secret_access_key):
    try:
        # Create an SES client
        ses_client = boto3.client('ses', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

        # List verified email addresses
        response = ses_client.list_verified_email_addresses()

        # Print the verified email addresses
        print("Verified Email Addresses:")
        for email in response['VerifiedEmailAddresses']:
            print("-", email)

        return True
    except Exception as e:
        print("Error:", str(e))
        return False

if __name__ == "__main__":
    # Replace these with your actual SES credentials
    access_key_id = "AKIAZ4L47OFVDCBFOCFA"
    secret_access_key = "u/oYMf9J7gvzf7hfFmkcloXkfKuAKIOsD8gWDYC8"

    # Check SES credentials
    check_ses_credentials(access_key_id, secret_access_key)
