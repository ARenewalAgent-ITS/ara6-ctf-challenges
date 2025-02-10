use std::io::{self, Write};

fn no() {
	println!("That is... wrong.");
}

fn yes() {
	println!("Yes! This one you got it right!");
}

fn main() {
	println!("Hello! I recently learned Rust because of the hype on memory-safe low-level programming language");
	println!("Now, I wanted you to reverse how do beginners think when they wrote a Rust program. GLHF!");

	let mut input = String::new();
	print!(">> ");
	io::stdout().flush().unwrap();
	io::stdin().read_line(&mut input);
	input.pop();

	if input.starts_with("ARA6") == false {
		return no();
	}

	if (input.chars().nth(4) == Some('{')) == false {
		return no();
	}

	let mut c: u32 = 5;
	let mut i: u8 = 0;
	'outer: loop {
		let mut j: u8 = 0;
		'inner: loop {
			let ch: char = {
				unsafe {
					let mine: u8 = 'A' as u8 - 1 + ((i + j) % 26);
					mine as char
				}
			};
			if input.chars().nth((c) as usize) != Some(ch) {
				return no();
			}
			j += 1;
			c += 1;
			if j == 15 {
				break 'inner;
			}
			if i == 4 {
				break 'outer;
			}
		}
		i += 1;
	}

	if (input.pop() == Some('}')) == false {
		return no();
	}

	// We pop the last character '}' previously, so we adding one here
	if (input.len()+1) != 67 {
		return no();
	}

	yes()
}
