from pypsexec.client import Client
from config import user_creds

# creates an encrypted connection to the host with the username and password
hostname = "192.168.56.101"
username = "kircho"
password = "asdfpoi123"

# hostname = user_creds.get("hostname")
# username = user_creds.get("username")
# password = user_creds.get("password")

c = Client(hostname, username=username, password=password)
# c = Client(hostname)

# # set encrypt=False for Windows 7, Server 2008
# c = Client("hostname", username="username", password="password", encrypt=False)
#
# # if Kerberos is available, this will use the default credentials in the
# # credential cache
# c = Client("hostname")
#
# # you can also tell it to use a specific Kerberos principal in the cache
# # without a password
# c = Client("hostname", username="username@DOMAIN.LOCAL")

c.connect()
try:
    c.create_service()

    # After creating the service, you can run multiple exe's without
    # reconnecting

    # run a simple cmd.exe program with arguments
    stdout, stderr, rc = c.run_executable("cmd.exe",
                                          arguments="/c echo Hello World")
    print(stdout)

    stdout, stderr, rc = c.run_executable("cmd.exe",
                                          arguments="/c msg * Hi there :)")

    print(stdout)

    # # # run whoami.exe as the SYSTEM account
    # stdout, stderr, rc = c.run_executable("whoami.exe", use_system_account=True)
    # print(stdout)
    #
    # # run command asynchronously (in background), the rc is the PID of the spawned service
    # stdout, stderr, rc = c.run_executable("longrunning.exe",
    #                                       arguments="/s other args",
    #                                       asynchronous=True)
    #
    # # run whoami.exe as a specific user
    # stdout, stderr, rc = c.run_executable("whoami",
    #                                       arguments="/all",
    #                                       username="local-user",
    #                                       password="password",
    #                                       run_elevated=True)
finally:
    c.remove_service()
    c.disconnect()
