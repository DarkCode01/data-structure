"use strict";
const Node = require("../node/node");

function BST() {
  this.root = null;
}

BST.prototype.insert = function(value) {
  const node = new Node(value, null, null);

  if (!this.root) {
    this.root = node;
  } else {
    let current = this.root;
    let parent;

    while(true) {
      parent = current;
      
      if (node.data < parent.data) {
        current = current.left;
        if (!current) {
          parent.left = node;
          break;
        }
      } else {
        current = current.right;

        if (!current) {
          parent.right = node;
          break;
        }
      }
    }
  }
}

BST.prototype.inOrder = function(node) {
  if (node) {
    this.inOrder(node.left);
    console.log(`${node.show()} `);
    this.inOrder(node.right);
  }
}

BST.prototype.preOrder = function(node) {
  if (node) {
    console.log(`${node.show()} `);
    this.preOrder(node.left);
    this.preOrder(node.right);
  }
}

BST.prototype.postOrder = function(node) {
  if (node) {
    this.postOrder(node.left);
    this.postOrder(node.right);
    console.log(`${node.show()} `);
  }
}

BST.prototype.getMin = function() {
  let current = this.root;
  while (current.left) {
    current = current.left;
  }

  return current;
}

BST.prototype.getMax = function() {
  let current = this.root;
  while (current.right) {
    current = current.right;
  }

  return current;
}

BST.prototype.find = function(data) {
  let current = this.root;

  while (current && current.data !== data) {
    if (data < current.data) {
      current = current.left;
    } else {
      current = current.right;
    }
  }

  return current;
}

module.exports = BST;
