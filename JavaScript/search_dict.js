let a = {aashu:12, raaj: 22, veer: 34, moru: 44};
key = 'veer';
let c = Object.entries(a).filter(([k,v])=>{
    if(k==key){
        return "Key found: " + k + " with value: " + v;
    }
    
})
console.log(c)