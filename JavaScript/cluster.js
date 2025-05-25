function first(){
    let count = 0
    function second(){
        count++;
        console.log("Count is: " + count);
    }
    return second;
}
const c = first()
c()