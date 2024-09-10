### Exercise: Sorting Files with `sort`

#### Objective:
Understand how to use the `sort` command to alphabetically and numerically sort records in text files.

#### Requirements:
- A Unix-based system with terminal access (e.g., Linux, macOS).
- Two text files: `alphabet.txt` and `counts.txt`.

#### Steps:

1. **Create Sample Files**

   - Create a file named `alphabet.txt` with the following content:
   
     ```bash
     echo -e "Alpha\nTango\nBravo\nEcho\nFoxtrot" > alphabet.txt
     ```

   - Create a file named `counts.txt` with the following content:
   
     ```bash
     echo -e "105\n8\n37\n42\n54" > counts.txt
     ```

2. **View the Content of the Files**

   - Display the content of the `alphabet.txt` file using the `cat` command:
   
     ```bash
     cat alphabet.txt
     ```
   
   - Display the content of the `counts.txt` file:
   
     ```bash
     cat counts.txt
     ```

3. **Sort the Alphabetical File**

   - Use the `sort` command to sort the contents of the `alphabet.txt` file alphabetically:
   
     ```bash
     sort alphabet.txt
     ```

   - **Expected Output:**
     ```
     Alpha
     Bravo
     Echo
     Foxtrot
     Tango
     ```

4. **Sort the Numerical File (Lexicographical Order)**

   - Use the `sort` command to sort the `counts.txt` file. By default, `sort` sorts numbers lexicographically (by characters), not by numeric value.
   
     ```bash
     sort counts.txt
     ```

   - **Expected Output:**
     ```
     105
     37
     42
     54
     8
     ```

5. **Sort the Numerical File (Numerical Order)**

   - Use the `-n` option with `sort` to sort the numbers in `counts.txt` in true numeric order:
   
     ```bash
     sort -n counts.txt
     ```

   - **Expected Output:**
     ```
     8
     37
     42
     54
     105
     ```

#### Tasks:

1. **Sort `alphabet.txt` Alphabetically**
   - Use `sort` to sort the alphabetically unordered words in `alphabet.txt`.

2. **Sort `counts.txt` Lexicographically**
   - Sort `counts.txt` using the default `sort` command and observe how it treats the numbers as strings.

3. **Sort `counts.txt` Numerically**
   - Use `sort -n` to sort `counts.txt` by actual numerical values.

#### Key Takeaways:
- `sort` sorts alphabetically or lexicographically by default.
- Use the `-n` option to sort numbers based on their numerical value.
