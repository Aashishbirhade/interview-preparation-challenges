a = [
  {
    id: 1,
    name: "Aashish",
    age: 42,
    roll: 10,
  },
  {
    id: 2,
    name: "veer",
    age: 40,
    roll: 10,
  },
  {
    id: 3,
    name: "moru",
    age: 40,
    roll: 10,
  },
];
console.log(a);
a.map((v,i) =>{
    console.log(i)
    console.log(v.name ,v.age , v.roll)
})
