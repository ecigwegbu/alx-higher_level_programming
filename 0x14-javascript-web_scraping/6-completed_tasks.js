#!/usr/bin/node
// computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2]; // https://jsonplaceholder.typicode.com/todos
request(url, function (body, response) {
  const tasks = JSON.parse(response.body);

  const userTasks = {};
  for (const task of tasks) {
    // console.log(task.title);
    if (task.completed === true) {
      // check if userid exists in userTasks
      if (Object.keys(userTasks).includes(task.userId.toString())) {
        // increment count by 1
        userTasks[task.userId] = userTasks[task.userId] + 1;
      } else {
        // add new user_Id to userTasks
        userTasks[task.userId] = 1;
      }
    }
  }
  console.log(userTasks);
});
