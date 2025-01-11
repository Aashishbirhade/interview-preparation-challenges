const a = ["Aashish", "moru", "jayesh"];
const v = ["student", "employee", "developer", "designer"];

// Shuffle the `v` array
const shuffledV = v.sort(() => Math.random() - 0.5);
console.log(shuffledV,Math.random()-0.5)
// Ensure `v` has at least as many elements as `a`
if (shuffledV.length < a.length) {
    console.error("Not enough roles in 'v' for each name in 'a'");
} else {
    a.forEach((e, i) => console.log(e + " " + shuffledV[i]));
}
