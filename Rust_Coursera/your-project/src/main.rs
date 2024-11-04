#starting to work with rust, thanks to coursera, https://www.coursera.org/learn/rust-fundamentals/home/module/1
fn main() {
    println!("Hello, world!");
}

// create a function that finds out the average of several numbers and return it 
fn average(numbers: &[i32]) -> f64 {
    let sum: i32 = numbers.iter().sum();
    let count = numbers.len();
    sum as f64 / count as f64
}
