const isrev = (a)=>{
    rev = ""
    for(let i = 0; i < a.length; i++){
        rev = a[i] + rev
    }
    return rev
}


let a = "Aashish"
console.log(isrev(a))