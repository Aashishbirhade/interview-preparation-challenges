import React from "react"

function Design(){
    return(
         <div className="py-20 bg-gradient-to-b from-blue-600  to-black/95">
        <div className="flex w-4/5 m-auto rounded-2xl bg-black text-lg  text-white text-center">
        <div className="w-1/2 pt-16">
          <div className="mx-10 text-left">
            <h1 className="font-extrabold text-4xl my-10">Automation reliability </h1>{" "}
          <p className=" hyphens-auto tracking-wider">
            Streamlining business and infrastructure operations with process
            automation, hyper-automation, and agentic solutions, enabling
            seamless workflows, compliance, cloud modernization, and optimized
            FinOps, CloudOps, and DevSecOps for scalable efficiency.
          </p>
          </div>
        </div>
        <div className="">
          {/* Dark Image (default) */}
          <img
            src="https://qualitykiosk.com/wp-content/uploads/2025/07/img-automation-reliability-hover.png"
            alt="Dark Eye"
            className=" inset-0 w-full h-full object-cover transition duration-500 grayscale hover:grayscale-0"
          />
        </div>
      </div>
      </div>

    )
}
export default Design