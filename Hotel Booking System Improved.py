print("Welcome To The Booking Management System!")

print("We Have A Few Rooms Available, They Are:")
print("")
print("Luxury Suite. Detials About This Room: Booking Time: 8:00am\nTwo King Beds With A Lovely View Of The Ocean And A PRIVATE Beach To Have Fun And Surf! Also Features A Hot Tub and A Movie Room To Watch Your Favorite Shows!\nCost: $25,000 Per Night")
print("")
print("Master Suite. Details About This Room: Booking Time: 4:00pm\nKing Bed With A Lovely View Of The Ocean.\nCost: $7,500 Per Night")
print("")
print("Mini Suite. Details About This Room: Booking Time: 12:00pm\nQueen Bed With A View Of A Mountainside.\nCost: $6,500 Per Night")
print("")
print("Double Regular. Details About This Room: Booking Time: 6:00am\nTwo Twin Beds And Has A Hot Tub.\nCost: $4,500 Per Night")
print("")
print("Regular. Details About This Room: Booking Time: 2:00pm\nOne Queen Bed But No Other Upgrades.\nCost: $2,500 Per Night")
print("")
print("Messy Room. Details About This Room: Booking Time: 12:00am\nOne Ripped, Broken And Dirty Pull - Out Sofa.\nCost: $800 Per Night")
print("")

C = int(input("Please Enter Your Choice Of Room.\nEnter 1 For The Luxury Suite\nEnter 2 For The Master Suite\nEnter 3 For The Mini Suite\nEnter 4 For The Double Regular\nEnter 5 For The Regular\nEnter 6 For The Messy Room "))

if(C == 1):
    print("You Have Selected The Luxury Suite! You Will Be Paying $25,000 Per Night.")
    print("Have A Great Day And We'll See You Soon!\nThank You For Using The Booking Management System!")

elif(C == 2):
    print("You Have Selected The Master Suite! You Will Be Paying $7,500 Per Night.")
    print("Have A Great Day And We'll See You Soon!\nThank You For Using The Booking Management System!")

elif(C == 3):
    print("You Have Selected The Mini Suite! You Will Be Paying $6,500 Per Night.")
    print("Have A Great Day And We'll See You Soon!\nThank You For Using The Booking Management System!")
    
elif(C == 4):
    print("You Have Selected The Double Regular! You Will Be Paying $4,500 Per Night.")
    print("Have A Great Day And We'll See You Soon!\nThank You For Using The Booking Management System!")
    
elif(C == 5):
    print("You Have Selected The Regular! You Will Be Paying $2,500 Per Night.")
    print("Have A Great Day And We'll See You Soon!\nThank You For Using The Booking Management System!")
    
elif(C == 6):
    print("You Have Selected The Messy Room! You Will Be Paying $800 Per Night.")
    print("Have A Great Day And We'll See You Soon!\nThank You For Using The Booking Management System!")

else:
    print("ERROR ERROR ERROR ERROR ERROR.That Was Not One Of The Options, Please Refresh.ERROR ERROR ERROR ERROR ERROR")
