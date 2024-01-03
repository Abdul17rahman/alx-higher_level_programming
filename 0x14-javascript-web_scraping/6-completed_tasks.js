#!/usr/bin/node
// Get Movies where char is Wedge

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);
  const usrTasks = {};
  const todos = JSON.parse(body);
  const completed = todos.filter(todo => {
    return todo.completed === true;
  });
  completed.forEach(todo => {
    const userId = todo.userId;
    usrTasks[userId] = (usrTasks[userId] || 0) + 1;
  });
  console.log(usrTasks);
});
