import {userState,useEffect} from react


// Tujhe kaise yaad rahega useEffect kab use karna hai?
// "Kya mujhe component load hote hi kuch karna hai?" 👉 useEffect with []
// "Kya mujhe kisi state/prop ke badlav pe kuch karna hai?" 👉 useEffect with [dependency]
// "Kya mujhe kuch clean-up karna hai?" 👉 return function inside useEffect
function Practice(){
    const [count, setCount] = userState(0);

    useEffect(() => {
        console.log("Component mounted or updated");
        return () => {
            console.log("Component unmounted");
        };
    }, [count]);

    return (
        <div>
            <h1>Count: {count}</h1>
            <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
    );
}