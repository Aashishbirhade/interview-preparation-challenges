let x = 6
const a = [5,4,6,2,7]
let max = a[0]
let c = 1
for(let i = 1;i <a.length;i++){
    if(max < a[i]){
        max = a[i]
        c += 1
    }
}
console.log("count of max is "+c)