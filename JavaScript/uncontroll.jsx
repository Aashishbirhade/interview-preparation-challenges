import React, { useRef } from 'react';

function ControlledForm() {
  const name = useRef(null);
  
  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Submitted Name: ${name.current.value}`);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>Enter Name: </label>
      <input type="text" ref={name} />
      <button type="submit">Submit</button>
    </form>
  );
}

export default ControlledForm;
