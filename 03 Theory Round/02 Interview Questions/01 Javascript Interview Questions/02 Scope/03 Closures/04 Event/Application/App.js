// Closures in Events

let button = document.getElementById('button');

function outer() {
	let a = 10;
	let b = 20;
	function inner() {
		console.log(a);
	}
	inner();
}

button.addEventListener('click', outer);
