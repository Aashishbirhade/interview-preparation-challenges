function first(a, callback) {
    let c = 0;

    function wrapper(b) {
        c++;
        console.log("Count is: " + c);
        return callback(a, b);
    }

    return wrapper;
}

function add(x, y) {
    return x + y;
}

const resultFn = first(10, add);  
console.log(resultFn(20));       
console.log(resultFn(5));        
