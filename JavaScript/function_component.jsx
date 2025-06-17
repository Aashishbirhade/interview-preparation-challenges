import React, { useState } from 'react';

function V() {
  // State declaration
  const [count, setCount] = useState(0);

  // Event handler
  function increment() {
    setCount(count + 1);
  }

  return (
    <>
      <div>
        <h1>Count: {count}</h1>
        <button onClick={increment}>Increment</button>
      </div>
    </>
  );
}

export default V;
