#!/usr/bin/node
// 6-Square

class Square extends require('./5-square') {
  charPrint (c) {
    /* !c ? c = 'X' : c; */
    if (!c) {
      this.print();
    } else {
      if (this.width && this.height) {
        let rect = '';
        for (let i = 0; i < this.width; i++) { // build one line
          rect += 'C';
        }
        for (let j = 0; j < this.height; j++) { // output several lines
          console.log(rect);
        }
      }
    }
  }
}

/* module.exports = Rectangle; */
module.exports = Square;
