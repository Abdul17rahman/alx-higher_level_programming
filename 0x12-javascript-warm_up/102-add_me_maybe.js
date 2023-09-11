#!/usr/bin/node
module.exports.addMeMaybe = function (x, theFunc) {
  x++;
  theFunc(x);
};
