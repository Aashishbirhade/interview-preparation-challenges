import React from "react";

function Git() {
  return (
    <>
      <div className="flex gap-40 p-8 bg-[#0d1117] text-white">
        <div className="w-1/2 p-4 relative">
          {/* Main Border */}
          <div className="border-t-8 border-b-8 border-l-8 border-white/30 h-[450px] w-3/5 relative">
            {/* Top Right Corner */}
            <div className="absolute top-0 right-0 border-4 border-t-36  border-white/30 "></div>
            {/* Bottom Right Corner */}
            <div className="absolute bottom-0 right-0 border-4 border-b-36 border-white/30 "></div>
          </div>

          <div className="absolute top-32 text-3xl font-extrabold left-24 tracking-wider">
            Using this website has made my tasks so much easier I can't imagine
            my day without it
          </div>
        </div>

        <div className="w-2/5 p-6 ">
            <img src="https://github.githubassets.com/assets/profile-first-pr-dark-bc160471dcac.svg" alt="" className="w-full "/>
        
        </div>
      </div>
    </>
  );
}

export default Git;
