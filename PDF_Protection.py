import sys
import PyPDF2
import getpass
import os

def pdf_protect(input_file, output_file, password):
	"""this function handles pdf reading, encryption and saving process"""
	try:
		reader=PyPDF2.PdfReader(input_file)
		writer=PyPDF2.PdfWriter()

		# tracks the pages count for the user feedback
		pages_num=len(reader.pages)
		# Bulk copying pages for efficiency
		writer.append_pages_from_reader(reader)
		writer.add_metadata({}) # Clearing metadata for privacy
		writer.encrypt(password) # Applies 128-bit encryption
		# Write the encrypted content into the output pdf
		with open(output_file,'wb') as f:
			writer.write(f)
		print(f"Successfully {pages_num} pages are encrypted into {output_file}.")
	except FileNotFoundError:
		print(f"{input_file} is not found")
	except Exception as e:
		print(f"An Error occurred:{e}")

def main():
	"""This main function manages command-line inputs and user interaction"""
	# Ensures correct number of terminal arguments
	if len(sys.argv)!=3:
		print("Usage: python script.py <input_file> <output_file>")
		sys.exit(1)
	input_file=sys.argv[1]
	output_file=sys.argv[2]

	# Checking whether the source pdf exists or not.
	if not os.path.exists(input_file):
		print(f"Error: The file '{input_file}' doesn't exist. Please Check!")
		sys.exit(1)
	
	#Loops until the user provides a existing pdf and consistent password
	while True:
		password=getpass.getpass("Enter password:")
		confirm_password=getpass.getpass("Confirm password:")
		if password==confirm_password:
			pdf_protect(input_file, output_file, password)
			break
		else: 
			print("Passwords do not match. Please try again.\n")
	

if __name__=="__main__":
	main()