import React,{useState,useEffect} from 'react'

function Frontend() {
    const [Form, setForm] = useState(
        {
            name:"",
            age:"",
            email:"",
            Password:"",
        })
    
    const [User, setUser] = useState([])
    const onchange = (e) => {
        const{name,value}= e.target
        setForm(prev =>({
            ...prev,[name]:value
        }))
    }

    const handlesubmit =(e)=>{
        e.preventDefault()
        try{
            fetch(`localhost:3000/test?name=${form.name}&age=${form.age}&email=${form.email}&password=${form.Password}`)
            setForm({
                name:"",
                age:"",
                email:"",
                Password:"",
            })
        }
        catch(err){
            console.log(err)
        }
    }
    useEffect(()=>{
        fetchuser()
    },[])
    const fetchuser = async ()=>{
        try{
            const res = await fetch('http://localhost:3000/test')
            const data = await res.json()
            setUser(data)
        }
        catch(err){
            console.log(err)
        }
    }

  return (
   <>
   <div>
        <form action="" onSubmit={handlesubmit}>
            <input type="text" name="name" placeholder='Name' onChange={handlechange} />
            <input type="text" name="age" placeholder='Age' onChange={handlechange} />
            <input type="email" name="email" placeholder='Email' onChange={handlechange} />
            <input type="password" name="Password" placeholder='Password' onChange={handlechange} />
            <button type='submit'>Submit</button>
        </form>
   </div>
   </>
  )
}

export default Frontend
