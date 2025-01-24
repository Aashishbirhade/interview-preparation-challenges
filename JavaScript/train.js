const fetchData = async () => {
    const data = JSON.stringify({ search: "Vande Bharat Express " });

    try {
        const response = await fetch("https://trains.p.rapidapi.com/v1/railways/trains/india", {
            method: "POST",
            headers: {
                "x-rapidapi-key": "4baa0ca40bmsh10cd84246b04162p11f193jsnf1185f5fb777",
                "x-rapidapi-host": "trains.p.rapidapi.com",
                "Content-Type": "application/json"
            },
            body: data
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const result = await response.json();
        console.log("API Response: ", result);
    } catch (error) {
        console.error("Error occurred: ", error.message);
    }
};

fetchData();
