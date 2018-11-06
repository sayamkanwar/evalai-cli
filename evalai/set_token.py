import click

from evalai.utils.config import AUTH_TOKEN_DIR
@click.group(invoke_without_command=True)
def token():
    """
    Add or change your token.
    """
    """
    Invoked by `evalai token`.
    """
    input_token = input("Enter your token: ")
    AUTH_TOKEN_PATH_NEW = "%s/token.json" % AUTH_TOKEN_DIR
    f=open(AUTH_TOKEN_PATH_NEW,"w+") 
    json_token = "{\"token\":\"%s\"}" % input_token
    f.write(json_token)
    f.close()
    print("Token successfully set!")
    return input_token
