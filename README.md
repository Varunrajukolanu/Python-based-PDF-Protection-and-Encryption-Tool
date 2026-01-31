During my tenure as an "Offensive Cybersecurity Intern" in  InLighnX Global, I developed a "Python-based PDF Protection and Encryption Tool" designed to automate document security through "128-bit encryption". I engineered a "modular architecture" that effectively separates the "User Interface logic," which includes secure credential input via the "getpass module", "fail-fast file validation" using os.path.exists(), and "password consistency loops", from the "Core Technical logic".

Technical Features:
1.Optimized Page Transfer: Implemented the modern "append_pages_from_reader shortcut" for "efficient bulk page transfers", which maintains document integrity better than manual loops.
2.Privacy Sanitization: Integrated "metadata sanitization" by stripping internal identifiers like "Author" and "Creator" using add_metadata({}).
3.Secure Input: Used the getpass library to ensure passwords are not echoed to the screen or stored in terminal history.
4.Robust Error Handling: Created a "fail-fast" system to verify file existence before processing begins.

How to Run:
Install Dependencies: pip install PyPDF2 

Execute the Script:

python PDF_Protection.py <input_file.pdf> <output_file.pdf> 
***Note: Make sure the script and input_file are in the same location***

Verified Test Results
The tool’s robustness was verified through "rigorous testing":

Successful Encryption Message: 8 pages were encrypted into the result file correctly.

Missing File Handling: The program stops immediately if the file path is incorrect.

Retry Loops: The script successfully forces a retry if passwords do not match.

Technical Limitations: I created a pdf with images and text consisting of 27,216 pages, the terminal took almost a minute to complete the process. It isnt a limitaion of the pdf size, the bigger the pdf the bigger the time it will take to complete. The completed encrypted file took a minute to open after entering the password.

Conclusion
This project demonstrates a sophisticated application of "document security", providing a "robust solution for confidential document automation" that successfully meets "modern privacy standards".
