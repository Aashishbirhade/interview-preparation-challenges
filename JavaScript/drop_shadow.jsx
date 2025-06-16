import React from 'react'

function v() {
  return (
    <>
    <div>
        <div className=' text-white p-8 bg-black md:flex flex-wrap'>
            <div className=' md:leading-12 text-lg md:text-3xl md:p-10  w-full  text-shadow-sm tracking-wider md:w-1/2'>The story follows a young ninja, Naruto Uzumaki, on his journey to become the Hokage, or head ninja, of his village. The manga was first released in installments in the Japanese magazine Weekly Shonen Jump. Publishers later collected the installments and presented them in book form.</div>
            <img src="./src/images/anime.png" alt="" className=' drop-shadow-lg mx-auto drop-shadow-amber-300' />
        </div>
        <div className='flex items-center justify-center text-center'>
            <div className='bg-red-300 w-1/2'>left</div>
            <div className='w-1 h-72 mx-auto bg-black'></div>
            <div className='bg-pink-800 w-1/2'>right</div>
        </div>
       
    </div>
    </>
  )
}

export default v
