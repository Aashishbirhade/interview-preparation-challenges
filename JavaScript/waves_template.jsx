
import React from "react"

function animation(){
  return(
    <>
    <div className="flex flex-col">
      <div className="h-[500px] md:flex text-white  bg-[#45150e]">
        <div className="w-1/2  flex justify-center text-3xl hyphens-auto tracking-widest px-8 font-extrabold leading-12 items-center">
        <p>Virat Kohli is a world-renowned Indian cricketer known for his aggressive batting style and exceptional consistency. He has captained the Indian national team across all formats and is considered one of the greatest batsmen of his generation.
        </p>
        </div>
        <div className="w-1/2 py-10 "><img src="./src/images/anime/thor.png" alt="" className="mx-auto w-3/5  "/></div>
      </div>
      <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100"><g fill="#45150e"><path d="M0 0v99.7C62 69 122.4 48.7 205 66c83.8 17.6 160.5 20.4 240-12 54-22 110-26 173-10a392.2 392.2 0 0 0 222-5c55-17 110.3-36.9 160-27.2V0H0Z" opacity=".5"></path><path d="M0 0v74.7C62 44 122.4 28.7 205 46c83.8 17.6 160.5 25.4 240-7 54-22 110-21 173-5 76.5 19.4 146.5 23.3 222 0 55-17 110.3-31.9 160-22.2V0H0Z"></path></g></svg></div>
    </div>
    </>
  )

}
export default animation 