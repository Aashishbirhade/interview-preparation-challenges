import React from "react";

function half_border() {
  return (
    <>
      <div className="w-1/2  p-5 relative">
        <div className="grid grid-cols-3 gap- h-96 ">
          <div className="border-4 border-t-red-500 border-l-red-500 border-transparent"></div>
          <div className=""></div>
          <div className="border-4 border-t-red-500 border-r-red-500 border-transparent"></div>
          <div className="border-4 border-b-red-500 border-l-red-500 border-transparent"></div>
          <div className="border-4 border-b-red-500 border-transparent"></div>
          <div className="border-4 border-b-red-500 border-r-red-500 border-transparent"></div>
        </div>

        <div className="absolute top-5  text-lg mx-5 p-4 tracking-widest">
          Aashish Birhade
          <p>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Rerum
            deserunt quam officiis! Assumenda sed eligendi itaque quasi
            dignissimos natus nemo!
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae
            quos, doloremque modi repudiandae amet magnam earum consectetur
            harum repellendus cupiditate debitis iusto! Consectetur voluptatibus
            natus, optio esse rem possimus, enim saepe, dignissimos tempore
            corrupti beatae hic quasi! Ab dicta aliquid, necessitatibus magni
            eos, et tempore atque dolorem, in repellendus nemo!
          </p>
        </div>
      </div>

      <div className="w-1/2 bg-amber-600 ">2</div>
    </>
  );
}

export default half_border;
