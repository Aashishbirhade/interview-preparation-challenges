function* generator(){
    console.log("start")
    yield 1
    console.log("middle")
    yield 2
    console.log("end")
    yield 3
}
const gen = generator()
console.log(gen.next()) // { value: 1, done: false }
console.log(gen.next()) // { value: 2, done: false }        
console.log(gen.next()) // { value: 3, done: false }