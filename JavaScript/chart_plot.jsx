// npm install recharts
import React from "react";
import { LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer} from "recharts"
// LineChart → Main chart box
// Line → Chart ki line draw karta hai
// XAxis → Horizontal axis
// YAxis → Vertical axis
// CartesianGrid → Background grid lines
// Tooltip → Hover karne par values show hoti hain
// ResponsiveContainer → Chart ko responsive banata hai
  const d = [
    {name:"veer",sales:200},
    {name:"raaj",sales:300},
    {name:"karan",sales:100},
    {name:"aashu",sales:500},
    {name:"ramu",sales:400},
  ]

  function Sale() {
    return (
    <div className="w-full max-w-2xl mx-auto p-4 bg-white shadow-lg rounded-2xl">
      <h2 className="text-xl font-bold text-center mb-4">Monthly Sales</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={d}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="sales" stroke="#f97316" strokeWidth={3} />
        </LineChart>
      </ResponsiveContainer>
    </div>
    )
  }
  export default Sale