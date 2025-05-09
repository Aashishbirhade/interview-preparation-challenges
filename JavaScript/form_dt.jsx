import {react,userState} from react
const Form =()=>{
    
    const [formdata, setformdata] = useState({
        name :"",
        age : "",
        email : ""
    })
    const  submit=(e)=>{
        const {name,value} = e.target()
        setformdata((pre)=>({
            ...pre, [name]:value 
        }))
        e.preventDefault()}

    return(
        <div>
         <form action="post" onSubmit={submit}>
            <label htmlFor="name">Name:</label>
            <input type="text" id="name" name="name" value={formdata.name} onChange={submit} />
            <label htmlFor="age">Age:</label>
            <input type="text" id="age" name="age" value={formdata.age} onChange={submit} />
            <label htmlFor="email">Email:</label>
            <input type="text" id="email" name="email" value={formdata.email} onChange={submit} />
            <input type="submit" value="Submit" />


         </form>
        </div>
    )}

export default Form