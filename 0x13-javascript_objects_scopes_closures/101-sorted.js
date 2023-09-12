#!/usr/bin/node
const dict = require('./101-data.js').dict; // Import the original dictionary

let newDict = {}; // Create a new empty dictionary for the swapped data

// Iterate through the original dictionary
for (let key in dict) {
  // Check if the value from the original dictionary is a key in the new dictionary
  if (newDict[dict[key]] === undefined) {
    // If it's not, create a new array with the current key as its first element
    newDict[dict[key]] = [key];
  } else {
    // If it is, push the current key into the existing array
    newDict[dict[key]].push(key);
  }
}

console.log(newDict); // Log the new dictionary with swapped keys and grouped values
