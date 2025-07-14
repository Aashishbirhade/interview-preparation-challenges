function isdivisor(a){
    let b = []
  for(let i = 0;i<a;i++){
    if(a%i==0){
        
        b.push(i)
    }
  }
    console.log(b)
}
let a = 12
isdivisor(a)
