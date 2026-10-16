Nokia phone menu = """
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

print (main_menu)

	main_menu_prompt = input('Enter any option: ')

	match(main_menu_prompt):



def phone_book():
       
	    phonebook_menu = """
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
				print(phonebook_menu)
				phonebook_prompt = input('Enter any option: ')
				match(phonebook_prompt):
					case "0": break
					case "1": print("Search")
					case "2": print("Service Nos.")
					case "3": print("Add name")
					case "4": print("Erase")
					case "5": print("Edit")
					case "6": print("Copy")
					case "7": print("Assign tone")
					case "8": print("Send b’card")
					case "9": 

                def option():                          
						    option_menu = """
							List of Option functions
							1. Memory in use
							2. Type of view
							3. Memory status
							0. Back
						"""
						while True:
                           
							print(option_menu)
							option_prompt = input('Enter any option: ')
							match(option_prompt):
								case "0": break
								case "1": print("Memory in use")
								case "2": print("Type of view")
								case "3": print("Memory status")
                                case _ : print("Invalid Input")                                

                    case "10": print("Speed dials")
                    case "11": print("Voice tags")

def Messages():
        Messages_menu = """ 
                list_of_messages_functions      
                    1. Write messages
	                2. Inbox
	                3. Outbox
	                4. Picture messages
	                5. Templates
	                6. Smileys
	                7. Message settings
	                8. Info service
	                9. Voice mailbox number
	                10. Service command editor
	                0. Back
	                """
			                while True:
                                
				                messages_prompt = input('Enter any option: ')
				                match(messages_prompt):
					            case "0": break
					            case "1": print("Write messages")
					            case "2": print("Inbox")
					            case "3": print("Outbox")
					            case "4": print("Picture messages")
					            case "5": print("Templates")
					            case "6": print("Smileys")
					            case "7": 

                            def message_settings():						
						                    messsage_settings_menu = """
		                                    print("Message settings")
						messsage_settings_menu = """
		List of Message settings functions
		1. Set 1
		2. Common
		0. Back
		"""
						while True:
							print(messsage_settings_menu)
							messsage_settings_prompt = input('Enter any option: ')
							match(messsage_settings_prompt):
								case "0": break
								case "1": 
									print("Set 1")
									set_menu = """
			List of set functions
			1. Message centre number
			2. Messages sent as
			3. Message validity
			0. Back
			"""
									print(set_menu)
									set_prompt = input('Enter any option: ')
									
								case "2":
									print("Common")
									common_menu = """
			List of common functions
			1. Delivery reports
			2. Reply via same centre
			3. Character support
			0. Back
			"""
									print(common_menu)
									common_prompt = input('Enter any option: ')
								case _ : print("Invalid Input")
											
					case "8": print("Info service")
					case "9": print("Voice mailbox number")
					case "10": print("Service command editor")
					case _ : print("Invalid Input")
				

