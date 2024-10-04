question_data = [
    {"text": "Python is a compiled language.", "answer": "False"},
    {"text": "HTML stands for Hypertext Markup Language.", "answer": "True"},
    {"text": "JavaScript is primarily used for server-side programming.", "answer": "False"},
    {"text": "CSS is used to style HTML documents.", "answer": "True"},
    {"text": "The 'print' function in Python outputs text to the console.", "answer": "True"},
    {"text": "A variable in programming cannot change its value.", "answer": "False"},
    {"text": "In Python, lists are ordered collections of items.", "answer": "True"},
    {"text": "The 'if' statement is used for making decisions in code.", "answer": "True"},
    {"text": "An array can hold elements of different data types.", "answer": "False"},
    {"text": "Java is a platform-independent language.", "answer": "True"},
    {"text": "A loop is used to execute a block of code repeatedly.", "answer": "True"},
    {"text": "Python uses indentation to define code blocks.", "answer": "True"},
    {"text": "The 'else' statement can be used without an 'if' statement.", "answer": "False"},
    {"text": "Functions in programming can return values.", "answer": "True"},
    {"text": "In C++, 'int' is used to declare integer variables.", "answer": "True"},
    {"text": "Comments in code are executed during runtime.", "answer": "False"},
    {"text": "The 'while' loop will continue until its condition is false.", "answer": "True"},
    {"text": "In Python, dictionaries are unordered collections of key-value pairs.", "answer": "True"},
    {"text": "SQL is used for managing relational databases.", "answer": "True"},
    {"text": "A syntax error occurs when the code is written correctly, but logic is wrong.", "answer": "False"},
    {"text": "In Java, the main method is the entry point of any program.", "answer": "True"},
    {"text": "In programming, an 'API' stands for Application Programming Interface.", "answer": "True"},
    {"text": "HTML can be used to create dynamic web applications.", "answer": "False"},
    {"text": "Git is a version control system.", "answer": "True"},
    {"text": "In JavaScript, 'undefined' means a variable has been declared but not assigned a value.", "answer": "True"},
    {"text": "A boolean data type can only hold one of two values: true or false.", "answer": "True"},
    {"text": "CSS can be used to create animations.", "answer": "True"},
    {"text": "Java uses a garbage collector to manage memory.", "answer": "True"},
    {"text": "In Python, tuples are mutable data structures.", "answer": "False"},
    {"text": "A 'for' loop is often used to iterate over a sequence.", "answer": "True"},
    {"text": "An exception is a runtime error that can be handled in code.", "answer": "True"},
    {"text": "In C#, the 'static' keyword means that a member belongs to the type itself rather than to a specific object.", "answer": "True"},
    {"text": "CSS selectors are used to apply styles to HTML elements.", "answer": "True"},
    {"text": "JavaScript is the same as Java.", "answer": "False"},
    {"text": "Python can be used for web development, data analysis, and artificial intelligence.", "answer": "True"},
    {"text": "An IDE stands for Integrated Development Environment.", "answer": "True"},
    {"text": "In programming, a 'bug' is a synonym for a feature.", "answer": "False"},
    {"text": "Java supports multiple inheritance.", "answer": "False"},
    {"text": "The term 'frontend' refers to the client-side of a web application.", "answer": "True"},
    {"text": "A class in OOP is a blueprint for creating objects.", "answer": "True"},
    {"text": "Python uses braces {} to define blocks of code.", "answer": "False"},
    {"text": "In SQL, the 'SELECT' statement is used to retrieve data from a database.", "answer": "True"},
    {"text": "A 'stack' is a data structure that follows the Last In, First Out (LIFO) principle.", "answer": "True"},
    {"text": "In Java, 'final' keyword is used to declare constants.", "answer": "True"},
    {"text": "HTML5 introduced new semantic elements like <header> and <footer>.", "answer": "True"},
    {"text": "In Python, the 'len()' function returns the length of a list.", "answer": "True"},
    {"text": "A 'query' is a request for information from a database.", "answer": "True"},
    {"text": "In Java, method overloading allows multiple methods with the same name but different parameters.", "answer": "True"},
    {"text": "In JavaScript, 'let' is used to declare variables with block scope.", "answer": "True"},
    {"text": "A 'boolean' can store any type of data.", "answer": "False"},
    {"text": "A function can be defined without a return statement.", "answer": "True"},
    {"text": "JSON stands for JavaScript Object Notation.", "answer": "True"},
    {"text": "CSS Grid is a layout system that allows for complex responsive web designs.", "answer": "True"},
    {"text": "In Python, 'None' is equivalent to 'null' in other languages.", "answer": "True"},
    {"text": "A web server's primary role is to send and receive email.", "answer": "False"},
    {"text": "In C++, pointers are used to reference memory addresses.", "answer": "True"},
    {"text": "The 'switch' statement is used as a shorthand for multiple 'if' statements.", "answer": "True"},
    {"text": "In HTML, the <script> tag is used to include JavaScript.", "answer": "True"},
    {"text": "React is a JavaScript library for building user interfaces.", "answer": "True"},
    {"text": "In Python, 'input()' reads user input as a string.", "answer": "True"},
    {"text": "XML is primarily used for styling web pages.", "answer": "False"},
    {"text": "The command line is a text-based interface to interact with the operating system.", "answer": "True"},
    {"text": "In CSS, 'margin' creates space inside an element's border.", "answer": "False"},
    {"text": "A 'kernel' is the core part of an operating system.", "answer": "True"},
    {"text": "In SQL, 'JOIN' is used to combine rows from two or more tables.", "answer": "True"},
    {"text": "In programming, 'refactoring' means rewriting code to improve its structure without changing its behavior.", "answer": "True"},
    {"text": "A 'constructor' is a special method used to create an instance of a class.", "answer": "True"},
    {"text": "In Python, 'break' is used to exit a loop.", "answer": "True"},
    {"text": "In Java, 'this' refers to the current object.", "answer": "True"},
    {"text": "A 'repository' is a storage location for software packages.", "answer": "True"},
    {"text": "In HTML, the <link> tag is used to connect CSS files.", "answer": "True"},
    {"text": "A database is a collection of organized data.", "answer": "True"},
    {"text": "In programming, an 'argument' is a value passed to a function.", "answer": "True"},
    {"text": "A 'debugger' is a tool used to find and fix errors in code.", "answer": "True"},
    {"text": "In Python, the 'map()' function applies a function to every item in an iterable.", "answer": "True"},
    {"text": "The 'return' statement is optional in a function.", "answer": "True"},
    {"text": "Python is a high-level programming language.", "answer": "True"},
    {"text": "HTML is a programming language.", "answer": "False"},
    {"text": "JavaScript can be used for both frontend and backend development.", "answer": "True"},
    {"text": "CSS stands for Cascading Style Sheets.", "answer": "True"},
    {"text": "The 'print' function in Python is used to output text.", "answer": "True"},
    {"text": "A variable can store multiple types of data in Python.", "answer": "True"},
    {"text": "In Java, 'String' is a primitive data type.", "answer": "False"},
    {"text": "A loop can be used to repeat a block of code.", "answer": "True"},
    {"text": "In Python, lists are mutable data structures.", "answer": "True"},
    {"text": "The 'else' statement can exist without an 'if' statement.", "answer": "False"},
    {"text": "Java uses a garbage collector to manage memory.", "answer": "True"},
    {"text": "HTML can be used to create interactive web pages.", "answer": "False"},
    {"text": "A function can return multiple values in Python.", "answer": "True"},
    {"text": "The 'while' loop continues until its condition is false.", "answer": "True"},
    {"text": "In C++, 'int' is used to declare integer variables.", "answer": "True"},
    {"text": "Comments in code are ignored by the compiler.", "answer": "True"},
    {"text": "SQL is used for querying databases.", "answer": "True"},
    {"text": "In Python, 'None' is equivalent to 'null' in JavaScript.", "answer": "True"},
    {"text": "The 'switch' statement is used in Python.", "answer": "False"},
    {"text": "An API stands for Application Programming Interface.", "answer": "True"},
    {"text": "CSS can be used to change the layout of a webpage.", "answer": "True"},
    {"text": "Java is a platform-independent language.", "answer": "True"},
    {"text": "In programming, a 'bug' refers to an error in the code.", "answer": "True"},
    {"text": "Variables in Python are case-sensitive.", "answer": "True"},
    {"text": "An array can hold elements of different data types.", "answer": "False"},
    {"text": "In JavaScript, 'undefined' means a variable has been declared but not assigned a value.", "answer": "True"},
    {"text": "A 'class' in programming is a blueprint for creating objects.", "answer": "True"},
    {"text": "CSS stands for Computer Style Sheets.", "answer": "False"},
    {"text": "In Python, 'len()' returns the length of a list or string.", "answer": "True"},
    {"text": "A 'tuple' in Python is mutable.", "answer": "False"},
    {"text": "The 'break' statement is used to exit a loop.", "answer": "True"},
    {"text": "The 'continue' statement skips the current iteration of a loop.", "answer": "True"},
    {"text": "In Java, the 'final' keyword is used to declare constants.", "answer": "True"},
    {"text": "HTML tags are case-sensitive.", "answer": "False"},
    {"text": "A 'stack' is a data structure that follows the Last In, First Out (LIFO) principle.", "answer": "True"},
    {"text": "In SQL, 'INSERT INTO' is used to add new data to a table.", "answer": "True"},
    {"text": "Python supports multiple inheritance.", "answer": "True"},
    {"text": "In C#, 'public' means a member is accessible from anywhere.", "answer": "True"},
    {"text": "A 'constructor' is a special method used to create an instance of a class.", "answer": "True"},
    {"text": "JavaScript is the same as Java.", "answer": "False"},
    {"text": "Git is a version control system.", "answer": "True"},
    {"text": "The 'return' statement is optional in a function.", "answer": "False"},
    {"text": "A 'binary tree' is a tree data structure in which each node has at most two children.", "answer": "True"},
    {"text": "In Python, 'for' loops can iterate over a range of numbers.", "answer": "True"},
    {"text": "In programming, a 'syntax error' occurs when the code violates the rules of the programming language.", "answer": "True"},
    {"text": "In C++, 'new' is used to allocate memory dynamically.", "answer": "True"},
    {"text": "The 'print()' function in Java outputs text to the console.", "answer": "False"},
    {"text": "In HTML, the <head> tag contains metadata about the document.", "answer": "True"},
    {"text": "Python uses braces {} to define blocks of code.", "answer": "False"},
    {"text": "A 'compiler' translates code from a high-level language to machine code.", "answer": "True"},
    {"text": "A 'database' is a structured collection of data.", "answer": "True"},
    {"text": "In Python, you can create comments by using the '#' symbol.", "answer": "True"},
    {"text": "CSS Flexbox is a layout model that provides a more efficient way to arrange items.", "answer": "True"},
    {"text": "In SQL, 'WHERE' is used to filter records.", "answer": "True"},
    {"text": "In programming, 'refactoring' means rewriting code to improve its structure without changing its behavior.", "answer": "True"},
    {"text": "In Java, 'this' refers to the current object.", "answer": "True"},
    {"text": "In Python, the 'map()' function applies a function to every item in an iterable.", "answer": "True"},
    {"text": "A web server's primary role is to send and receive email.", "answer": "False"},
    {"text": "In JavaScript, 'let' is used to declare variables with block scope.", "answer": "True"},
    {"text": "The term 'frontend' refers to the server-side of a web application.", "answer": "False"},
    {"text": "A 'repository' is a storage location for software packages.", "answer": "True"},
    {"text": "In C++, pointers are used to reference memory addresses.", "answer": "True"},
    {"text": "The 'HTML' is used to style web pages.", "answer": "False"},
    {"text": "In Python, 'break' is used to exit a loop.", "answer": "True"},
    {"text": "CSS Grid is a layout system that allows for complex responsive web designs.", "answer": "True"},
    {"text": "A 'boolean' data type can hold any type of data.", "answer": "False"},
    {"text": "In Python, 'input()' reads user input as a string.", "answer": "True"},
    {"text": "XML is primarily used for styling web pages.", "answer": "False"},
    {"text": "The command line is a text-based interface to interact with the operating system.", "answer": "True"},
    {"text": "In CSS, 'padding' creates space inside an element's border.", "answer": "True"},
    {"text": "The 'main()' function is optional in C programming.", "answer": "False"},
    {"text": "A class in OOP is a blueprint for creating objects.", "answer": "True"},
    {"text": "In Java, method overloading allows multiple methods with the same name but different parameters.", "answer": "True"},
    {"text": "A 'syntax error' is a mistake in the logic of a program.", "answer": "False"},
    {"text": "Java is the same as JavaScript.", "answer": "False"},
    {"text": "Python supports functional programming features.", "answer": "True"},
    {"text": "In Python, dictionaries are ordered collections of key-value pairs.", "answer": "True"},
    {"text": "CSS can be used to change the text color of HTML elements.", "answer": "True"},
    {"text": "A web browser interprets HTML and displays the content as a web page.", "answer": "True"},
    {"text": "In Java, 'abstract' classes cannot be instantiated.", "answer": "True"},
    {"text": "In C#, 'static' members belong to the class rather than any object instance.", "answer": "True"},
    {"text": "Python's 'self' refers to the class itself.", "answer": "False"},
    {"text": "The 'char' data type in C++ can hold a single character.", "answer": "True"},
    {"text": "In SQL, the 'UPDATE' statement is used to modify existing records.", "answer": "True"},
    {"text": "In HTML, the <footer> tag is used to define the footer of a document.", "answer": "True"},
    {"text": "A 'function' is a reusable block of code that performs a specific task.", "answer": "True"},
    {"text": "In Python, the 'try' block is used to catch exceptions.", "answer": "False"},
    {"text": "The 'class' keyword is used to define a class in Python.", "answer": "True"},
    {"text": "A JSON file is a text file that uses a specific syntax for storing data.", "answer": "True"},
    {"text": "In programming, a 'loop' is used to repeat code a fixed number of times.", "answer": "False"},
    {"text": "A 'hash table' is a data structure that implements an associative array.", "answer": "True"}
]

question_data.extend([
    {"text": "In C++, 'namespace' is used to organize code.", "answer": "True"},
    {"text": "The 'else' statement can follow a 'while' loop.", "answer": "True"},
    {"text": "Python uses indentation to define the scope of loops and functions.", "answer": "True"},
    {"text": "In SQL, 'COUNT()' is an aggregate function.", "answer": "True"},
    {"text": "In Java, 'static' methods can access instance variables directly.", "answer": "False"},
    {"text": "In HTML, the <body> tag is used to define the main content of a document.", "answer": "True"},
    {"text": "A 'singly linked list' can traverse in only one direction.", "answer": "True"},
    {"text": "CSS can be applied to HTML documents through an external file, internal styles, or inline styles.", "answer": "True"},
    {"text": "In Python, 'is' checks for value equality.", "answer": "False"},
    {"text": "In Java, 'final' can be applied to classes, methods, and variables.", "answer": "True"},
    {"text": "In programming, a 'script' refers to a set of commands that are executed by a specific runtime environment.", "answer": "True"},
    {"text": "An 'interface' in Java is a blueprint for a class.", "answer": "True"},
    {"text": "In HTML, the <div> tag is a block-level container.", "answer": "True"},
    {"text": "The 'git clone' command creates a new local copy of a remote repository.", "answer": "True"},
    {"text": "In Python, you can use 'import' to include libraries and modules.", "answer": "True"},
    {"text": "The 'socket' library in Python is used for creating network connections.", "answer": "True"},
    {"text": "In JavaScript, functions are first-class citizens.", "answer": "True"},
    {"text": "In Python, you can use 'def' to declare a function.", "answer": "True"},
    {"text": "CSS can be used to create responsive web designs.", "answer": "True"},
    {"text": "In C++, 'delete' is used to free memory allocated with 'new'.", "answer": "True"},
    {"text": "In SQL, the 'SELECT * FROM' statement retrieves all columns from a table.", "answer": "True"},
    {"text": "A 'linked list' can store data in a linear fashion but does not use contiguous memory.", "answer": "True"},
    {"text": "In HTML, the <img> tag is used to embed images.", "answer": "True"},
    {"text": "In Python, 'open()' is used to read files.", "answer": "True"},
    {"text": "A 'parameter' is a variable in the function definition.", "answer": "True"},
    {"text": "JavaScript can manipulate HTML and CSS.", "answer": "True"},
    {"text": "The 'try' block in Python is used to handle exceptions.", "answer": "True"},
    {"text": "The 'float' data type can hold decimal values in programming.", "answer": "True"},
    {"text": "In C#, you can use 'var' to declare variables with inferred types.", "answer": "True"},
    {"text": "In Python, a 'set' is an unordered collection of unique elements.", "answer": "True"},
    {"text": "In programming, 'inheritance' is a way to create a new class based on an existing class.", "answer": "True"},
    {"text": "CSS rules are applied in the order they are written.", "answer": "True"},
    {"text": "In Java, 'void' indicates that a method does not return a value.", "answer": "True"},
    {"text": "In Python, 'lambda' functions are anonymous functions.", "answer": "True"},
    {"text": "In C++, '#include' is used to include libraries.", "answer": "True"},
    {"text": "A 'database management system' is used to manage databases.", "answer": "True"},
    {"text": "In HTML, <table> is used to create tables.", "answer": "True"},
    {"text": "In Java, 'super' is used to call the superclass constructor.", "answer": "True"},
    {"text": "The 'main()' function is required in Python scripts.", "answer": "False"},
    {"text": "In SQL, 'DISTINCT' is used to return unique values.", "answer": "True"},
    {"text": "In programming, an 'algorithm' is a step-by-step procedure for solving a problem.", "answer": "True"},
    {"text": "In C#, 'string' is a primitive data type.", "answer": "False"},
    {"text": "In HTML, <link> is used to connect external CSS files.", "answer": "True"},
    {"text": "In Java, 'throws' is used to declare exceptions in a method signature.", "answer": "True"},
    {"text": "In Python, you can use 'dict()' to create a dictionary.", "answer": "True"},
    {"text": "A 'data structure' is a way to organize and store data.", "answer": "True"},
    {"text": "The 'join()' method in Python is used to concatenate strings.", "answer": "True"},
    {"text": "In C++, 'cout' is used for console output.", "answer": "True"},
    {"text": "In SQL, 'HAVING' is used to filter groups after aggregation.", "answer": "True"},
    {"text": "A 'merge sort' is a sorting algorithm that uses recursion.", "answer": "True"},
    {"text": "In JavaScript, the 'window' object represents the browser window.", "answer": "True"},
    {"text": "In HTML, the <header> tag defines the header of a document.", "answer": "True"},
    {"text": "A 'variable' is a named storage location in memory.", "answer": "True"},
    {"text": "In Python, the 'break' statement is used to terminate a loop.", "answer": "True"},
    {"text": "In C++, the 'virtual' keyword is used to define a base class method that can be overridden.", "answer": "True"},
    {"text": "A 'while' loop continues until its condition is false.", "answer": "True"},
    {"text": "In HTML, the <section> tag is used to define sections in a document.", "answer": "True"},
    {"text": "The 'push()' method adds an element to the end of an array in JavaScript.", "answer": "True"},
    {"text": "In Python, 'elif' is used for multiple conditional checks.", "answer": "True"},
    {"text": "In C#, 'interface' defines a contract that classes can implement.", "answer": "True"},
    {"text": "CSS can be used to hide elements on a web page.", "answer": "True"},
    {"text": "The 'yield' keyword in Python is used to return a generator.", "answer": "True"},
    {"text": "In SQL, 'ALTER TABLE' is used to modify an existing table.", "answer": "True"},
    {"text": "In Java, 'StringBuilder' is used for mutable strings.", "answer": "True"},
    {"text": "A 'binary search' is an efficient algorithm for finding an item in a sorted list.", "answer": "True"},
    {"text": "In programming, a 'namespace' is a container for identifiers.", "answer": "True"},
    {"text": "In Python, the 'strip()' method removes whitespace from the beginning and end of a string.", "answer": "True"},
    {"text": "In JavaScript, 'document.getElementById()' is used to access elements by their ID.", "answer": "True"},
    {"text": "In C++, a 'reference' is an alias for an existing variable.", "answer": "True"},
    {"text": "In HTML, the <form> tag is used to create interactive forms.", "answer": "True"},
    {"text": "In SQL, 'UNION' is used to combine the results of two or more SELECT statements.", "answer": "True"},
    {"text": "A 'frontend framework' is used to build server-side applications.", "answer": "False"},
    {"text": "In Python, 'break' is used to exit a loop.", "answer": "True"},
    {"text": "The 'split()' method in Python is used to split strings.", "answer": "True"},
    {"text": "In Java, 'static' variables are shared among all instances of a class.", "answer": "True"},
    {"text": "A 'forEach' loop is a method available in JavaScript arrays.", "answer": "True"},
    {"text": "In HTML, the <meta> tag is used to specify metadata about a web page.", "answer": "True"},
    {"text": "The 'case' keyword is used in Python to handle multiple conditions.", "answer": "False"},
    {"text": "In C++, 'new' allocates memory on the heap.", "answer": "True"},
    {"text": "The 'float' data type in Java can hold decimal values.", "answer": "True"},
])

question_data.extend([
    {"text": "In Python, you can define a class using the 'class' keyword.", "answer": "True"},
    {"text": "In C#, 'string' is an object that represents text.", "answer": "True"},
    {"text": "A 'function' can only take a fixed number of parameters.", "answer": "False"},
    {"text": "In HTML, <ul> defines an ordered list.", "answer": "False"},
    {"text": "Java's 'System.out.println()' is used to print to the console.", "answer": "True"},
    {"text": "In SQL, the 'DELETE' statement removes records from a table.", "answer": "True"},
    {"text": "The 'class' keyword in Python is used to define classes.", "answer": "True"},
    {"text": "In C++, 'cout' is used for input.", "answer": "False"},
    {"text": "In JavaScript, 'var' declares a variable with function scope.", "answer": "True"},
    {"text": "In Python, list comprehensions provide a concise way to create lists.", "answer": "True"},
    {"text": "A 'data type' defines the type of data that can be stored in a variable.", "answer": "True"},
    {"text": "In Java, 'void' methods can return values.", "answer": "False"},
    {"text": "The 'import' statement in Python is used to include modules.", "answer": "True"},
    {"text": "In SQL, the 'INNER JOIN' keyword is used to return rows that have matching values in both tables.", "answer": "True"},
    {"text": "In Java, the 'new' keyword is used to create objects.", "answer": "True"},
    {"text": "The 'public' access modifier allows members to be accessible from anywhere.", "answer": "True"},
    {"text": "In Python, 'assert' is used for debugging purposes.", "answer": "True"},
    {"text": "A 'bubble sort' is a simple sorting algorithm.", "answer": "True"},
    {"text": "In JavaScript, 'let' allows you to declare variables that can be re-assigned.", "answer": "True"},
    {"text": "In HTML, <span> is an inline container.", "answer": "True"},
    {"text": "A 'hash function' is used to convert data into a fixed size.", "answer": "True"},
    {"text": "In C++, 'friend' function can access private members of a class.", "answer": "True"},
    {"text": "In SQL, 'GROUP BY' is used to group rows that have the same values in specified columns.", "answer": "True"},
    {"text": "In Python, 'str()' converts an object to a string.", "answer": "True"},
    {"text": "In programming, a 'loop' can be infinite.", "answer": "True"},
    {"text": "In Java, 'abstract' methods can have a body.", "answer": "False"},
    {"text": "A 'web server' serves web pages to users.", "answer": "True"},
    {"text": "In Python, you can use 'map()' to apply a function to a list.", "answer": "True"},
    {"text": "In HTML, <canvas> is used to draw graphics.", "answer": "True"},
    {"text": "In Java, 'throw' is used to raise exceptions.", "answer": "True"},
    {"text": "The 'in' keyword in Python checks for membership in a collection.", "answer": "True"},
    {"text": "In SQL, 'LIKE' is used to search for a specified pattern in a column.", "answer": "True"},
    {"text": "A 'function' is a block of code that performs a specific task.", "answer": "True"},
    {"text": "In C++, 'protected' members are accessible only within the class and derived classes.", "answer": "True"},
    {"text": "In JavaScript, 'this' refers to the global object in a function.", "answer": "False"},
    {"text": "In Python, 'pop()' removes and returns the last item in a list.", "answer": "True"},
    {"text": "A 'RESTful API' uses HTTP requests to perform CRUD operations.", "answer": "True"},
    {"text": "In HTML, the <footer> tag defines the footer of a section or page.", "answer": "True"},
    {"text": "In Java, 'import' is used to include other classes.", "answer": "True"},
    {"text": "In SQL, 'SELECT DISTINCT' retrieves unique records from a table.", "answer": "True"},
    {"text": "In programming, an 'exception' is an event that disrupts the normal flow of execution.", "answer": "True"},
    {"text": "A 'query' is a request for information from a database.", "answer": "True"},
    {"text": "In Python, you can use 'enumerate()' to iterate over a list with indexes.", "answer": "True"},
    {"text": "In Java, 'synchronized' is used to control access to a method or block.", "answer": "True"},
    {"text": "The 'return' keyword is used to exit a function and return a value.", "answer": "True"},
    {"text": "In HTML, <blockquote> is used to define a section that is quoted from another source.", "answer": "True"},
    {"text": "In C++, a 'struct' can contain methods.", "answer": "True"},
    {"text": "In SQL, 'ORDER BY' is used to sort the results of a query.", "answer": "True"},
    {"text": "In Java, 'volatile' is used to indicate that a variable's value may change unexpectedly.", "answer": "True"},
    {"text": "The 'null' value in programming represents the absence of a value.", "answer": "True"},
    {"text": "In Python, the 'append()' method adds an item to the end of a list.", "answer": "True"},
    {"text": "A 'function expression' creates a function that can be used as a variable.", "answer": "True"},
    {"text": "In C++, 'const' indicates that a variable's value cannot change.", "answer": "True"},
    {"text": "In SQL, 'WHERE' is used to filter records before any groupings.", "answer": "True"},
    {"text": "In JavaScript, 'typeof' is used to determine the type of a variable.", "answer": "True"},
    {"text": "In HTML, <audio> is used to embed sound content.", "answer": "True"},
    {"text": "In programming, a 'package' is a collection of related classes and interfaces.", "answer": "True"},
    {"text": "In Python, the 'finally' block is executed whether an exception occurs or not.", "answer": "True"},
    {"text": "A 'singleton' is a design pattern that restricts a class to a single instance.", "answer": "True"},
    {"text": "In Java, 'interface' can contain method implementations.", "answer": "False"},
    {"text": "The 'slice' operator in Python is used to extract portions of lists or strings.", "answer": "True"},
    {"text": "In SQL, 'INSERT' is used to remove records from a table.", "answer": "False"},
    {"text": "In HTML, <script> is used to define client-side JavaScript code.", "answer": "True"},
    {"text": "In C++, the 'new' operator allocates memory for an object.", "answer": "True"},
    {"text": "A 'test case' is a set of conditions to verify if a software program is working correctly.", "answer": "True"},
    {"text": "In Python, you cannot concatenate strings and integers directly.", "answer": "True"},
    {"text": "The 'render()' function is commonly used in web frameworks to generate HTML.", "answer": "True"},
])
question_data.extend([
    {"text": "In JavaScript, 'async' is used to define asynchronous functions.", "answer": "True"},
    {"text": "In SQL, 'INSERT INTO' is used to add new rows to a table.", "answer": "True"},
    {"text": "In HTML, <iframe> is used to embed another document within the current HTML document.", "answer": "True"},
    {"text": "In C#, 'List' is a collection that can resize dynamically.", "answer": "True"},
    {"text": "In Python, a 'tuple' is a mutable collection.", "answer": "False"},
    {"text": "In Java, 'extends' is used to create a subclass.", "answer": "True"},
    {"text": "A 'foreign key' is a field in one table that uniquely identifies a row of another table.", "answer": "True"},
    {"text": "In JavaScript, 'JSON' stands for JavaScript Object Notation.", "answer": "True"},
    {"text": "In Python, 'super()' is used to call a method from the parent class.", "answer": "True"},
    {"text": "A 'binary tree' is a tree data structure in which each node has at most two children.", "answer": "True"},
    {"text": "In HTML, <nav> is used to define navigation links.", "answer": "True"},
    {"text": "In C++, a 'pointer' holds the memory address of another variable.", "answer": "True"},
    {"text": "In SQL, 'CASE' is used to execute conditional logic.", "answer": "True"},
    {"text": "In Python, a 'list' can contain mixed data types.", "answer": "True"},
    {"text": "In Java, 'try-catch' blocks are used for exception handling.", "answer": "True"},
    {"text": "A 'constructor' is a special method used to initialize objects.", "answer": "True"},
    {"text": "In JavaScript, 'map()' creates a new array populated with the results of calling a provided function on every element.", "answer": "True"},
    {"text": "In Python, the 'raise' keyword is used to trigger exceptions.", "answer": "True"},
    {"text": "In HTML, <style> is used to define CSS styles.", "answer": "True"},
    {"text": "In C#, 'override' is used to provide a new implementation of a method in a derived class.", "answer": "True"},
    {"text": "In SQL, 'EXISTS' checks for the existence of any record in a subquery.", "answer": "True"},
    {"text": "In programming, 'encapsulation' restricts direct access to some of an object's components.", "answer": "True"},
    {"text": "In Python, 'list' is a data structure that stores elements in a sequence.", "answer": "True"},
    {"text": "In Java, 'main()' method is the entry point of any Java program.", "answer": "True"},
    {"text": "A 'metadata' is data that describes other data.", "answer": "True"},
    {"text": "In HTML, <link> is used to define a relationship between a document and an external resource.", "answer": "True"},
    {"text": "In C++, 'template' allows functions and classes to operate with generic types.", "answer": "True"},
    {"text": "In Java, 'char' is used to store a single character.", "answer": "True"},
    {"text": "A 'data lake' is a centralized repository for storing large amounts of structured and unstructured data.", "answer": "True"},
    {"text": "In SQL, 'CREATE TABLE' is used to create a new table in a database.", "answer": "True"},
    {"text": "In Python, the 'filter()' function is used to filter elements from a list.", "answer": "True"},
    {"text": "In Java, 'interface' cannot have instance variables.", "answer": "True"},
    {"text": "In HTML, <progress> is used to display progress of a task.", "answer": "True"},
    {"text": "A 'session' is a way to store information about a user across multiple pages.", "answer": "True"},
    {"text": "In Python, 'enumerate()' adds a counter to an iterable.", "answer": "True"},
    {"text": "In JavaScript, 'NaN' represents a non-numeric value.", "answer": "True"},
    {"text": "In SQL, 'LIMIT' is used to specify the number of records to return.", "answer": "True"},
    {"text": "In C++, 'const_cast' is used to cast away constness.", "answer": "True"},
    {"text": "In HTML, <code> is used to define computer code.", "answer": "True"},
    {"text": "In Python, 'kwargs' is used to pass a variable number of keyword arguments.", "answer": "True"},
    {"text": "A 'function signature' includes the function name and the parameters.", "answer": "True"},
    {"text": "In Java, 'assert' is used for debugging purposes.", "answer": "True"},
    {"text": "In SQL, 'UPDATE' is used to change existing records in a table.", "answer": "True"},
    {"text": "In Python, a 'dictionary' is an unordered collection of key-value pairs.", "answer": "True"},
    {"text": "In Java, 'volatile' variables can be accessed by multiple threads.", "answer": "True"},
    {"text": "In programming, a 'loop' cannot be nested inside another loop.", "answer": "False"},
    {"text": "In C#, 'enum' is a special value type that defines a set of named constants.", "answer": "True"},
    {"text": "In HTML, <template> is used to define content that can be reused.", "answer": "True"},
    {"text": "A 'namespace' prevents name conflicts by organizing code into separate scopes.", "answer": "True"},
    {"text": "In SQL, 'DROP TABLE' is used to delete a table from a database.", "answer": "True"},
    {"text": "In Python, the 'sorted()' function returns a new sorted list from the elements of any iterable.", "answer": "True"},
    {"text": "In Java, 'charAt()' is used to retrieve a character at a specific index of a string.", "answer": "True"},
    {"text": "In C++, 'namespace' can contain functions, variables, and classes.", "answer": "True"},
    {"text": "A 'linked list' allows for efficient insertion and deletion of elements.", "answer": "True"},
    {"text": "In Python, 'map()' returns an iterator that applies a function to all the items in an input list.", "answer": "True"},
    {"text": "In JavaScript, 'document.querySelector()' returns the first element that matches a specified CSS selector.", "answer": "True"},
    {"text": "In SQL, 'SET' is used to specify the values to be updated in an UPDATE statement.", "answer": "True"},
    {"text": "In C#, 'string' is an alias for the 'System.String' type.", "answer": "True"},
    {"text": "In HTML, <mark> is used to highlight text.", "answer": "True"},
    {"text": "In Python, 'next()' is used to retrieve the next item from an iterator.", "answer": "True"},
])
