/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = 'Campus';
const collection = 'Students';

// Create a new database.
use(database);

// Create a new collection.
db.createCollection(collection);

const students = [
    {'fname':'Omar','lname':'Youssef','email':'yousefomar720@gmail.com','studid':20210591},
    {'fname':'Nourhan','lname':'Abdallah','email':'nourhanabdallah@gmail.com','studid':20210437}
]

db.Students.insertMany(students);

db.Students.find()