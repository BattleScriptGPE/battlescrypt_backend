CREATE TABLE IF NOT EXISTS Users ( 
    userID INT AUTO_INCREMENT, 
    name VARCHAR(100) , 
    username VARCHAR(100) , 
    password VARCHAR(100) , 
    mail VARCHAR(100) , 
    role INT , 
    created_at timestamp default current_timestamp , 
    primary key (userID)
);