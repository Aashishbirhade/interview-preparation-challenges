async function info(){
    const d = await fetch("https://randomuser.me/api/")
    const data = await d.json()
  
    const user = data.results[0]
    const {title, first, last} = user.name
    console.log("Name :",title, first, last)
    console.log("Email :",user.email)
    console.log("DOB :",user.dob.age)

}
info()




async function info(count) {
    const response = await fetch(`https://randomuser.me/api/?results=${count}`);
    const data = await response.json();
    
    data.results.forEach((user, index) => {
        const { title, first, last } = user.name;
        console.log(`Person ${index + 1}:`);
        console.log("Name:",first, last);
        console.log("Email:", user.email);
        console.log("DOB (Age):", user.dob.age);
        console.log("Phone No:",user.phone)
        console.log("------------------");
    });
}


info(5);
