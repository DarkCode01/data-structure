"use strict";

function List() {
  this.listSize = 0;
  this.pos = 0;
  this.dataStore = [];
};

List.prototype.append = function(element) {
  this.dataStore[this.listSize++] = element
}

List.prototype.find = function(element) {
  for (const index in this.dataStore) {
    if (element == this.dataStore[index]) {
      return parseInt(index);
    }
  }

  return -1;
}

List.prototype.remove = function(element) {
  const pos = this.find(element);

  if (pos !== -1) {
    this.dataStore.splice(pos, 1);
    --this.listSize;
    return true;
  }

  return false;
}

List.prototype.length = function() {
  return this.listSize;
}

List.prototype.toString = function() {
  return this.dataStore;
}

List.prototype.insert = function(element, after) {
  const pos = this.find(after);

  if (pos !== -1) {
    this.dataStore.splice(pos + 1, 0, element);
    ++this.listSize;
    return true;
  }

  return false;
}

List.prototype.clear = function() {
  this.dataStore = [];
  this.listSize = 0;
  this.pos = 0;
}

List.prototype.contains = function(element) {
  return this.find(element) !== -1;
}

List.prototype.moveTo = function(position) {
  this.pos = position;
}

List.prototype.getElement = function() {
  this.dataStore[this.pos];
}



module.exports = List;