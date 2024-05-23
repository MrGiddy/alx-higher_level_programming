#!/usr/bin/node
// Computes the number of tasks completed by user id

// Import the request module
const request = require('request');

// Get API URL: https://jsonplaceholder.typicode.com/todos
const url = process.argv[2];

// Request all the tasks and count only those completed per user id
request(url, (err, resp, body) => {
  if (err) console.log(err);

  // Convert JSON string to JS Object
  const todos = JSON.parse(body);

  const countRecord = {};
  // For each task
  todos.forEach((todo) => {
    // If the task is completed
    if (todo.completed === true) {
      // If it is not yet in countRecord object
      if (!(todo.userId in countRecord)) {
        // Set completion count for the task as 1
        countRecord[todo.userId] = 1;
      } else {
        // Increment completion count for the task
        countRecord[todo.userId] += 1;
      }
    }
  });
  console.log(countRecord);
});
