import unittest
import subprocess
import os

    # The values inserted in this test file are the values I got when I run the file_system_analyzer.py
    # You can check the Screenshot.png provided

class TestFileSystemAnalyzer(unittest.TestCase):
    
    #don't forget to change the path 
    directory_path = r"C:\Users\louay\OneDrive\Desktop\New\a"

    # Test case for directory traversal and file type analysis
    def test_directory_traversal_and_file_type_analysis(self):
        result = subprocess.run(["python", "file_system_analyzer.py", self.directory_path, "--large-file-threshold", "200000"], capture_output=True, text=True)
        self.assertIn("jpg: 5 files, Total Size: 227885 bytes", result.stdout)  
        self.assertIn("zip: 16 files, Total Size: 352 bytes", result.stdout)  
        self.assertIn("image: 1 files, Total Size: 45577 bytes", result.stdout)  # Add image file count and size

    # Test case for large files identification
    def test_large_files_identification(self):
        result = subprocess.run(["python", "file_system_analyzer.py", self.directory_path, "--large-file-threshold", "200000"], capture_output=True, text=True)
        self.assertIn("GitHubDesktopSetup-x64.exe: 143686248 bytes", result.stdout)  
        self.assertIn("VC_redist.x64.exe: 25416016 bytes", result.stdout)  
        self.assertNotIn("VC_redist.x64.exe: 143686248 bytes", result.stdout)  # Update with correct size for VC_redist.x64.exe

    # Test case for handling invalid directory path
    def test_invalid_directory_path(self):
        invalid_path = r"C:\invalid\path"
        result = subprocess.run(["python", "file_system_analyzer.py", invalid_path], capture_output=True, text=True)
        self.assertIn("Error: Invalid directory path.", result.stdout)

    # Test case for prompting user for directory and threshold input
    def test_prompt_user_for_input(self):
        result = subprocess.run(["python", "file_system_analyzer.py"], input=f"{self.directory_path}\n200000", capture_output=True, text=True)
        self.assertIn("File Type Analysis:", result.stdout)
        self.assertIn("Total number of files analyzed:", result.stdout)

if __name__ == "__main__":
    unittest.main()
