[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10184631&assignment_repo_type=AssignmentRepo)
# Assessment 2: Video Inventory Manager.  <br>Object Oriented Programming + CSV Reading


## Requirements
- This assessment should be completed using Python.

## Challenge
*Back in the day*, humans would actually leave their homes to go rent a physical video copy of movies (what a strange concept, right?). Blockbuster was the leading video rental company in this era. Today, there is only one Blockbuster location left which is located in Bend, Oregon. We are going to ask you to build a video inventory application for this Blockbuster!

### Data Files Provided
 We have provided you with two data csv files. customers.csv and inventory.csv.

#### customer.csv
- id
- account_type 
- first_name 
- last_name 
- current_video_rentals (list of titles separated by '/')

#### inventory.csv
- id 
- title 
- rating 
- release_year 
- copies_available 

### Data Management
Your Video Inventory Management application should manage the following data:

- Manage customer information:
  - customer id
  - customer account type (sx/px/sf/pf)
    - "sx" = standard account: max 1 rental out at a time
    - "px" = premium account: max 3 rentals out at a time
    - "sf" = standard family account: max 1 rental out at a time AND can not rent any "R" rated movies
    - "pf" = premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies   
  - customer first name
  - customer last name 
  - current list of video rentals (*by title*)
- Manage the store's video inventory:
  - video id
  - video title
  - video rating
  - video release year
  - number of copies currently available in-store
  
### Application Features
Your application should allow:
1. Viewing the current video inventory for the store
    - show `title` and `copies_available` for each video in the inventory
2. Viewing all customers
    - show `customer_id` and `name` for each customer in the store
3. Viewing a customer's current rented videos
    - take in a `customer_id` from the user and show current rented videos for that customer
    - each title should be listed separately (i.e. not displayed as one string with slashes straight from the CSV file)
4. Adding a new customer
    - a newly created customer should not have any rentals 
    - can you prevent duplicate ids from existing?
5. Renting a video out to a customer
    - video *by `title`*
    - customer *by `id`*
    - **IMPORTANT:** Customers should be limited based on their account type. Your application should enforce these limitations when attempting to rent a video!
6. Returning a video from a customer
    - customer *by `id`*
    - video *by `title`*
7. Exiting the application

Be sure to give careful consideration into what data structures & data types (including classes) you might need to use in your application logic. 

Your menu should look something like this: 
```
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View store customers
3. View customer rented videos
4. Add new customer
5. Rent video
6. Return video
7. Exit
```

## Important Grading Information
- Make sure you read the [Assessment-2 Grading Rubric](https://docs.google.com/spreadsheets/d/1AlAQukmB3SS7IyW2hu0zY-9RaQnHY3lLeTi2O1fUb30/edit?usp=sharing).
  - Application Correctness (60%)
  - Code Design (40%)
- You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - *5% penalty*: If you complete and submit the retake **within one week** of receiving your grade. 
  - *10% penalty*: If you complete and submit the retake **by the start of week 12**. A retake for this assessment WILL NOT be accepted after this date.

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with the help of other students/individuals.
- Push your solution up to this repo and submit in google classroom.
