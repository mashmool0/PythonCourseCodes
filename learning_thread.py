import time
import threading
import random
lst_otps = []
# opt


def expired_otp(otp):
    time.sleep(100)
    lst_otps.remove(otp)


while True:
    username = input('enter your username ')
    # check useranmae
    # sending otp
    otp_code = random.randint(1000, 9999)
    print(otp_code)
    lst_otps.append(otp_code)

    user_otp_entry = int(
        input("please enter your otp code : (10 seconds expired)"))
    t = threading.Thread(target=expired_otp, args=(otp_code,), daemon=True)

    t.start()

    print(user_otp_entry)
    print(lst_otps)
    if user_otp_entry in lst_otps:
        print("welcome")
        break
