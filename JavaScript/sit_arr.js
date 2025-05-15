let n = [10,2,3,50,56,3,66,2]
for(let i = 0; i < n.length; i++){
    for(let j = i + 1; j < n.length; j++){
        if(n[i] > n[j]){
            let temp = n[i]
            n[i] = n[j]
            n[j] = temp
        }
    }
}
console.log(n)