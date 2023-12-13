#!/usr/bin/node
/* a script that imports a dictionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence. */
const data = require('./101-data');

const occurrencesDict = data.dict;
const usersByOccurrence = {};

for (const userId in occurrencesDict) {
  const occurrence = occurrencesDict[userId];

  if (!usersByOccurrence[occurrence]) {
    usersByOccurrence[occurrence] = [];
  }

  usersByOccurrence[occurrence].push(userId);
}

console.log(usersByOccurrence);
