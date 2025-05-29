# 0x06. Star Wars API

## Description

This project involves writing a Node.js script that interacts with the Star Wars API (SWAPI) to retrieve and display a list of characters from a specified Star Wars movie. The movie is selected using a movie ID passed as a command-line argument.

This task is designed to strengthen your understanding of:

- Making HTTP requests in Node.js
- Parsing and handling JSON responses
- Working with RESTful APIs
- Asynchronous programming using callbacks and/or async/await
- Using command-line arguments
- Iterating and managing arrays of asynchronous data

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on **Ubuntu 20.04 LTS** using **Node.js v10.14.x**
- The first line of all your files should be exactly `#!/usr/bin/node`
- Your code should be semistandard compliant:
  - Based on Standard JavaScript style + semicolons
- All your files must be executable
- You are **not allowed to use `var`**
- All files should end with a new line
- Length of your files will be tested using `wc`

## Usage

To run the script, use the following format:

```bash
./0-starwars_characters.js <movie_ID>

Example:
Bash

./0-starwars_characters.js 3
This will fetch and display the characters from Episode VI (Return of the Jedi) in the order they appear in the movie.

Expected Output:
python-repl
Copy code
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
How It Works
The script reads the movie ID from the command line.

It sends a GET request to the SWAPI film endpoint:
https://swapi-api.alx-tools.com/api/films/<movie_ID>/

It retrieves the list of character URLs from the film data.

It makes additional HTTP requests to each character URL in order.

It prints out the name of each character line by line.

Concepts Used
request module for HTTP GET requests

JSON parsing with JSON.parse()

Asynchronous programming using callbacks or async/await

Command-line arguments with process.argv

Iteration with for...of and asynchronous functions

Resources
SWAPI Documentation

Node.js request module

Node.js Command Line Arguments

JavaScript Promises

Async/Await

Author
Duncan Korir