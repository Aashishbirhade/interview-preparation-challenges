let li = [1,2,3,4,5,6,7,8,9,10]
v = 3
for (let i = 0;i<v;i++){
    for(let j = li.length-1;j>0;j--){
       [ li[j],li[j-1]] = [li[j-1],li[j]]
    }
}
console.log(li)