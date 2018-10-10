use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        panic!("Please provide an argument.");
    }
    match args[1].parse::<i64>() {
        Ok(num) => {
            if num % 9 == 0 {
                println!("Dividable by 9.");
            } else {
                println!("Not dividable by 9.");
            }
        },
        Err(_) => {
            println!("Please provide a number as argument.");
        }
    }
}
