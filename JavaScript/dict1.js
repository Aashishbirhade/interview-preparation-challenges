let d = {veer:12,raaj:22,aashu:34,moru:44};
// let c = Object.entries(d).filter(([key,value])=>{return value< 24})
// console.log(c)
for (let [key,value] of Object.entries(d)){
    if(value < 24){
        console.log(key);
    }
}