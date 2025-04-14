let a = "DAs"
let i = 0
let j = a.length-1
while (i<j){
    if (a[i]!=a[j]){
        console.log("not palindrome")
        break
    }
    i++
    j--
}