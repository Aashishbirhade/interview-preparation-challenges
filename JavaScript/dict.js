
    let employees =  [
      {
        "id": 101,
        "name": "Amit Sharma",
        "age": 29,
        "department": "Software Development",
        "position": "Senior Developer",
        "salary": 85000,
        "email": "amit.sharma@example.com",
        "phone": "+91 9876543210"
      },
      {
        "id": 102,
        "name": "Priya Verma",
        "age": 26,
        "department": "Human Resources",
        "position": "HR Manager",
        "salary": 65000,
        "email": "priya.verma@example.com",
        "phone": "+91 8765432109"
      },
      {
        "id": 103,
        "name": "Rahul Mehta",
        "age": 32,
        "department": "Marketing",
        "position": "Marketing Lead",
        "salary": 72000,
        "email": "rahul.mehta@example.com",
        "phone": "+91 7654321098"
      },
      {
        "id": 104,
        "name": "Sonia Kapoor",
        "age": 28,
        "department": "Finance",
        "position": "Financial Analyst",
        "salary": 78000,
        "email": "sonia.kapoor@example.com",
        "phone": "+91 6543210987"
      },
     
      {
        "id": 106,
        "name": "Neha Joshi",
        "age": 30,
        "department": "Customer Support",
        "position": "Customer Relations Manager",
        "salary": 70000,
        "email": "neha.joshi@example.com",
        "phone": "+91 4321098765"
      },
      {
        "id": 107,
        "name": "Rohan Das",
        "age": 27,
        "department": "IT Support",
        "position": "System Administrator",
        "salary": 68000,
        "email": "rohan.das@example.com",
        "phone": "+91 3210987654"
      },
    
      {
        "id": 109,
        "name": "Anil Reddy",
        "age": 29,
        "department": "Engineering",
        "position": "Mechanical Engineer",
        "salary": 75000,
        "email": "anil.reddy@example.com",
        "phone": "+91 1098765432"
      },
     
    ]

    employees.forEach((employee,id)=>{
        
        console.log(id+1)
        console.log("Name:"+employee.name)
        console.log("Age:"+employee.age)
        console.log("Email:"+employee.email)
        console.log("Dept:"+employee.department)
        console.log("Position:"+employee.position)
        console.log("Salary:"+employee.salary)
        console.log("++++++++++++++++++++++++++")

    })

    