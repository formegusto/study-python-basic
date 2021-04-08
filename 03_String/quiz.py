url = "http://daum.net"

password = url.replace("http://", "")
password = password[:password.index(".")]
print(password)

password = password[0:3] + str(len(password)) + str(password.count("e")) + "!"
print(password)
