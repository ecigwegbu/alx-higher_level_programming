#!/usr/bin/node
// An empty rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      let rect = '';
      for (let i = 0; i < this.width; i++) { // build one line
        rect += 'X';
      }
      for (let j = 0; j < this.height; j++) { // output several lines
        console.log(rect);
      }
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
