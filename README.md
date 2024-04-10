# Book Library Management

## Install dependencies

```bash
pip install -r requirements.txt
```

## Setup DB

1. Create Database:

    ```sql
    CREATE DATABASE dbmsproject;
    ```

2. Create Tables:

    - `Customer`:

        ```sql
        create table Customer (
          id int primary key auto_increment,
          first_name varchar(255) not null,
          last_name varchar(255) not null,
          address varchar(255) not null,
          phone_no varchar(10) not null
        );

        insert into Customer (first_name, last_name, address, phone_no) values ('John', 'Doe', '123 Main St, Anytown', '1234567890');
        insert into Customer (first_name, last_name, address, phone_no) values ('Jane', 'Smith', '456 Elm St, Somewhere', '9876543210');
        insert into Customer (first_name, last_name, address, phone_no) values ('Alice', 'Johnson', '789 Oak St, Nowhere', '4567890123');
        insert into Customer (first_name, last_name, address, phone_no) values ('Bob', 'Williams', '321 Pine St, Anyplace', '7890123456');
        insert into Customer (first_name, last_name, address, phone_no) values ('Emily', 'Brown', '654 Maple St, Everywhere', '2345678901');
        ```

    - `Book`:

        ```sql
        create table Book (
          isbn int primary key auto_increment,
          title varchar(255) not null,
          price real not null,
          author int not null
        );

        insert into Book (title, price, author) values ('The Great Gatsby', 10.99, 1);
        insert into Book (title, price, author) values ('To Kill a Mockingbird', 9.99, 2);
        insert into Book (title, price, author) values ('1984', 11.99, 3);
        insert into Book (title, price, author) values ('Pride and Prejudice', 8.99, 4);
        insert into Book (title, price, author) values ('The Catcher in the Rye', 12.99, 5);
        ```

    - `_Order`:

        ```sql
        create table _Order (
          id int primary key auto_increment,
          total real not null
        );

        insert into _Order (total) values (50.75);
        insert into _Order (total) values (35.25);
        insert into _Order (total) values (28.50);
        insert into _Order (total) values (42.00);
        insert into _Order (total) values (65.80);
        ```

    - `Category`:

        ```sql
        create table Category (
          id int primary key auto_increment,
          name varchar(255) not null unique
        );

        insert into Category (name) values ('Fiction');
        insert into Category (name) values ('Non-fiction');
        insert into Category (name) values ('Mystery');
        insert into Category (name) values ('Science Fiction');
        insert into Category (name) values ('Romance');
        ```

    - `Publisher`:

        ```sql
        create table Publisher (
          license varchar(15) not null unique,
          first_name varchar(255),
          last_name varchar(255),
          address varchar(255)
        );

        insert into Publisher (license, first_name, last_name, address) values ('ABC123', 'Harper', 'Lee', '789 Broadway, Bigcity');
        insert into Publisher (license, first_name, last_name, address) values ('DEF456', 'George', 'Orwell', '456 Park Ave, Metropolis');
        insert into Publisher (license, first_name, last_name, address) values ('GHI789', 'Jane', 'Austen', '123 High St, Smalltown');
        insert into Publisher (license, first_name, last_name, address) values ('JKL012', 'J.D.', 'Salinger', '101 Avenue Rd, Townsville');
        insert into Publisher (license, first_name, last_name, address) values ('MNO345', 'F. Scott', 'Fitzgerald', '246 Main St, Villageton');
        ```

    - `Payment`:

        ```sql
        create table Payment (
          id int primary key auto_increment,
          amt real not null,
          notes varchar(255)
        );
        ```

3. Start Application.
