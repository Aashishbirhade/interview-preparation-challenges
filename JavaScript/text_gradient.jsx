import React from "react";

function text_gradient() {
  return (
    <>
      <div className="h-screen justify-center content-center">
        <p className="text-2xl font-extrabold bg-gradient-to-r from-blue-500 to-pink-500 bg-clip-text text-transparent ">
          aashish birhade
        </p>
      </div>
      <div className="h-36 w-96 bg-gradient-to-r from-red-500 to-pink-500 rounded-2xl p-1">
        <div className="h-full w-full rounded-2xl bg-black">11</div>
      </div>
    </>
  );
}

export default text_gradient;
