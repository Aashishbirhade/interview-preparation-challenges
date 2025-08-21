let a = [1,2,3,4,5,6]
let s = 0
let n = a.length-1
while(s<n){
    let t = a[s]
    a[s] = a[n]
    a[n] = t
    s += 1
    n -= 1
}
console.log(a)