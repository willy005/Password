import pyperclip
from user_credentials import User, Credential

	# Function to create a new user account
def create_user(fname,lname,password):
	new_user = User(fname,lname,password)
	return new_user

	#Function to save a new user account
def save_user(user):
	User.save_user(user)

	#Function that verifies the existance of the user before creating credentials
def verify_user(first_name,password):
	checking_user = Credential.check_user(first_name,password)
	return checking_user

	#Function to generate a password automatically
def generate_password():
	gen_pass = Credential.generate_password()
	return gen_pass
	
	#Function to create a new credential
def create_credential(user_name,site_name,account_name,password):
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

	#Function to save a newly created credential
def save_credential(credential):
	Credential.save_credentials(credential)

	#Function to display credentials saved by a user
def display_credentials(user_name):
	return Credential.display_credentials(user_name)
	
	#Function to copy a credentials details to the clipboard
def copy_credential(site_name):
	return Credential.copy_credential(site_name)

def main():
	print(' ')
	print('Hello! Welcome to Password Locker.')
	while True:
		# print(' ')
		# print("-"*60)
		print('Use these codes to navigate: \n 1-Create an Account \n 2-Log In \n 3-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == '3':
			break

		elif short_code == '1':
			# print("-"*60)
			# print(' ')
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == '2':
			print("-"*60)
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n 1-Create a Credential \n 2-Display Credentials \n 3-Copy Password \n 4-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)

					if short_code == '4':
						print(" ")
						print(f'Goodbye {user_name}')
						break

					elif short_code == '1':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n 1-enter existing password \n 2-generate a password \n 3-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == '1':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == '2':
								password = generate_password()
								break
							elif psw_choice == '3':
								break
							else:
								print('Oops! Wrong option entered. Try again.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_credential(chosen_site)
						print('')
					else:
						print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			print("-"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again.')
				






if __name__ == '__main__':
	main()

