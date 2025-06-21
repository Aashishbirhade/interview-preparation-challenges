const str_vol =(str)=>{
  let c = str.split('').filter((ele) => {
    return 'aeiouAEIOU'.includes(ele);
  });
    return c
}
console.log(str_vol("Aashish"))