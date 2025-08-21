// function isprime(a){
//  for (let i = 2;i<a;i++){
//     if (a%i==0){
//         return false
//     }
//  }
//  return true
// }

// let a =  10
// let b = []
// let c = []
// for (let i = 2; i <= a; i++){
//     if (isprime(i)){
//         b.push(i)
//     } else {
//         c.push(i)
//     }
// }
// console.log("Prime No: ",b)
// console.log("Non Prime No: ",c)


function prime_no(a){
    let f = true 
    for(let i = 2; i<a;i++){
        if(a%i==0){
          f = false
          return f 
        }
    }
    return f
}
let v = prime_no(25)
if(v){
    console.log("yes")
}
else{
    console.log("no")
}