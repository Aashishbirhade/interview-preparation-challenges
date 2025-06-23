import React from "react";

function v() {
  return (
    <>
      <div className="flex gap-40 p-8">
        {/* <div className=' text-white p-8 bg-black md:flex flex-wrap'>
            <div className=' md:leading-12 text-lg md:text-3xl md:p-10  w-full  text-shadow-sm tracking-wider md:w-1/2'>The story follows a young ninja, Naruto Uzumaki, on his journey to become the Hokage, or head ninja, of his village. The manga was first released in installments in the Japanese magazine Weekly Shonen Jump. Publishers later collected the installments and presented them in book form.</div>
            <img src="./src/images/anime.png" alt="" className=' drop-shadow-lg mx-auto drop-shadow-amber-300' />
        </div> */}

        <div className="w-1/2 p-4 relative">
  {/* Main Border */}
  <div className="border-t-8 border-b-8 border-l-8 border-red-500 h-[450px] w-3/5 relative">
    {/* Top Right Corner */}
    <div className="absolute top-0 right-0 border-4 border-t-36  border-red-500"></div>
    {/* Bottom Right Corner */}
    <div className="absolute bottom-0 right-0 border-4 border-b-36 border-red-500"></div>
  </div>

  <div className="absolute top-32 text-3xl font-extrabold left-24 tracking-wider">
    Using this website has made my tasks so much easier I can't imagine my day without it
  </div>
</div>

<div className="w-2/5 p-6 ">
  <div className="border-t-8 border-b-8 border-r-8 border-red-500 h-9/12 w-3/4 m-auto my-8 p-1 relative">
  {/* Top Left Corner */}
  <div className="absolute top-0 left-0  border-t-8 border-red-500 bg-white"></div>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtCJFXiUK-7kcHNgjXL2E3b4dA1tQ5k1kCew&s" alt="" className="h-full w-full" />

  {/* Bottom Left Corner */}
  <div className="absolute bottom-0 left-0  border-b-8 border-red-500 bg-white"></div></div>
  
</div>

      </div>
    </>
  );
}

export default v;
