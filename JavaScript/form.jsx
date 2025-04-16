import {React,UseState} from React
function Form(){
const [Name, setName] = UseState("")

return (
 <form action="post">
    <label htmlFor="name">Name:</label>
    <input type="text" id="name" name="name" value={Name} onChange={(e) => setName(e.target.value)} />
    <input type="submit" value="Submit" />
    <p>{Name}</p>
 </form>
)
}

export default Form