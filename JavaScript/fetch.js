async function handel() {
  try {
    let v = await fetch("https://jsonplaceholder.typicode.com/posts/1");
    
    if (!v.ok) {
      throw new Error(`HTTP Error! Status: ${v.status}`);
    }
    
    let data = await v.json();
    console.log(data);
  } catch (error) {
    console.error("Fetch Failed:", error);
  }
}

handel();
