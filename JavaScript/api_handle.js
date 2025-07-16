// async function info(){
//     const d = await fetch("https://randomuser.me/api/")
//     const data = await d.json()
  
//     const user = data.results[0]
//     const {title, first, last} = user.name
//     console.log("Name :",title, first, last)
//     console.log("Email :",user.email)
//     console.log("DOB :",user.dob.age)

// }
// info()




// async function info(count) {
//     const response = await fetch(`https://randomuser.me/api/?results=${count}`);
//     const data = await response.json();
//     //user : for contain and index for no
//     data.results.forEach((user, index) => {
//         const { title, first, last } = user.name;
//         console.log(`Person ${index + 1}:`);
//         console.log("Name:",first, last);
//         console.log("Email:", user.email);
//         console.log("DOB (Age):", user.dob.age);
//         console.log("Phone No:",user.phone)
//         console.log("------------------");
//     });
// }


// info(5);



async function temp(){
    let res = await fetch("https://jsonplaceholder.typicode.com/posts?_limit=20")
    let data = await res.json()
    
    console.log(data)
}
temp()