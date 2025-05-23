let pro = new Promise((resolve,reject) =>{
let success = false
if(success){
    resolve("success")
}
else{
    reject("failed")
}
})


pro.then((res)=>{
    console.log(res)
})
.catch((err)=>{
    console.log(err)
})