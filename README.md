# goit-algo-hw-03

# MODULE 3 | Recursive functions, algorithms and examples of their application
   
## Task 1: Recursive File Copy and Sort by Extension

Write a Python program that recursively copies files from the source directory, moves them to a new directory, and sorts them into subdirectories based on file extensions.

Also, consider the following conditions:

1. **Argument Parsing**: 
The script should accept two command-line arguments: the path to the source directory and the path to the destination directory (by default, if the destination directory is not provided, it should be named dist).

2.  **Recursive Directory Reading**:

 - Write a function that accepts a directory path as an argument.
 - The function should iterate over all items in the directory.
 - If an item is a directory, the function should call itself recursively for that directory.
 - If an item is a file, it should be prepared for copying.
3. **File Copying**:
- For each file type, a new path should be created in the source directory using the file extension as the subdirectory name.
- The file with the corresponding type should be copied to the appropriate subdirectory.
4. **Exception Handling**: 
The code should handle exceptions properly, such as file or directory access errors.

## Task 2: Koch Snowflake Fractal

Write a Python program that uses recursion to create a Koch snowflake fractal, with the recursion level specified by the user.

## Task 3: Tower of Hanoi (Optional)

Write a program that moves disks from peg A to peg C using peg B as an auxiliary. Disks have different sizes and are initially placed on the starting peg in descending order from top to bottom.

### Rules:

1. Only one disk can be moved at a time.
2. A disk can only be placed on a larger disk or an empty peg.
The input to the program is n — the number of disks on the starting peg. The output should log the sequence of steps to move the disks from peg A to peg C.