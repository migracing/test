import time

print("Hello world!")
print("Logging test...")
print("This will appear in Docker logs.")

# Keep alive so you can see output in logs
while True:
    print("Still alive...")
    time.sleep(5)
