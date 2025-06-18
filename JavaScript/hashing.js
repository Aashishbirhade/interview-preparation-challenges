const express = require("express");
const app = express();
const bcrypt = require("bcrypt");


app.get("/", (req, res) => {
  res.send("hello bhau");
});

app.get("/create", async (req, res) => {
  const { username,email, password } = req.body;
  const salt = 10;
  const hash = await bcrypt.hash(password, salt);
  console.log(hash);
  const user = await userModel.create({
    username,
    email,
    password: hash,
  });
  
  res.send("user created",user);
});
app.get("/login", async (req, res) => {
  const { username, password } = req.body;
  const user = await userModel.findOne({ username });
  if (!user) {
    return res.status(400).send("user not found");
  }
  const isMatch = await bcrypt.compare(password, user.password);
  if (!isMatch) {
    return res.status(400).send("invalid credentials");
  }
  res.send("login successful");
});
app.listen(3000, () => {
  console.log("server is running on port 3000");
});
