nokia_menu = """
List of menu functions
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Music 
9. Games
10. Calculator
11. Reminders
12. Clock
13. Profiles
14. Services
15. SIM services
16. Back"""
while True:
    print("\n===== NOKIA MENU =====")
    print("1. Phone book")
    print("2. Messages")
    print("3. Chat")
    print("4. Call register")
    print("5. Tones")
    print("6. Settings")
    print("7. Call divert")
    print("8. Music")
    print("9. Games")
    print("10. Calculator")
    print("11. Reminder")
    print("12. Clock")
    print("13. Profiles")
    print("14. Services")
    print("15. SIM services")
    print("0. Exit")

     choice = input("Please select an option: ")

    match choice:

        case "1":

                List of phonebook functions
				1. Search
				2. Service Nos.
				3. Add name
				4. Erase
				5. Edit
				6. Copy
				7. Assign tone
				8. Send b’card
				9. Options
				10. Speed dials
				11. Voice tags
				0. Back
			"""
            while True:
                print("\n--- Phone book ---")
                print("1. Search")
                print("2. Service Nos")
                print("3. Add name")
                print("4. Erase")
                print("5. Edit")
                print("6. Copy")
                print("7. Assign tone")
                print("8. Send business card")
                print("9. Options")
                print("10. Speed dials")
                print("11. Voice tags")
                print("0. Back")

                sub_choice =input("Please select an option: ")

                match sub_choice:
                    case "1":
                        print("Search.")
                    case "2":
                        print("Service Nos.")
                    case "3":
                        print("Add name.")
                    case "4":
                        print("Erase.")
                    case "5":
                        print("Edit.")
                    case "6":
                        print("Copy.")
                    case "7":
                        print("Assign tone.")
                    case "8":
                        print("Send business card.")
                    case "9":
                        print("Options.")
                    case "10":
                        print("Speed dials.")
                    case "11":
                        print("Voice tags.")
                    case "0":
                        break
                    case _:
                        print("Please select a valid option.")

        case "2":
            while True:
                print("\n--- Messages ---")
                print("1. Write messages")
                print("2. Inbox")
                print("3. Outbox")
                print("4. Picture messages")
                print("5. Templates")
                print("6. Smileys")
                print("7. Message settings")
                print("8. Info service")
                print("9. Voice mailbox number")
                print("10. Service command editor")
                print("0. Back")

                sub_choice =input("Please select an option: ")

                match sub_choice:
                    case "1":
                        print("Write messages.")
                    case "2":
                        print("Inbox.")
                    case "3":
                        print("Outbox.")
                    case "4":
                        print("Picture messages.")
                    case "5":
                        print("Templates.")
                    case "6":
                        print("Smileys.")
                    case "7":
                        print("Message settings.")
                    case "8":
                        print("Info service.")
                    case "9":
                        print("Voice mailbox number.")
                    case "10":
                        print("Service command editor.")
                    case "0":
                        break
                    case _:
                        print("Please select a valid option.")

        case "3":
            print("\n--- Chat ---")
            print("Chat selected.")

        case "4":
            while True:
                print("\n--- Call register ---")
                print("1. Missed calls")
                print("2. Received calls")
                print("3. Dialled numbers")
                print("4. Erase recent call lists")
                print("5. Show call duration")
                print("6. Show call cost")
                print("7. Call cost settings")
                print("8. Prepaid credit")
                print("0. Back")

                sub_choice =input("Please select an option: ")

                match sub_choice:
                    case "1":
                        print("Missed calls.")
                    case "2":
                        print("Received calls.")
                    case "3":
                        print("Dialled numbers.")
                    case "4":
                        print("Erase recent call lists.")
                    case "5":
                        print("Show call duration.")
                    case "6":
                        print("Show call cost.")
                    case "7":
                        print("Call cost settings.")
                    case "8":
                        print("Prepaid credit.")
                    case "0":
                        break
                    case _:
                        print("Please select a valid option.")

        case "5":
            while True:
                print("\n--- Tones ---")
                print("1. Ringing tone")
                print("2. Ringing volume")
                print("3. Incoming call alert")
                print("4. Message alert tones")
                print("5. Keypad tones")
                print("6. Warning tones")
                print("7. Vibrating alert")
                print("8. Screen saver")
                print("0. Back")

                sub_choice =input("Please select an option: ")

                match sub_choice:
                    case "1":
                        print("Ringing tone.")
                    case "2":
                        print("Ringing volume.")
                    case "3":
                        print("Incoming call alert.")
                    case "4":
                        print("Message alert tones.")
                    case "5":
                        print("Keypad tones.")
                    case "6":
                        print("Warning tones.")
                    case "7":
                        print("Vibrating alert.")
                    case "8":
                        print("Screen saver.")
                    case "0":
                        break
                    case _:
                        print("Please select a valid option.")

        case "6":
            while True:
                print("\n--- Settings ---")
                print("1. Call settings")
                print("2. Phone settings")
                print("3. Security settings")
                print("4. Restore factory settings")
                print("0. Back")

                sub_choice =input("Please select an option: ")

                match sub_choice:
                    case "1":
                        print("Call settings.")
                    case "2":
                        print("Phone settings.")
                    case "3":
                        print("Security settings.")
                    case "4":
                        print("Restore factory settings.")
                    case "0":
                        break
                    case _:
                        print("Please select a valid option.")

        case "7":
            print("\n--- Call divert ---")
            print("Call divert selected.")

        case "8":
            while True:
                print("\n--- Music ---")
                print("1. Music player")
                print("2. Radio")
                print("3. Recorder")
                print("4. Track list")
                print("0. Back")

                sub_choice =input("Please select an option: ")

                match sub_choice:
                    case "1":
                        print("Music player.")
                    case "2":
                        print("Radio.")
                    case "3":
                        print("Recorder.")
                    case "4":
                        print("Track list.")
                    case "0":
                        break
                    case _:
                        print("Please select a valid option.")

        case "9":
            print("\n--- Games ---")
            print("Games selected.")

        case "10":
            print("\n--- Calculator ---")
            print("Calculator selected.")

        case "11":
            print("\n--- Reminder ---")
            print("Reminder selected.")

        case "12":
            while True:
                print("\n--- Clock ---")
                print("1. Alarm clock")
                print("2. Clock settings")
                print("3. Date settings")
                print("4. Stopwatch")
                print("5. Countdown timer")
                print("6. Auto update of date and time")
                print("0. Back")

                sub_choice =input("Please select an option: ")

                match sub_choice:
                    case "1":
                        print("Alarm clock.")
                    case "2":
                        print("Clock settings.")
                    case "3":
                        print("Date settings.")
                    case "4":
                        print("Stopwatch.")
                    case "5":
                        print("Countdown timer.")
                    case "6":
                        print("Auto update of date and time.")
                    case "0":
                        break
                    case _:
                        print("Please select a valid option.")

        case "13":
            print("\n--- Profiles ---")
            print("Profiles selected.")

        case "14":
            print("\n--- Services ---")
            print("Services selected.")

        case "15":
            print("\n--- SIM services ---")
            print("SIM services selected.")

        case "0":
            print("\nThank you for using Nokia.")
            break

        case _:
            print("\nInvalid choice. Select a number from 0 to 15.")
