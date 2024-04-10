#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    /* Instantiate only if w and h are positive ints > 0 */
    if ((w && h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
