import { useEffect, useState } from "react";
import axios from "axios";
function axio_fetch() {
    const [data,setdata] = useState(null);
    useEffect(()=>{
        axios.get("https://jsonplaceholder.typicode.com/posts/1")
        .then((res)=>setdata(res))
        .catch((error)=>console.error(error))
    },[])
  return (
    <div>
      <p>title= {data.title}</p>
    </div>
  )
}

export default axio_fetch
