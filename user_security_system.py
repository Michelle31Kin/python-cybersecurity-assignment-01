print("=" * 100)
print("                                          CYBERGUARD v1.0")
print("                                PERSONAL SECURITY MONITORING SYSTEM")
print("=" * 100)
print()
print("                                     Welcome, Security Analyst!")
print()
print("                                     Your mission is to monitor")
print("                        account information and identify potential threats.")
print()
print("                                  Starting security assessment....")
print()

username = str(input("    What is your username?  "))
email_address = str(input("    What is your email address?  "))
password = str(input("    Enter your password:  "))
age = str(input("    What is your age?  "))
ip_address = str(input("    What is the ip address of this device?  "))
print()

failedLogin_attempts = int(input("    How many failed login attempts have been detected?  "))
if failedLogin_attempts == 0:
    print("    No login attempts detected.")

elif failedLogin_attempts >= 5:
    print("    Critical: possibly a brute-force attack")

else:
    print("    Low security alert")
print()

account_status = (str(input("    What is the current status of your account?  Active ot Inactive?  ")))
if account_status == "Active" and failedLogin_attempts < 5:
    print("    Your account is active. No critical login detected.")
    print("    Thank you!!!")
else:
    print("    Your account is inactive. Please contact your system administrator for assistance.")
print()

if len(password) < 8:
    print("    Your password is weak. Please change your password to a stronger one.")
elif len(password) >= 8:
    print("    Your password is moderate.")
else:
    print("    Your password is strong.")
print()


print("=" * 100)
print("                                          USER INFORMATION")
print("=" * 100)
print()
print("    username:          ", username)
print("    email address:     ", email_address)
print("    age:               ", age)
print("    ip address:        ", ip_address)
print("    account status:    ", account_status)
print()

print("=" * 100)
print("                                         SECURITY ANALYSIS")
print("=" * 100)
print()
print("    failed login attempts: ", failedLogin_attempts)
print("    password strength:     ", len(password))
print()

print("=" * 100)
print("                                          THREAT DETECTION")
print("=" * 100)
print()
print("    ", failedLogin_attempts, "failed login attempts detected.")
print()

print("=" * 100)
print("                                        END SECURITY REPORT")
print("=" * 100)