#!/usr/bin/node

// Export the logMe function as a module
exports.logMe = function (item) { 
    console.log(`${count++}: ${item}`); // Log the count and the provided item
};