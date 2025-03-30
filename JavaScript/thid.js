const API_KEY = "";

const payload = {
  image_url: "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg", 
  enable_pbr: true,
  should_remesh: true,
  should_texture: true
};

const convertImageTo3D = async () => {
  try {
    const response = await fetch('https://api.meshy.ai/openapi/v1/image-to-3d', {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log("3D Model Response:", data);
  } catch (error) {
    console.error("Error:", error.message);
  }
};

convertImageTo3D();



