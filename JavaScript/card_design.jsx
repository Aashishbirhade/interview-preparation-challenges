import React from 'react';

const InvertedBorderCard = () => {
  return (
<div className="flex items-center justify-center flex-wrap h-screen gap-2.5 p-5 bg-[#22223b] font-jost">
  <div className="relative">
    <div className="w-[25rem] h-[25rem] rounded-[1.25rem] border-[0.5rem] border-[#4a4e69] overflow-hidden relative">
      <img
        src="./src/images/anime/tesla.webp"
        alt="Tesla Roadster"
        className="w-full h-full object-cover"
      />
    </div>

    {/* Title */}
    <div className="w-[12.5rem] h-[3.75rem] flex justify-center items-center absolute top-0 left-0 bg-[#22223b] border-b-[0.5rem] border-r-[0.5rem] border-[#4a4e69] rounded-tr-[1rem] p-[0.3rem]">
      <p className="bg-[#4a4e69] text-white text-[0.875rem] py-[0.3rem] px-[0.625rem] w-[95%] flex justify-center items-center gap-[0.3125rem] rounded-[0.3125rem]">
        <span className="font-semibold text-[1.2rem]">Tesla Roadster</span>
      </p>
    </div>

    {/* Title curves */}
    <div className="w-[1.25rem] h-[1.25rem] absolute top-[15%] left-[0.5rem] border-tl-[0.5rem] shadow-[-0.375rem_-0.375rem_0_0_#4a4e69]"></div>
    <div className="w-[1.25rem] h-[1.25rem] absolute top-[13%] left-0 border-tl-[0.8rem] shadow-[-0.375rem_-0.375rem_0_0_#22223b]"></div>

    {/* Tag */}
    <div className="w-[12.5rem] h-[3.75rem] flex items-center justify-center absolute right-0 bottom-0 bg-[#22223b] border-t-[0.5rem] border-l-[0.5rem] border-[#4a4e69] rounded-tl-[1rem] p-[0.3rem]">
      <p className="bg-[#4a4e69] text-white text-[0.875rem] py-[0.3rem] px-[0.625rem] w-[95%] flex justify-center items-center gap-[0.3125rem] rounded-[0.3125rem]">
        <span className="font-semibold text-[1.2rem]">$200,000</span>
      </p>
    </div>

    {/* Tag curves */}
    <div className="w-[1.25rem] h-[1.25rem] absolute left-[45%] bottom-[0.5rem] border-br-[0.5rem] shadow-[0.375rem_0.375rem_0_0_#4a4e69]"></div>
    <div className="w-[1.25rem] h-[1.25rem] absolute left-[47%] bottom-0 border-br-[0.8rem] shadow-[0.375rem_0.375rem_0_0_#22223b]"></div>
  </div>
</div>
  );
};

export default InvertedBorderCard;
