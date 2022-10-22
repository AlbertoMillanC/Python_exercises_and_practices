import speedtest

test = speedtest ()

down_speed = test.download()
up_speed = test.upload()

print (f"Downloading speed test...{down_speed}")
print (f"Updating speed test...{ up_speed}")
