function prime(a){
    for(let i = 2; i<=a/2;i++){
        if (a%i==0){
            return "not prime"
        }
    }
    return "prime"
}

let  a = 3

console.log(prime(a))