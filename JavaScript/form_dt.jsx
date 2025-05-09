import React, { useState } from "react";

const Form = () => {
  const [formdata, setFormdata] = useState({
    name: "",
    age: "",
    email: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormdata((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault(); // page reload hone se rokta hai
    console.log("Form submitted:", formdata);
    
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="name">Name:</label>
      <input
        type="text"
        id="name"
        name="name"
        value={formdata.name}
        onChange={handleChange}
      />

      <label htmlFor="age">Age:</label>
      <input
        type="text"
        id="age"
        name="age"
        value={formdata.age}
        onChange={handleChange}
      />

      <label htmlFor="email">Email:</label>
      <input
        type="text"
        id="email"
        name="email"
        value={formdata.email}
        onChange={handleChange}
      />

      <input type="submit" value="Submit" />
    </form>
  );
};

export default Form;
