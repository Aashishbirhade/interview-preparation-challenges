let arr = [1,2,34,2,53,6,44]
let k = 44
let n = arr.length
for (let i = 0;i<n;i++){
    if (arr[i]==k){
        console.log("key is found at index of "+i)
        break
    }
}