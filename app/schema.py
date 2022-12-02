instructions =[
    "DROP TABLE IF EXISTS email",
    """CREATE TABLE email (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        email VARCHAR(255) NOT NULL, 
        subject TEXT NOT NULL,
        content TEXT NOT NULL
     )""",
    """INSERT INTO email (email, subject, content) VALUES
    ('helmer.morales1@gmail.com', 'Helmer Morales', 'Hola mundo')"""

   
]