instructions =[
    "DROP TABLE IF EXISTS email",
    """CREATE TABLE email (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        email VARCHAR(255) NOT NULL, 
        subject TEXT NOT NULL,
        content TEXT NOT NULL
     )""",
   
]