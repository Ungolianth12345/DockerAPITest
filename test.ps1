# Specify the file path
$file_path = ".\dock.py"

# Get the associated program for the file
$associated_program = (Get-Command -ErrorAction SilentlyContinue (Invoke-Item $file_path).Extension).Path

# Print the associated program
Write-Output "Associated program for $file_path: $associated_program"
