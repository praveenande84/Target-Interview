/* -----> Variables <----- */

/*

syntax:
Declaration = Initialization;
declarationKeyword variableName = value;

*/

/* -----> var <----- */

var a;
a = 10;
console.log(a);

a = 20;
console.log(20);

var a = 30;
console.log(a);

console.log('-----------------------');

/* -----> let <----- */

let b;
b = 40;
console.log(b);

// let b = 50; // SyntaxError: Identifier 'b' has already been declared

let c = 60;
console.log(c);

console.log('------------------------');

/* -----> const <----- */

// const d; // SyntaxError: Missing initializer in const declaration

const e = 70;
console.log(e);

// e = 80; // TypeError: Assignment to constant variable

console.log('==========================');
